---
title: Cryptography
description: Using cryptography in Magic is as easy as clicking a button. The integrated cryptography component allows you to easily create as many cryptography key pairs as you wish, and/or import public keys belonging to others, resulting in that you can securely communicate with anyone you wish.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-crypto.jpg"
---

# Cryptography

The cryptography component allows you to manage and administrate your server's cryptography key pair, and/or your
server's public keys. The latter which are public keys belonging to others, allowing you to securely communicate
with other Magic servers, and/or clients, using cryptography features such as cryptographic
signatures, and encrypting communication between servers. To understand this component refer
to [this document](/tutorials/crypto-lambda-http/). Below is a screenshot of the cryptography component
in Magic.

![Cryptography](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crypto-receipt.jpg)

## Your server key

Your server key is a public/private key pair associated with your server. By sharing your public key
with other Magic servers, and/or clients, you can have others sending you encrypted data, in addition
to cryptographically sign data your server sends and have others verifying your signatures to ensure the
data originated from you. Below is a screenshot of this part of the component.

![Server cryptography key](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crypto-server-key.jpg)

## Public keys

The public keys section are public cryptography keys imported into your server, and allows your server to
encrypt data to the owners of these keys, to such securely communicate with others by encrypting data sent
to the other party. It also allows you to verify cryptographic signatures originated from others, to such
ensure the data was not tampered with in any ways before reaching your server. Below is a screenshot showing
this component.

![Public cryptography keys](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crypto-public-keys.jpg)

## Cryptography receipts

These are your cryptography receipts, implying receipts for cryptographically signed payloads sent by other
parties as a part of [cryptographically secured lambda invocations](/tutorials/crypto-lambda-http/). Below
is a screenshot of this part of Magic.

![Cryptography receipts](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crypto-receipts.jpg)

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
