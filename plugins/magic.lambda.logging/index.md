---
title: magic.lambda.logging
---

This project contains logging wrapper slots for Magic. More specifically, this project provides the following
slots allowing you to create log entries.

* __[log.info]__ - Information log entries, typically smaller pieces of information
* __[log.debug]__ - Debug log entries, typically additional debugging information not enabled in production
* __[log.error]__ - Error log entries, typically exceptions
* __[log.fatal]__ - Fatal log entries, from which the application cannot recover from

In addition to the above slots there are also slots that allows you to retrieve log items, and/or some
basic statistics from your log. These can be found below.

* __[log.count]__ - Counts number of log items, optionally matching the specified filter condition
* __[log.get]__ - Returns the log item with the specified id
* __[log.query]__ - Returns a list of log items according to its arguments
* __[log.capabilities]__ - Returns the capabilities of the log implementation

By default, this project will log into your `magic.log_entries` database/table, using either MySQL, PostgreSQL,
Microsoft SQL Server or SQLite. This allows you to use SQL to generate statistics on top of your logs.
An example of creating a log entry can be found below.

```
log.info:Howdy world from magic.lambda.logging
```

You can of course exchange the above **[log.info]** with **[log.error]**, **[log.debug]** or **[log.fatal]**.

Children nodes will be assumed to be _"meta information"_ associated with the invocation, allowing you to
log data such as follows.

```
log.info:Some log entry
   username:foo
   ip:123.123.123.123
```

The above will log _"some log entry"_ for you, and associate **[username]** and **[ip]** with your log entry as meta data.
This allows you to use the same log entry for similar log types, and parametrise your log entry with meta information,
giving you aggregate capabilities on log entries having the same content, while still preserving meta information unique
to each log entry. Notice, if you don't provide a value to your log invocation, no meta data will be associated with your
log entry, but all arguments will rather be concatenated as a single string and end up in the _"content"_ parts of
your log entry after having been evaluated.

## Exception logging

The **[log.error]** and **[log.fatal]** slots give you the option of logging an exception stack trace, by parametrising
your invocation with an **[exception]** argument, which will _not_ be assumed to be meta information, but rather end up
in the _"exception"_ column as you create the log item. All other parameters will still be evaluated or used as meta
information.

## Log level configuration

The slots **[log.debug]**, **[log.info]**, **[log.error]**, and **[log.fatal]** are actually logging with their
last parts becoming the _"type"_ of log item. This is similar to how Log4Net and Log4J works, and can be turned on
and off as you see fit. The level is an increasing leverage type of value, applied in the following order.

* debug
* info
* error
* fatal

This implies that if you set the level to for instance _"error"_ no invocations to **[log.debug]** or **[log.info]**
will log anything into your log, allowing you to _"turn up and down"_ the level of logging you need as a configuration
setting through your _"appsetting.json"_ file. Below is an example configuration setting the level to _"info"_. The
default value for log level is _"debug"_. In a production environment you might want to increase this to at
least _"info"_.

```
{
  "magic": {
    "logging": {
      "level": "info"
    }
  }
}
```

The above value will for instance log everything except invocations to **[log.debug]**.

## Querying your log

**Notice** - To see the capabilities of your particular log implementation please invoke **[log.capabilities]** and verify
your particular log implementation can actually do what you need for it to do, since not all implementations have the
same capabilities - Implying things such as filtering log items according to content, and/or timeshifting log items, etc,
might not be implemented for your particular implementation.

To retrieve log items sequentially you can use **[log.query]**. This slot can optionally take a **[from]** argument
being the id of an existing log item from where to start retrieving items, and a **[max]** argument being the maximum
number of records to return. If no **[max]** argument is specified, the default value of this is 10. In addition the
invocation can be fiven a string as its value, which if given must match the content of your log items for an item
to be returned. Below is an example of usage.

```
log.query:"We successfully authenticated user 'root'"
   from:555
   max:20
```

The above will return log items starting from id 554 and down, and return only 20 records, and all returned records
will have a content value of _"We successfully authenticated user 'root'"_. To return a single log item you can use
**[log.get]**  and pass in the id of the log item you want to retrieve as its value.

**Notice** - If your particular log implementation does not support querying you _cannot_ query items
according to content as illustrated above, but rather only page items. Invoke **[log.capabilities]** to see if
your implementation supports querying before relying upon its existence.

## Project website for magic.lambda.logging

The source code for this repository can be found at [github.com/polterguy/magic.lambda.logging](https://github.com/polterguy/magic.lambda.logging), and you can provide feedback, provide bug reports, etc at the same place.

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

## Copyright and maintenance

The projects is copyright of Aista, Ltd 2021 - 2023, and professionally maintained by [AINIRO your friendly ChatGPT website chatbot vendor](https://ainiro.io).
