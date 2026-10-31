---
title: "How to use [system.is-os]"
description: "How to use [system.is-os] - In addition to the above slots this project also contains the following slots."
generated: true
guide: true
---

The reference page of [`system.is-os`](/reference/slots/system/system.is-os/) has its arguments, constraints and declaration.

In addition to the above slots this project also contains the following slots.

* __[system.os]__ - Returns description of your operating system
* __[system.is-os]__ - Returns true if your underlying operating system is of the specified type

The last slot above takes an argument such as _"Windows"_, _"OSX_, _"Linux"_, etc, and will return true
of the operating system you are currently running on belongs to the specified family of operating systems.
Below is example usage of both.

```
system.is-os:OSX
system.os
```
