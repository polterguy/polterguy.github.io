---
title: "Hyperlambda endpoints and arguments"
description: "Hyperlambda endpoints and arguments - The default IHttpExecutorAsync implementation can explicitly declare what arguments the file can legally accept, and if an argument is given during invocation that the file doesn'..."
generated: true
---

This page is part of the [magic.endpoint](/plugins/magic.endpoint/) documentation.

The default `IHttpExecutorAsync` implementation can explicitly declare what arguments the file can
legally accept, and if an argument is given during invocation that the file doesn't allow for, an
exception will be thrown and the file will never be executed. This allows you to declare what
arguments your Hyperlambda file can accept, and avoid having anything _but_ arguments explicitly
declared in your Hyperlambda file from being sent into your endpoint during invocation of your
HTTP endpoint. An example Hyperlambda file taking two arguments can be found below.

```
.arguments
   arg1:string
   arg2:int

strings.concat
   get-value:x:@.arguments/*/arg1
   .:" - "
   get-value:x:@.arguments/*/arg2

unwrap:x:+/*
return
   result:x:@strings.concat
```

If you save this file on disc as `/files/modules/tutorials/foo2.get.hl`, you can invoke it as follows
using the HTTP GET verb - Assuming your backend is running on localhost at port 5000.

```
http://localhost:5000/magic/modules/tutorials/foo2?arg1=howdy&arg2=5
```

JSON payloads and form URL encoded payloads are automatically converted to lambda/nodes -
And query parameters are treated indiscriminately the same way as JSON payloads -
Except of course, query parameters cannot pass in complex graph objects, but only
simply key/value arguments. Only POST, PUT and PATCH endpoints can handle payloads. If you
supply a payload to a GET or DELETE endpoint, an exception will be thrown, and an error
returned to the caller.

To allow for _any_ arguments to your files, simply _omit_ the **[.arguments]** node
in your Hyperlambda althogether, or supply an **[.arguments]** node and set its value to `*`.
Alternatively, you can also _partially_ ignore arguments sanity checking of individual nodes,
by setting their values to `*`, such as the following illustrates.

```
.arguments
   arg1:string
   arg2:date
   arg3:*
```

In the above arguments declaration, **[arg1]** and **[arg2]** will be sanity checked, and input converted
to `string` or `date` (DateTime) - But the **[arg3]** parts will be completely ignored, allowing the caller
to invoke it with _anything_ as `arg3` during invocation - Including complete graph JSON objects, assuming
the above declaration is for a `PUT`, `POST` or `PATCH` Hyperlambda file.

The '\*' value for an argument also turn
off all conversion, implying everything will be given to your lambda object with the JSON type the argument
was passed in as.
All arguments declared are considered optional, and the file will still resolve if the argument is not given,
except of course the argument won't exist in the **[.arguments]** node. However, no argument _not_ found
in your **[.arguments]** declaration can be provided during invocations, assuming you choose to declare
an **[.arguments]** collection in your Hyperlambda endpoint file, and you don't set its value to `*`.

To declare what type your arguments can be, set the value of the argument declaration node to
the Hyperlambda type value inside of your arguments declaration, such as illustrated above.
Arguments will be converted if possible, to the type declaration in your argument's declaration.
If no conversion is possible, an exception will be thrown.
Although the sanity check will check graph objects, passed in as JSON payloads, it has its restrictions,
such as not being able to sanity check complex objects passed in as arrays, etc. If you need stronger
sanity checking of your arguments, you will have to manually check your more complex graph objects
yourself in your own Hyperlambda files.

Also realise that if the value originates from a payload, as in from a PUT, PATCH or POST JSON object
for instance, these types of objects might contain null values. If they do, no conversion will be attempted,
and internally within your endpoint's Hyperlambda code, you might therefore expect to see for instance
`long` values being in fact _null_, even though technically these are not nullable types in .Net.

---

[&larr; API URLs](/plugins/magic.endpoint/api-urls/) | [all of magic.endpoint](/plugins/magic.endpoint/) | [Accepted Content-Type values for Hyperlambda endpoints &rarr;](/plugins/magic.endpoint/accepted-content-type-values-for-hyperlambda-endpoints/)
