---
title: Log
description: Documentation for your Magic log component, allowing you to verify your cloudlet is healthy and running optimally.
og_image: "/images/log.jpg"
header:
  image: /assets/images/wizard-writing-secret-spells-into-his-spell-book.webp
---

The log component allows you to browse your server's log. When an important event occurs in Magic, a log entry will typically be created describing the event. Examples of such events are when users are logging in, or errors are occuring in the system for some reasons.

![Screenshot of Magic's integrated log component](/images/log.jpg)

You can also filter your server's log, look up specific items, to find bugs happening as your system is being used. Notice, if you created a cloudlet at [AINIRO](https://ainiro.io), by default all log entries older than 2 weeks will be automatically deleted to avoid exhausting your cloudlet's persistent storage.

## Creating your own log items from Hyperlambda

You can create your own log entries using Hyperlambda code such as the following.

```
log.info:Something important happened
   what:Something
   importance:High
```

In the above example we are creating an _"info"_ type of log entry, and the _"Something important happened"_ will become the item's content, while the **[what]** and **[importance]** parts becomes meta data associated with your log entry. If you execute the above Hyperlambda using the _"Hyperlambda Playground"_ component you can see your log entry in your _"Log"_ component at the top afterwards. There are 4 types of log entries you can create by default.

* __[log.debug]__ - These are debug log entries intended for helping you debug your modules and components. These are typically not displayed in a production cloudlet since typically you would turn _off_ debug logging in production
* __[log.info]__ - These are information types of entries providing information about general things occurring in your system
* __[log.error]__ - These are errors and logs when an error occurs in your system and you should pay particular notice to these
* __[log.fatal]__ - These are fatal errors that prevents your system from working correctly and are fatal, implying they might prevent your cloudlet from working

## Configuring logging

Your server has a _"log level"_ setting that decides how much it should log. This is an incrementally increasing value starting at _"debug"_ and ending at _"off"_. The latter implying logging is turned off. You can change this _"log level"_ by changing your `magic:logging:level` configuration setting. The log level declares at what _"level"_ your server will insert log entries. For instance, typically when debugging you want to set the level at _"debug"_, while in a production environment you want to increase it to (at least) _"info"_ to avoid flooding your server with debug log entries. This implies that in your debug environment you will see
all log entries, including your debug log entries - While in production Magic won't create log entries for debug log items.

## Log internals

Log items will be persisted into your magic _"log_entries"_ database table. The [magic.lambda.logging](/plugins/magic.lambda.logging/) project is what encapsulates the logging related slots in Hyperlambda.
