---
title: "How to use [log.error]"
description: "How to use [log.error] - The [log.error] and [log.fatal] slots give you the option of logging an exception stack trace, by parametrising your invocation with an [exception] argument, which will not be assumed to be me..."
generated: true
guide: true
---

The reference page of [`log.error`](/reference/slots/log/log.error/) has its arguments, constraints and declaration.

The **[log.error]** and **[log.fatal]** slots give you the option of logging an exception stack trace, by parametrising
your invocation with an **[exception]** argument, which will _not_ be assumed to be meta information, but rather end up
in the _"exception"_ column as you create the log item. All other parameters will still be evaluated or used as meta
information.
