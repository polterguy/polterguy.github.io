
# NoSQL based IO, caching, and logging adapters for Hyperlambda

This project contains alternative NoSQL file system services, implementing `IFileService`, `IFolderService`, and
`IStreamService`, allowing you to use it as an interchangeable _"virtual file system"_ for cases where you want
to have 100% stateless magic instances. This is important if you're using Magic in a Kubernetes cluster or
something similar, load balancing invocations, virtually resolving files and folders towards a virtual file system.
If you take this path you'll have to configure your _"appsettings.json"_ file such as illustrated further
down in this document. The project also contains an `ILogger` implementation service you can use that will create
log entries in a NoSQL based storage of your choice, in addition to an `IMagicCache` implementation service
allowing you to use a NoSQL based out of process cache implementation. See further down in this document for
details about how to configure these parts.

## Configuration

The primary configuration for the project to apply for your _"appsettings.json"_ file can be found below. Notice,
although you can create as many NoSQL cluster connection settings as you wish, and use these in your own code,
the IO, caching, and logging services requires you to use `generic` as your cluster name, and you cannot change
this.

```
{
  "magic": {
    "cql": {
      "generic": {
        "host": "127.0.0.1",
        "credentials": {
          "username": "xxx",
          "password": "xxx"
        },
        "port": 12345
      }
    }
  }
}
```

**Notice** - The _"credentials"_ parts above are optional, and can be ommitted if you don't require
authentication to connect to your database. You can also provide multiple hosts as contact points,
by separating multiple IP addresses or hosts by a comma (,). The above _"port"_ parts is also
optional.

The above configures the adapter to use `127.0.0.1` as the host for your contact point or cluster. To configure
the adapter to store files and folders inside of its CQL based database, you can alternatively add something such
as follows to your _"appsettings.json"_ file.

```
{
  "magic": {
    "io": {
      "file-service": "magic.data.cql.io.CqlFileService",
      "folder-service": "magic.data.cql.io.CqlFolderService",
      "stream-service": "magic.data.cql.io.CqlStreamService"
    }
  }
}
```

**Notice** - This project also includes a _"mixed"_ service implementation, storing system files and folders
in the file system while storing dynamic files and folders in a NoSQL database of your choice. These
can be found in the same namespace, but are named _"MixedXXX"_ instead of using the above names.

If you want to use a CQL based log implementation, you'll have to configure Magic to use the NoSQL
`ILogger` service such as follows.

```
{
  "magic": {
    "logging": {
      "service": "magic.data.cql.logging.Logger"
    }
  }
}
```

If you want to use a CQL based caching implementation, you'll have to configure Magic to use the NoSQL
`IMagicCache` service such as follows.

```
{
  "magic": {
    "caching": {
      "service": "magic.data.cql.caching.Caching"
    }
  }
}
```

## Schemas

To use the alternative CQL based file storage system you'll have to create your _"magic\_files"_ keyspace and its 
_"files"_ table as follows.

```sql
create keyspace if not exists magic_files with replication = { 'class': 'NetworkTopologyStrategy', 'replication_factor': 5 };

use magic_files;

create table if not exists files(
   tenant text,
   cloudlet text,
   folder text,
   filename text,
   content blob,
   primary key((tenant, cloudlet), folder, filename));
```

To use the alternative CQL based logging implementation you'll have to create your _"magic\_log"_ keyspace and its
_"log"_ table as follows.

```sql
create keyspace if not exists magic_log with replication = { 'class': 'NetworkTopologyStrategy', 'replication_factor': 3 };

use magic_log;

create table if not exists log(
   tenant text,
   cloudlet text,
   created timeuuid,
   type text,
   content text,
   exception text,
   meta frozen<map<text, text>>,
   primary key((tenant, cloudlet), created)) with clustering order by (created desc);

alter table log with default_time_to_live = 1209600;
```

**Notice** - The above setting for TTL implies log items will be automatically evicted after 14 days,
since 1,209,600 seconds implies 14 days. Depending upon your needs you might want to increase or decrease this
setting. However, to avoid exhausting your hard drive space over time on your server, we suggest you do _not_
entirely remove the TTL setting.

To use the alternative CQL based caching implementation you'll have to create your _"magic\_cache"_ keyspace and its
_"cache"_ table as follows.

```sql
create keyspace if not exists magic_cache with replication = { 'class': 'NetworkTopologyStrategy', 'replication_factor': 3 };

use magic_cache;

create table if not exists cache(
   tenant text,
   cloudlet text,
   key text,
   value text,
   primary key((tenant, cloudlet), key));
```

## Adding existing files into NoSQL database

The following Hyperlambda will insert all your existing files and folders into your cluster keyspace, allowing you to
play around with an existing CQL file system implementation. Notice, you'll have to change the **[.tenant]** and
**[.cloudlet]** values to resemble the absolute root folder for your Magic backend. The values in the file below is
obviously just an example of how it might look like if you've got the files on a Mac within your _"Documents"_ folder.
The _"tenant"_ and the _"cloudlet"_ parts are resolved by doing a string split operation on your `magic:io:root-files`
root folder upon the last (/) found in your folder - Implying if you use the Docker images with the default configuration
the _"tenant"_ part would become _"magic"_ and the _"cloudlet"_ part would become _"files"_, since the Docker images
stores files within the _"/magic/files/"_ folder.

```
/*
 * Inserts all dynamic files and folders into the magic CQL database.
 */
cql.connect:[generic|magic_files]

   /*
    * The root folder where your Magic backend is running.
    */
   .tenant:Users
   .cloudlet:"thomashansen/Documents/projects/magic/magic/backend"

   /*
    * Inserting root folder.
    */
   cql.execute:"insert into files (tenant, cloudlet, folder, filename) values (:tenant, :cloudlet, '/files/', '')"
      tenant:x:@.tenant
      cloudlet:x:@.cloudlet

   /*
    * Inserting appsettings.json and its folder.
    */
   config.load
   convert:x:-
      type:bytes
   cql.execute:"insert into files (tenant, cloudlet, folder, filename, content) values (:tenant, :cloudlet, '/config/', 'appsettings.json', :config)"
      tenant:x:@.tenant
      cloudlet:x:@.cloudlet
      config:x:@convert
   cql.execute:"insert into files (tenant, cloudlet, folder, filename) values (:tenant, :cloudlet, '/config/', '')"
      tenant:x:@.tenant
      cloudlet:x:@.cloudlet

   /*
    * Inserting folders.
    */
   io.folder.list-recursively:/
      display-hidden:true
   for-each:x:-/*

      strings.concat
         .:/files
         get-value:x:@.dp/#
      
      cql.execute:"insert into files (tenant, cloudlet, folder, filename) values (:tenant, :cloudlet, :folder, '')"
         tenant:x:@.tenant
         cloudlet:x:@.cloudlet
         folder:x:@strings.concat

   /*
    * Inserting files.
    */
   io.file.list-recursively:/
      display-hidden:true
   for-each:x:-/*

      io.file.load.binary:x:@.dp/#
   
      strings.split:x:@.dp/#
         .:/
      unwrap:x:+
      .filename:x:@strings.split/0/-
      remove-nodes:x:@strings.split/0/-
      strings.join:x:@strings.split/*
         .:/
      strings.concat
         .:/files/
         get-value:x:@strings.join
         .:/
      strings.replace:x:-
         .://
         .:/
      cql.execute:"insert into files (tenant, cloudlet, folder, filename, content) values (:tenant, :cloudlet, :folder, :filename, :content)"
         tenant:x:@.tenant
         cloudlet:x:@.cloudlet
         folder:x:@strings.replace
         filename:x:@.filename
         content:x:@io.file.load.binary

remove-nodes:x:../**/io.folder.list-recursively/*
remove-nodes:x:../**/io.file.list-recursively/*
```

## Internals

This project is created to be a multi-tenant solution, implying multiple users, and/or cloudlets, can use the same physical
database for both files, log entries, and cache entries. However, this implies you are able to correctly resolve the 
_"tenant"_ parts and the _"cloudlet"_ parts for all the above tables. How to achieve this is currently beyond the scope
of this document, but our suggestion is to create some sort of `IRootResolver` service implementation that is dynamically
created according to the `Host` HTTP header of requests.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.data.cql](https://github.com/polterguy/magic.data.cql), and you can provide feedback, provide bug reports, etc at the same place.

- ![Build status](https://github.com/polterguy/magic.data.cql/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.cql)
