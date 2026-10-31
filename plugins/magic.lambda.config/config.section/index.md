---
title: "How to use [config.section]"
description: "How to use [config.section] - This slot reads one section of your \"appsettings.json\" file, and returns each of its keys as a child node holding the value."
generated: true
guide: true
---

The reference page of [`config.section`](/reference/slots/config/config.section/) has its arguments, constraints and declaration.

This slot reads one section of your _"appsettings.json"_ file, and returns each of its keys as a child node holding the value. A key that is a section of its own has no value, so you read it by asking for it with the section names separated by `:`, such as in the example below.

```
config.section:magic:culture
```
