---
title: "How to use [timezone.init]"
description: "How to use [timezone.init] - This slot reads the \"magic:culture:defaultTimeZone\" setting from your \"appsettings.json\" file, and makes it the default time zone used when dates are converted."
generated: true
guide: true
---

The reference page of [`timezone.init`](/reference/slots/timezone/timezone.init/) has its arguments, constraints and declaration.

This slot reads the _"magic:culture:defaultTimeZone"_ setting from your _"appsettings.json"_ file, and makes it the default time zone used when dates are converted. It takes no arguments, and Magic invokes it during startup, but you can also invoke it yourself after changing the setting.

```
timezone.init
```
