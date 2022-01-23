
# CQL IO and logging adapters for Hyperlambda

This data adapter contains alternative NoSQL file system services, implementing `IFileService`, `IFolderService`, and
`IStreamService`, allowing you to use as an interchangeable _"virtual file system"_ for cases where you want
to have 100% stateless magic instances, which is important if you're using Magic in a Kubernetes cluster or
something similar, load balancing invocations, virtually resolving files and folders towards a virtual file system.
If you take this path you'll have to configure your _"appsettings.json"_ file such as illustrated further
down in this document. The project also contains an `ILogger` implementation service you can use that will create
log entries in a NoSQL based storage of your choice. See below for details about how to configure this.

## Configuration

The primary configuration for the project to apply for your _"appsettings.json"_ file can be found below. Notice,
the IO and log services requires you to use `generic` as your cluster name, and you cannot change this.

```json
{
  "magic": {
    "cql": {
      "generic": {
        "host": "127.0.0.1"
      }
    }
  }
}
```

The above configures the adapter to use `127.0.0.1` as the host for your contact point or cluster. To configure
the adapter to store files and folders inside of its CQL based database, you can alternatively add something such
as follows to your _"appsettings.json"_ file.

```json
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

If you want to use a CQL based log implementation, you'll have to configure Magic to use the NoSQL
`ILogger` service such as follows.

```json
{
  "magic": {
    "logging": {
      "service": "magic.data.cql.logging.Logger"
    }
  }
}
```

## Schema

To use the alternative CQL based file storage system you'll have to create your _"magic"_ keyspace and its 
_"files"_ table as follows.

```cql
create keyspace if not exists magic with replication = { 'class': 'NetworkTopologyStrategy', 'replication_factor': 5 };

use magic;

create table if not exists files(
   tenant text,
   cloudlet text,
   folder text,
   filename text,
   content blob,
   primary key((tenant, cloudlet), folder, filename));
```

To use the alternative CQL based log implementation you'll have to create your _"magic"_ keyspace and its
_"log_entries"_ table as follows.

```cql
create keyspace if not exists magic with replication = { 'class': 'NetworkTopologyStrategy', 'replication_factor': 5 };

use magic;

create table if not exists log_entries(
   tenant text,
   cloudlet text,
   created timeuuid,
   type text,
   content text,
   exception text,
   primary key((tenant, cloudlet), created)) with clustering order by (created desc);

alter table log_entries with default_time_to_live = 604800;
```

**Notice** - The above setting for TTL implies log items will be automatically deleted after 7 days,
since 604,800 seconds implies 7 days. Depending upon your needs you might want to increase this setting.

## Adding existing files into keyspace

The following Hyperlambda will insert all your existing files and folders into your cluster keyspace, allowing you to
play around with an existing CQL file system implementation. Notice, you'll have to change the **[.tenant]** and
**[.cloudlet]** values to resemble the absolute root folder for your Magic backend. The values in the file below is
obviously just an example of how it might look like if you've got the files on a Mac within your _"Documents"_ folder.

```
/*
 * Inserts all dynamic files and folders into the magic CQL database.
 */
cql.connect:[generic|magic]

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

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.data.cql](https://github.com/polterguy/magic.data.common), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

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
