---
title: "How to use [data.read]"
description: "How to use [data.read] - A [vocabulary] entry can optionally declare a value, which pins the slot to that exact argument."
generated: true
guide: true
---

The reference page of [`data.read`](/reference/slots/data/data.read/) has its arguments, constraints and declaration.

A **[vocabulary]** entry can optionally declare a _value_, which pins the slot to that exact argument.
An entry without a value allows the slot with any argument, exactly as above, while an entry with a
value only allows the slot when its argument matches.

```
.result
whitelist

   vocabulary
      data.connect:chinook
      data.read
      return-nodes

   .lambda

      // Legal, since the vocabulary pins [data.connect] to exactly this database.
      data.connect:chinook
         data.read
            table:Artist
            limit:5
         return-nodes:x:@data.read/*
```

With the above vocabulary, `data.connect:northwind` throws, because the argument does not match the
pin. Repeat the same slot name with different values to allow more than one argument. This is how you
confine a piece of untrusted Hyperlambda to one specific database, one specific URL, or one specific
dynamic slot, instead of merely to the _name_ of a slot.

Notice, dynamic slots are pinned the same way, through the slot that invokes them.

```
vocabulary
   signal:accounting.report
   signal:hr.hire
```

The above allows the caller to invoke those two dynamic slots, and no others.

Files are pinned the same way, through **[execute-file]** and **[io.file.execute]**, which lets you admit
a specific Hyperlambda file instead of the slots it uses.

```
vocabulary
   execute-file:/modules/reports/top-customers.hl
   io.file.execute:/modules/reports/top-customers.hl
   io.file.load:/modules/reports/top-customers.hl
```

The statements inside an admitted file, or inside an admitted dynamic slot, are not restricted by the
whitelist, so the file can invoke slots that the caller itself cannot. This lets you expose complex business
logic to untrusted code without exposing the raw resources it works on, as long as you trust the file, and the
file validates the arguments it is given. The **[io.file.load]** line is optional, and allows the caller to
read the file's source. Read more in the
[Sandbox API generator](/dashboard/endpoint-generator/#business-logic-without-raw-access).
