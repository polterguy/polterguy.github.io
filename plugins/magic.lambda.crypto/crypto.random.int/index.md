---
title: "How to use [crypto.random.int]"
description: "How to use [crypto.random.int] - This slot create a random integer value for you using a CSRNG generator."
generated: true
guide: true
---

The reference page of [`crypto.random.int`](/reference/slots/crypto/crypto.random.int/) has its arguments, constraints and declaration.

This slot create a random integer value for you using a CSRNG generator.
The slot can optionally take a **[max]** argument, which defines the maximum value it will return.
This slot is useful for creating random integers where you need cryptographically
secured random values. An example of generating a cryptographically secure random string integer
with a maximum value of 1024 can be found below.

```
crypto.random.int
   max:1024
```
