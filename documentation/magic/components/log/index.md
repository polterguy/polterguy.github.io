---
title: Your Magic and Hyperlambda log component
description: This article shows you how you can utilise Magic's log in your own Hyperlambda code, easily allowing you to monitor how your Magic backend is doing and catching errors and security issues.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-getting-started.jpg"
---


# Your Magic and Hyperlambda log component

The log component allows you to see your server's log. When an important event occurs in
Magic, a log entry will typically be created describing the event. Examples of such events
are when users are logging in, or an error occurs in the system for some reasons. Below you can
see a screenshot of how the log component looks like.

![Magic log](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/log.jpg)

You can also create your own log entries in your own Hyperlambda by using code resembling the following.

```
log.info:Something important happened
   what:Something
   importance:High
```

In the above example we are creating an _"info"_ type of log entry, and the _"Something important happened"_
will become the item's sub-type, while the **[what]** and **[importance]** parts becomes meta data associated
with your log entry. If you execute the above Hyperlambda using your dashboard's _"Eval"_ component you can
see your log entry in your _"Log"_ component at the top afterwards. There exists 4 types of log entries you
can create by default.

* __[log.debug]__ - These are debug log entries intended for helping you debug your modules and components
* __[log.info]__ - These are information types of entries providing information about important things occurring in your system
* __[log.error]__ - These are errors and logs when an error occurs in your system
* __[log.fatal]__ - These are fatal errors that prevents your system from working correctly

Your server has a _"log level"_ setting that decides how much it should log. This is an incrementally
increasing value starting at _"debug"_ and ending at _"off"_. The latter implying logging is turned off.
You can change this _"log level"_ by changing your `magic:logging:level` configuration setting. The log level
declares at what _"level"_ your server will insert log entries. For instance, typically when debugging you want
to set the level at _"debug"_, while in a production environment you want to increase it to (at least) _"info"_
to avoid flooding your server with debug log entries. This implies that in your debug environment you will see
all log entries, including your debug log entries - While in production Magic won't create log entries for
debug log items.


* [Read more about logging from Hyperlambda](/documentation/magic.lambda.logging/)
* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
