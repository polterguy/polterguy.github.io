---
title: "Hyperlambda and cryptography"
description: "Hyperlambda and cryptography - The magic.lambda.crypto project supports several cryptographic functions, but first a bit of cryptography theory."
generated: true
---

This page is part of the [magic.lambda.crypto](/plugins/magic.lambda.crypto/) documentation.

The magic.lambda.crypto project supports several cryptographic functions, but first a bit of cryptography theory.
Public key cryptography, or what's often referred to as _"asymmetric cryptography"_ is based upon
a *key pair*. One of your keys are intended for being publicly shared, and is often referred to
as _"your public key"_. This key can do two important things.

1. Your public key can encrypt data such that *only* its private counterpart key can decrypt the data
2. Your public key can verify that a message originated from a party that has access to its private counterpart

Hence, keeping your *private* key as **private**, is of outmost importance, otherwise 3rd
parties might read messages others send to you, and also impersonate you in front of others. In addition, securely
delivering your public key to the other party, is of equal importance, to make sure they're using the *correct*
public key in their communication with you. If you can keep your private key private,
and securely deliver your public key to others, you have a 100% secure channel to use for communication,
preventing malicious individuals from both reading what others send to you, and also tampering with the
content you send to others, before the other party receives it. Hence, cryptography is about two main subjects.

1. Encrypting messages sent *to you*
2. Allowing you to provide guarantees that a message originated *from you*

Depending upon your paranoia level, you might just send your public key in an email, which is considered insecure -
Or you might need to physically meet the person whom you want to communicate with,
and give him a USB stick with your public key, which is considered full paranoia level. The latter might be important
if you fear what's often referred to as a _"man in the middle attack"_, where some malicious adversary, takes your public key,
and gives a bogus and fake public key to the other party. This results in that the man in the middle
can intercept your communication, decrypt it, and re-encrypt it with your public key, before he or she
sends it to you - In addition to that he can use a similar mechanism to impersonate your signatures,
allowing the other party to falsely believe some message originated from you, when it did indeed originate
from a malicious _"man in the middle"_.

There are several different ways to create a key pair, just have the above in mind as you start using
cryptography in your Hyperlambda applications. Most of the cryptography functions in this library is
using Bouncy Castle, which is a thoroughly tested library for doing cryptography. Bouncy Castle is
owned by a charitable organisation in Australia, so they don't need to obey by American laws, reducing
American intelligence services ability to coerce them to build backdoors and similar constructs
into their code. Bouncy Castle is also Open Source, allowing others to scrutinise their code for such
backdoors. However, with cryptography, there *are no guarantees*, only a _"general feeling and concent"_
amongst developers that it's secure.

The asymmetric parts of this project is built upon RSA for its public and private key pairs.

---

[&larr; Symmetric cryptography using AES](/plugins/magic.lambda.crypto/aes/) | [all of magic.lambda.crypto](/plugins/magic.lambda.crypto/) | [Combining RSA and AES cryptography &rarr;](/plugins/magic.lambda.crypto/combining-rsa-and-aes-cryptography/)
