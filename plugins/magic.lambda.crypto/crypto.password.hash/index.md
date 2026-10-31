---
title: "How to use [crypto.password.hash]"
description: "How to use [crypto.password.hash] - As a general security rule of thumb, passwords should never be stored in clear text, but persisted into for instance a database as \"slowly hashed values with per record based salts\"."
generated: true
guide: true
---

The reference page of [`crypto.password.hash`](/reference/slots/crypto/crypto.password.hash/) has its arguments, constraints and declaration.

As a general security rule of thumb, passwords should never be stored in clear text, but persisted into for
instance a database as _"slowly hashed values with per record based salts"_. This prevents a whole range of
security issues, such as having adversaries creating Rainbow Dictionary attacks on your passwords. This
project contains two slots to implement this, and these are as follows.

* __[crypto.password.hash]__ - Creates a password hash
* __[crypto.password.verify]__ - Verifies a hashed password

Example usage can be found below.

```
crypto.password.hash:SomePasswordHere

crypto.password.verify:SomePasswordHere
   hash:x:@crypto.password.hash
```

The first slot invocation creates a Blowfish hash, while the second slot invocation verifies a previously
created Blowfish hash, given the password as its main argument. If you exchange the second password given
to **[crypto.password.verify]** by for instance adding one random character to it, the result will be
`false` from the second invocation.
Internally these are the slots Magic uses when it creates its JWT authentication database, and stores
passswords into your Magic database.
