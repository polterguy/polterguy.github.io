
# Audit logging from Hyperlambda

Logging wrapper slots for Magic. More specifically, this project provides the following slots.

* __[log.info]__ - Information log entries, typically smaller pieces of information
* __[log.debug]__ - Debug log entries, typically additional debugging information not enabled in production
* __[log.error]__ - Error log entries, typically exceptions
* __[log.fatal]__ - Fatal log entries, from which the application cannot recover from

By default, this project will log into your `magic.log_entries` database/table, using either MySQL, PostgreSQL, or
Microsoft SQL Server. This allows you to use SQL to generate statistics on top of your logs. An example of
logging an info piece of information can be found below.

```
log.info:Howdy world from magic.lambda.logging!
```

**Notice** - You can supply content to your log item two different ways. Either as a piece of string, or if you choose
to set its value to nothing, it will concatenate all children node's values, after having evaluated it as a lambda
object. This allows you to create rich log entries, based upon evaluating the children of the log invocation.
This gives you a convenience shortcut to create log entries that have strings concatenated as their content,
without having to manually concatenate them yourself. An example of the latter can be found below.

```
.a:foo bar

log.info
   .:'A value is '
   get-value:x:@.a
```

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.logging](https://github.com/polterguy/magic.lambda.logging), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.logging/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.logging)
