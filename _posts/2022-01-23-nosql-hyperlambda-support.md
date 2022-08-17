---
layout: post
author: thomas
title: NoSQL support in Hyperlambda
canonical_url: https://aista.com/blog/nosql-hyperlambda-support/
---

We just created [a new release of Magic](https://github.com/polterguy/magic/releases), and its main
feature is that Magic and Hyperlambda now supports NoSQL database types, such as
[Cassandra](https://cassandra.apache.org/_/index.html) and 
[ScyllaDB](https://www.scylladb.com/) through a CQL data adapter.
The way it works can probably be better illustrated with a snippet of code.

```
cql.connect:[generic|space]
   cql.select:"select * from table where column = 'foo/bar'"
```

The above assumes you've got a cql configuration section in your _"appsettings.json"_ file
resembling the following.

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

If you add the above configuration to your instance, and exchange the _"space"_ parts of the
**[cql.connect]** slot invocation above with an existing keyspace, and select something from
an actual existing table in the above select query, the above will actually return data from
a NoSQL CQL compliant database of your choice, such as Cassandra or ScyllaDB.
In addition, it is also possible to configure Magic to log towards your NoSQL database as of
version 10.0.19. Refer to the [magic.data.cql documentation](/documentation/magic.data.cql/) for
details about how to configure this. The above link also describes how to use a _"virtual file system"_
in Magic, storing files and folders in for instance ScyllaDB. The latter of course being a pre-requisite
for making Magic 100% _"stateless"_, facilitating for load balancing your Magic instances through
for instance a Kubernetes cluster and similar things.