---
title: "How to use [slots.create]"
description: "How to use [slots.create] - Creates a dynamic slot that can be invoked using [signal]."
generated: true
guide: true
---

This is the guide to [`slots.create`](/reference/slots/slots/slots.create/), whose reference page has its arguments, constraints and declaration.

Creates a dynamic slot that can be invoked using **[signal]**. Below is an example.

```
slots.create:foo
   return-value:int:57
```

Notice, the above slot aren't persisted in any ways, implying if your web server restarts its process, your
slot is removed. If you want to make sure your slots become a permanent part of your application, you need to
make sure you are somehow creating it during server startup, which can normally be done on a per module basis, by putting
a Hyperlambda file into your module's _"magic.startup"_ folder, which makes sure the code is executed during startup
of your web app.
