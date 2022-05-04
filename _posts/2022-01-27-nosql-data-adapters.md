---
layout: post
author: thomas
title: NoSQL files and logging data adapters for Hyperlambda
---

NoSQL has a couple of interesting traits. Its most important trait being of course that if applied correctly, it scales _linearly_.
With linearly we imply that having 5 billion records in your database does not reduce speed of retrieval or inserts
compared to having only 5 records in the same database. This is the reason why NoSQL database systems are often
associated with _"big data"_, because they facilitate for storing huge amounts of data empowering companies such as
Google, Twitter and Facebook.

As of lately Magic and Hyperlambda actually supports NoSQL data adapters through the Cassandra NuGet package.
We've tested it thoroughly for [ScyllaDB](https://scylladb.com), but it should work also
with [Cassandra](https://cassandra.apache.org/_/index.html) and any other database systems having native support
for the same protocols. This allows you to exchange the default log implementation, in addition to using Cassandra
or Scylla as a _"virtual file system"_. This of course scales a million times better than using the physical file
system for files and using MySQL or PostgreSQL as your log database. First of all because it allows you to have
100% _"stateless"_ Magic instances and load balance your requests through for instance a Kubernetes cluster,
having hundreds or millions of Magic instances for that matter, where all of your instance are running the same
Hyperlambda files. Secondly because inserts into a NoSQL database is an O(1) operation, implying logging will be
just as fast for your 5 billion'th record as for your 5th record.

## Configuring the NoSQL data adapters

If you want to play around with this yourself you'll have to do as follows.

1. Add NoSQL cluster configuration settings to Magic
2. Import your existing Hyperlambda files and configuration files into your Scylla or Cassandra database
3. Add NoSQL logging configuration settings
4. Add NoSQL files configuration settings
5. Restart your Magic instance

The above recipe assumes you're using _at least version 10.0.20 of Magic_. Below is the entire recipe if
you want to apply this yourself.

## Adding cluster connection settings

First add a NoSQL cluster connection setting into your _"appsettings.json"_ file with
the following _additional_ information. Notice, _keep_ all existing settings, and only _add_ the following.

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

Assuming you've got ScyllaDB running on your local development machine, the above will allow you to connect to
your Scylla cluster from Hyperlambda by using the **[cql.connect]** and **[cql.execute]** slots.

## Start ScyllaDB with Docker

If you don't have access to Scylla you can run a local instance on your development machine using Docker with the
following bash script.

```bash
sudo docker run --name scylla \
-p 9042:9042/tcp \
--volume /var/lib/scylla:/var/lib/scylla \
-d \
scylladb/scylla \
--developer-mode=1 \
--overprovisioned 1 \
--smp 2
```

You might get away with fewer open ports, depending upon your actual needs.

## Create your keyspaces

At this point you'll have to create the keyspaces for both your files and your log tables. This can be achieved using
`cqlsh` on your Scylla Docker container. To start `cqlsh` on your machine run the following bash script from a terminal.

```bash
docker exec -ti scylla bash
```

Then start `cqlsh` with the following.

```bash
cqlsh
```

At this point your terminal window should resemble the following.

![ScyllaDB CQL bash](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scylla-bash.jpg)

At this point you can execute CQL scripts in your terminal. To create the relevant keyspaces for Magic copy
and paste the following CQL into your cqlsh terminal.

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

Notice the default _"time to live"_ setting above, which implies log items will be automatically deleted after
1,209,600 seconds, which translates into 2 weeks. Change this as you see fit.

## Importing existing files from Magic into Scylla

At this point you can import your existing Hyperlambda files into your `magic_files`
keyspace. _Before you execute the following Hyperlambda however_, you'll have to change the **[.tenant]** and
the **[.cloudlet]** parts of it to fit your particular installation. If you're using the Docker images this is
done by setting these parts to the following values.

1. **[.tenant]** should be set to `magic`
2. **[.cloudlet]** should be set to `files`

If you're using the code version or something else, realize that the resolving of the above is done by using
the absolute path of your magic instance, and splitting it into tenant and cloudlet by its _last_ slash (/) occurrency.
Implying if you're running Magic at for instance _"C:/foo/bar/howdy"_ and you're using the default _"files"_ folder
for your dynamic Hyperlambda files, then your settings becomes as follows.

1. **[.tenant]** should be set to `C:/foo/bar/howdy`
1. **[.cloudlet]** should be set to `files`

When you have figured out which tenant and cloudlet values to use, you can exchange these in the following Hyperlambda,
and execute it through for instance Magic's _"Eval"_ menu item.

```
/*
 * Inserts all dynamic files and folders into the magic NoSQL database.
 */
cql.connect:[generic|magic_files]

   /*
    * The root folder where your Magic backend is running.
    * CHANGE THESE TWO VALUES!
    */
   .tenant:Users
   .cloudlet:thomashansen/Documents/projects/magic/magic/backend

   /*
    * Inserting root folder.
    */
   cql.execute:"insert into files (tenant, cloudlet, folder, filename) values (:tenant, :cloudlet, '/files/', '')"
      tenant:x:@.tenant
      cloudlet:x:@.cloudlet

   /*
    * Inserting appsettings.json and its folder.
    */
   cql.execute:"insert into files (tenant, cloudlet, folder, filename) values (:tenant, :cloudlet, '/config/', '')"
      tenant:x:@.tenant
      cloudlet:x:@.cloudlet
   config.load
   convert:x:-
      type:bytes
   cql.execute:"insert into files (tenant, cloudlet, folder, filename, content) values (:tenant, :cloudlet, '/config/', 'appsettings.json', :config)"
      tenant:x:@.tenant
      cloudlet:x:@.cloudlet
      config:x:@convert

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
```

After executing the above you are ready to switch your file system to use the virtual NoSQL based file system, which can be done by
adding the following configuration settings to your _"appsettings.json"_ file. Notice, _keep all existing settings_
and only _add_ the following parts.

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

Then to make sure you're using your NoSQL database for logging, you can add the following parts to your
_"appsettings.json"_ file.

```json
{
  "magic": {
    "logging": {
      "service": "magic.data.cql.logging.Logger"
    }
  }
}
```

At this point you can restart your Magic instance, and it will now resolve Hyperlambda files from your
Scylla or Cassandra database, in addition to also using Scylla or Cassandra as your log implementation.

If you didn't get the **[.tenant]** and **[.cloudlet]** parts correctly applied in your Hyperlambda
script above, it will be impossible to start Magic, and you'll get a whole range of errors as you try to
access your Magic instance. If you get things working though, Magic now 100% stateless, and you can create a
Kubernetes cluster with thousands of Magic instances, having everything scale linearly, ensuring Magic also
scales linearly, allowing you at least in theory _to handle millions of HTTP requests towards your backend per second_
by leveraging the load balancing features of your Kubernetes cluster to use your entire cluster as if it was one
physical server.

The file system is entirely created around _one_ table called _"files"_. This implies that also folders are
stored into the same table, and a folder is in fact just a file with an _empty_ filename. This allows us
to extremely rapidly select all files and folders beneath some specified sub folder, etc, and in fact using
the virtual file system is roughly 20% as fast as using the physical file system on my Mac AirBook with
an SSD hard drive. So things are still blistering fast, although not entirely as fast as with an SSD hard
drive. However, assuming you've got an average Hyperlambda and Magic solution, you'll barely notice
any performance loss, since 99% of your waiting time will anyways not be for your Hyperlambda files
to resolve and load, but rather waiting for IO data from your network as you access your database(s)
from your Hyperlambda files.

**Notice** - The default Magic Docker images does not allow for accessing the host network, implying
if you're using this through Magic's Docker images, you'll have to somehow bridge your Magic
backend's Docker container and your Scylla container, allowing your backend Docker container to access your
Scylla container, and/or host network. However, that's an exercize for later, unless you're able to figure
this out by yourself. This is easily achieved by searching for Docker networking and making sure you
either create your Scylla database container on the same virtual proxy network your Magic container
is created within, and/or allow your Magic container to access your host's network.

## Summing up

In this little micro tutorial we showed you how to use a virtual file system for your dynamic files, storing
your files in a Scylla database, in addition to also using Scylla as your log implementation. This of course
allows you to scale linearly, arguably into infinity, having billions of records, and millions of HTTP request
per second, if configured correctly through a Kubernetes cluster load balancing HTTP requests.

> Google, Twitter, and Facebook, move over rover, we've got a new clover in town ;)

FYI, no RDBMS system in the world is capable of scaling for millions of requests per second, so obviously there's
no way you can use MySQL, PostgreSQL, or SQL Server to leverage such scalability. We also need to implement
an alternative caching implementation to allow for out of process caching. The current implementation is just a memory based
cache - But this will be implemented later down the road. Stay tuned for more ^_^
