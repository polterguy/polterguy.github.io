---
title: "How to use [crypto.aes.decrypt]"
description: "How to use [crypto.aes.decrypt] - RSA is asymmetric cryptography, implying a different key is used for decrypting the data than the key that was used to encrypt the data."
generated: true
guide: true
---

The reference page of [`crypto.aes.decrypt`](/reference/slots/crypto/crypto.aes.decrypt/) has its arguments, constraints and declaration.

RSA is asymmetric cryptography, implying a different key is used for *decrypting* the data than the key that
was used to *encrypt* the data. Hyperlambda also supports *symmetric* cryptography, more specifically the AES
encryption algorithm. This algorithm requires the *same key* to decrypt some content that was used to encrypt
the data, and the key must either be 128, 192 or 256 bits long. Below is an example.

```
crypto.aes.encrypt:Howdy, this is cool
   password:Howdy World this is a passphrase that guarantees 256 bits strength

crypto.aes.decrypt:x:-
   password:Howdy World this is a passphrase that guarantees 256 bits strength
```

The length of the key argument you provide, becomes the bit strength of the encryption, ranging from
128 through 192 to 256 bits. However, even though the key you normally use for encrypting and decrypting
when using AES is supposed to be a `byte[]`, this project will automatically convert any passphrase
specified from a string to a SHA256 hash value. This allows you to use *any* passphrase you wish,
while avoiding reducing entropy, making it harder to crack the encrypted message.

Even though AES has low bit strength, it's still considered one of the strongest forms of cryptography
that exists, assuming you use it *correctly*. For the record, this library does *not* use the built in
AES library from .Net, which has several security issues, due to the way it handles padding among other
things - Neither does this library simply convert strings to `byte[]` arrays using `Encoding.UTF.GetBytes`,
which *significantly* reduces entropy, and makes your message easily cracked by a malicious agent with
some resources. Instead Magic uses Bouncy Castle, which does not have these security holes, in addition
to that it creates a SHA256 hash of passphrases used, if you provide a string, keeping as much entropy
as possible. However, if you want to decrypt it using *other* libraries, you'll have to inform the other
party of that the passphrase supplied is actually supposed to be hashed using SHA256 before supplied
as the `key` during decryption.

The library also supports using raw `byte[]` values as its **[password]** value, allowing you
to generate a random array of bytes, either 16, 24 or 32 bytes in size, and use this as your
passphrase directly - At which point the byte array will be used as is, and not hashed in any ways
before encryption/decryption occurs.

Due to AES' blistering speed and strength, it is often wise to combine asymmetric cryptography with
symmetric cryptography, which can be used by generating a random symmetric key/passphrase, then encrypt
this passphrase using asymmetric cryptography, such as for instance RSA, for then to use the passphrase
to encrypt the actual main data the caller wants to transmit. This has several advantages, such as
reducing the size of the data sent, while still providing the benefits from asymmetric cryptography,
such as securely sharing the public key, etc. Of course, sharing a symmetric key without major hassle,
and/or making adversaries also get a hold of it, is practically *very difficult* for obvious reasons,
unless you can asymmetrically encrypt the symmetric key.

If you only need a random array of 32 bytes, to use as your passphrase, in combination with for
instance RSA asymmetric cryptography - You can use the **[crypto.random]** slot as follows.

```
crypto.random
   min:32
   max:32
   raw:true

crypto.aes.encrypt:Some very, very, very secret text
   password:x:@crypto.random

crypto.aes.decrypt:x:-
   password:x:@crypto.random
```
