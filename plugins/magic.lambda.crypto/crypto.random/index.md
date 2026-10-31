---
title: "How to use [crypto.random]"
description: "How to use [crypto.random] - This slot create a bunch of random characters, or bytes for you."
generated: true
guide: true
---

This is the guide to [`crypto.random`](/reference/slots/crypto/crypto.random/), whose reference page has its arguments, constraints and declaration.

This slot create a bunch of random characters, or bytes for you.
The slot can optionally take a **[min]** and **[max]** argument, which defines the min/max length of the
random bytes/characters returned. If not supplied, the default values for these arguments are respectively 10 and 20.
This slot is useful for creating random secrets, and similar types of random strings, where you need cryptographically
secured random strings or byte arrays. An example of generating a cryptographically secure random string of text
between 50 and 100 characters in length can be found below.

```
crypto.random
   min:50
   max:100
```

Notice, the **[crypto.random]** slot will _only_ return characters from a-z, A-Z and 0-9. Which makes
it easily traversed using any string library. However, you can provide a **[raw]** argument, and set its
value to boolean true, at which point the slot will return the raw bytes as a `byte[]`. This has a much
larger amount of entropy than simply using alphanumeric characters for the same size - Which is
important as you start creating keys for AES cryptography operations etc.
