
# CQL data adapters for Magic and Hyperlambda

This project provides Magic and Hyperlambda with CQL data adapters, allowing you to perform CRUD operations towards
for instance Cassandra or ScyllaDB. 

## Slots

The project contains the following slots.

* __[cql.connect]__ - Creates a session towards a CQL cluster
* __[cql.execute]__ - Executes some CQL statement towards an open session and returns the result to caller

The basic idea of the slots are to allow for things such as follows.

```
cql.connect:[generic|space]
   cql.select:"select * from table where column = 'foo/bar'"
```

Where the `generic` parts above is a reference to a cluster you'll have to configure in your _"appsettings.json"_,
while the `space` parts above is a keyspace within that cluster. In such a regard the slots resembles the generic
RDBMS slots in usage, except of course it opens a connection towards a NoSQL database such as Cassandra or ScyllaDB,
and returns the result of executing your SQL towards a keyspace within that cluster. To use parameters in your CQL
you can use something resembling the following.

```
cql.connect:[generic|space]
   cql.select:"select * from table where column1 = :foo and column2 = :bar"
      foo:bar
      bar:x:@.arguments/*/some-arg
```

The way arguments are resolved is that in the above example `:foo` becomes a reference to the **[foo]**
node's value, and/or expression's value.

## Configuration

The primary configuration for the project to apply for your _"appsettings.json"_ file can be found below.

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

The above configures the adapter to use `127.0.0.1` as the host for your `generic` contact point or cluster.
You can add as many cluster connection points as you want to, and reference these using their unique names.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.cql](https://github.com/polterguy/magic.lambda.common), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.cql/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.cql&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.cql)
