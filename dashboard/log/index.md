---
title: Log
description: Browse your Magic cloudlet's server log to confirm it's healthy and running optimally, and to review important events as they happen.
header:
  image: /assets/images/hero/log.webp
  og_image: /assets/images/hero/log-og.png
  image_description: The Log component
faq:
  - q: "What is the Log component?"
    a: "It lets you browse your cloudlet's log, giving you control over events that might have consequences for your system - errors, security events, task executions, and anything your own code logs."
  - q: "How do I find the cause of an error?"
    a: "When something fails in the dashboard, the error message carries a 'View log entry' link taking you straight to the log entry describing the error - highlighted, and expanded to reveal its stack trace. You can also filter the log manually and click any entry carrying an exception to expand it."
  - q: "Can my own code create log entries?"
    a: "Yes. Your Hyperlambda code can create log entries as you see fit - including structured meta data - to record important events such as deleting records, executing tasks, or registering users."
  - q: "How long are log items kept?"
    a: "On AINIRO hosted cloudlets, log entries older than 2 weeks are automatically deleted by default, to avoid exhausting your cloudlet's persistent storage."
---

The log component allows you to browse your cloudlet's log. When an important event occurs in Magic, a log entry will typically be created describing the event. Examples of such events are when users are logging in, or errors are occurring in the system for some reason.

<img src="/images/log.webp" alt="Screenshot of Magic&#x27;s integrated log component" loading="lazy" width="2400" height="1500">

You can also filter your cloudlet's log, look up specific items, to find bugs happening as your system is being used. Log items carrying an exception can be expanded by clicking them, revealing the complete stack trace of whatever went wrong - which combined with filtering makes tracking down bugs in your system much easier.

<img src="/assets/images/log-expanded.webp" alt="Screenshot of an expanded log item showing the complete stack trace of an error" loading="lazy" width="2400" height="1500"> Notice, if you created a cloudlet at [AINIRO](https://ainiro.io), by default all log entries older than 2 weeks will be automatically deleted to avoid exhausting your cloudlet's persistent storage.

## From error to log entry in one click

Most of the time you don't even have to search. When something fails anywhere in the dashboard, the error message contains a _"View log entry"_ link, taking you straight to the log entry the error created - highlighted in the list, and expanded to reveal its stack trace. This works because failed HTTP requests return a `log-id` field next to their error message, containing the id of the log entry the server wrote for the error - so your own API clients can apply the same trick, correlating any error a user reports with the exact server-side log entry describing what went wrong.

## Creating your own log items from Hyperlambda

You can create your own log entries using Hyperlambda code such as the following.

```
log.info:Something important happened
   what:Something
   importance:High
```

In the above example we are creating an _"info"_ type of log entry, and the _"Something important happened"_ will become the item's content, while the **[what]** and **[importance]** parts become meta data associated with your log entry. The invocation also returns the id of the log entry it created, allowing your own code to reference the entry later - for instance returning it to a client the way Magic's own error handling does. If you execute the above Hyperlambda using the _"Hyperlambda Playground"_ component you can see your log entry in your _"Log"_ component at the top afterwards. There are 4 types of log entries you can create by default.

* __[log.debug]__ - These are debug log entries intended for helping you debug your modules and components. These are typically not displayed in a production cloudlet since typically you would turn _off_ debug logging in production
* __[log.info]__ - These are information types of entries providing information about general things occurring in your system
* __[log.error]__ - These are errors and logs when an error occurs in your system and you should pay particular notice to these
* __[log.fatal]__ - These are fatal errors that prevent your system from working correctly, implying they might prevent your cloudlet from working

## Configuring logging

Your cloudlet has a _"log level"_ setting that decides how much it should log. This is an incrementally increasing value starting at _"debug"_ and ending at _"off"_. The latter implying logging is turned off. You can change this _"log level"_ by changing your `magic:logging:level` configuration setting. The log level declares at what _"level"_ your cloudlet will insert log entries. For instance, typically when debugging you want to set the level at _"debug"_, while in a production environment you want to increase it to (at least) _"info"_ to avoid flooding your cloudlet with debug log entries. This implies that in your debug environment you will see
all log entries, including your debug log entries - While in production Magic won't create log entries for debug log items.

## Log internals

Log items will be persisted into your magic _"log_entries"_ database table. The [magic.lambda.logging](/plugins/magic.lambda.logging/) project is what encapsulates the logging related slots in Hyperlambda.

{% include faq.html %}
