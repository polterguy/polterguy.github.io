---
title: "How to use [crypto.hash]"
description: "How to use [crypto.hash] - The [crypto.hash] slot can be used to generate hash values."
generated: true
guide: true
---

The reference page of [`crypto.hash`](/reference/slots/crypto/crypto.hash/) has its arguments, constraints and declaration.

The **[crypto.hash]** slot can be used to generate hash values. When you invoke it, you can choose
between having the hash returned as raw a `byte[]`, as a _"fingerprint"_ or as its bit encoded hex
version. Below is an example of all three of these formats.

```
.data:Some data to hash

crypto.hash:x:@.data
   format:fingerprint

crypto.hash:x:@.data
   format:text

crypto.hash:x:@.data
   format:raw
```

To override the hashing algorithm used when creating hash values, apply an **[algorithm]** argument, and
set its value to the hashing algorithm you want to use. You can choose between the following hashing
algorithms as you consume the above slot.

* sha1
* md5
* sha256
* sha384
* sha512

**Notice** - sha1 and md5 is supported _only_ for legacy reasons, and _should not be used_ unless you have
a legacy system depending upon it. Sha1 and md5 are considered weak today due to the statistical probability
of that they can result in what's commonly referred to as _"hash collision"_.
This project also contains convenience overloads with the hashing algorithm being a part of the name of the
invocation, such as illustrated below.

* __[crypto.hash.sha1]__
* __[crypto.hash.md5]__
* __[crypto.hash.sha256]__
* __[crypto.hash.sha384]__
* __[crypto.hash.sha512]__

In addition you can hash a file directly, without having to load it first, by providing a **[filename]** argument
to it, such as illustrated below.

```
crypto.hash.sha256
   filename:/README.md
```

## About cryptography fingerprints

The fingerprint format resulting from a hash invocation is useful due to being much more easily read by
humans, and in such a regard better suited for being stored as a key reference into for instance a database,
and/or transmitted as a key reference over the network to other machines.

A fingerprint is actually just a cryptographic hash of your data, such as for instance your public key,
payload, etc.
