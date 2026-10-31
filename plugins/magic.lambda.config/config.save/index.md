---
title: "How to use [config.save]"
description: "How to use [config.save] - This slot saves the JSON you give it as your \"appsettings.json\" file."
generated: true
guide: true
---

The reference page of [`config.save`](/reference/slots/config/config.save/) has its arguments, constraints and declaration.

This slot saves the JSON you give it as your _"appsettings.json"_ file. The JSON replaces the file entirely, which is why you typically load it with **[config.load]** first, change it, and save the result. Below is an example, saving what was just loaded.

```
config.load
config.save:x:@config.load
```
