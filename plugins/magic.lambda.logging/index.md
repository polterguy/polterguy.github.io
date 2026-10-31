---
title: magic.lambda.logging
moved_anchors: {"how-to-use-logtimeshift": "/reference/slots/log/log.timeshift/#guide", "querying-your-log": "/plugins/magic.lambda.logging/querying-your-log/"}
---

This project contains logging wrapper slots for Magic. More specifically, this project provides the following
slots allowing you to create log entries.

* __[\[log.info\]](/reference/slots/log/log.info/)__ - Information log entries, typically smaller pieces of information
* __[\[log.debug\]](/reference/slots/log/log.debug/)__ - Debug log entries, typically additional debugging information not enabled in production
* __[\[log.error\]](/reference/slots/log/log.error/)__ - Error log entries, typically exceptions
* __[\[log.fatal\]](/reference/slots/log/log.fatal/)__ - Fatal log entries, from which the application cannot recover from

In addition to the above slots there are also slots that allows you to retrieve log items, and/or some
basic statistics from your log. These can be found below.

* __[\[log.count\]](/reference/slots/log/log.count/)__ - Counts number of log items, optionally matching the specified filter condition
* __[\[log.get\]](/reference/slots/log/log.get/)__ - Returns the log item with the specified id
* __[\[log.query\]](/reference/slots/log/log.query/)__ - Returns a list of log items according to its arguments
* __[\[log.capabilities\]](/reference/slots/log/log.capabilities/)__ - Returns the capabilities of the log implementation
* __[\[log.timeshift\]](/reference/slots/log/log.timeshift/)__ - Aggregates log entries into time buckets, one per day for the last two weeks

By default, this project will log into your `magic.log_entries` database/table, using either MySQL, PostgreSQL,
Microsoft SQL Server or SQLite. This allows you to use SQL to generate statistics on top of your logs.
An example of creating a log entry can be found below.

```
log.info:Howdy world from magic.lambda.logging
```

You can of course exchange the above **[log.info]** with **[log.error]**, **[log.debug]** or **[log.fatal]**.

All four slots return the id of the log entry they created as their value, allowing you to reference the entry later - for instance passing it to **[log.get]**, or returning it to a client such that an error can be correlated with the exact log entry describing it. If the configured log level filtered the invocation out, such that no entry was created, the returned value is null.

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


## Topics

* [Querying your log](/plugins/magic.lambda.logging/querying-your-log/) - your particular log implementation can actually do what you need for it to do, since not all implementations have the same capabilities - Implying things such as filtering log items according to conte
