---
title: Log
description: Browse your Magic cloudlet's server log to confirm it's healthy and running optimally, and to review important events as they happen.
header:
  image: /assets/images/hero/log.png
  og_image: /assets/images/hero/log-og.png
  image_description: The Log component
faq:
  - q: "What is the Log component?"
    a: "It lets you browse your server's log, giving you control over events that might have consequences for your system - errors, security events, task executions, and anything your own code logs."
  - q: "Can my own code create log entries?"
    a: "Yes. Your Hyperlambda code can create log entries as you see fit, to record important events such as deleting records, executing tasks, or registering users."
---

The log component allows you to browse your server's log. When an important event occurs in Magic, a log entry will typically be created describing the event. Examples of such events are when users are logging in, or errors are occurring in the system for some reason.

![Screenshot of Magic's integrated log component](/images/log.jpg)

You can also filter your server's log, look up specific items, to find bugs happening as your system is being used. Log items carrying an exception can be expanded by clicking them, revealing the complete stack trace of whatever went wrong - which combined with filtering makes tracking down bugs in your system much easier.

![Screenshot of an expanded log item showing the complete stack trace of an error](/assets/images/log-expanded.jpeg) Notice, if you created a cloudlet at [AINIRO](https://ainiro.io), by default all log entries older than 2 weeks will be automatically deleted to avoid exhausting your cloudlet's persistent storage.

## Creating your own log items from Hyperlambda

You can create your own log entries using Hyperlambda code such as the following.

```
log.info:Something important happened
   what:Something
   importance:High
```

In the above example we are creating an _"info"_ type of log entry, and the _"Something important happened"_ will become the item's content, while the **[what]** and **[importance]** parts become meta data associated with your log entry. If you execute the above Hyperlambda using the _"Hyperlambda Playground"_ component you can see your log entry in your _"Log"_ component at the top afterwards. There are 4 types of log entries you can create by default.

* __[log.debug]__ - These are debug log entries intended for helping you debug your modules and components. These are typically not displayed in a production cloudlet since typically you would turn _off_ debug logging in production
* __[log.info]__ - These are information types of entries providing information about general things occurring in your system
* __[log.error]__ - These are errors and logs when an error occurs in your system and you should pay particular notice to these
* __[log.fatal]__ - These are fatal errors that prevent your system from working correctly, implying they might prevent your cloudlet from working

## Configuring logging

Your server has a _"log level"_ setting that decides how much it should log. This is an incrementally increasing value starting at _"debug"_ and ending at _"off"_. The latter implying logging is turned off. You can change this _"log level"_ by changing your `magic:logging:level` configuration setting. The log level declares at what _"level"_ your server will insert log entries. For instance, typically when debugging you want to set the level at _"debug"_, while in a production environment you want to increase it to (at least) _"info"_ to avoid flooding your server with debug log entries. This implies that in your debug environment you will see
all log entries, including your debug log entries - While in production Magic won't create log entries for debug log items.

## Log internals

Log items will be persisted into your magic _"log_entries"_ database table. The [magic.lambda.logging](/plugins/magic.lambda.logging/) project is what encapsulates the logging related slots in Hyperlambda.

{% include faq.html %}
