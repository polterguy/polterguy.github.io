---
title: "How to use [log.debug]"
description: "How to use [log.debug] - The slots [log.debug], [log.info], [log.error], and [log.fatal] are actually logging with their last parts becoming the \"type\" of log item."
generated: true
guide: true
---

The reference page of [`log.debug`](/reference/slots/log/log.debug/) has its arguments, constraints and declaration.

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
