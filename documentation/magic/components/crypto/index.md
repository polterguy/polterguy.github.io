---
title: Cryptography
description: Using cryptography in Magic is as easy as clicking a button. The integrated cryptography component allows you to easily create as many cryptography key pairs as you wish, and/or import public keys belonging to others, resulting in that you can securely communicate with anyone you wish.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-crypto.jpg"
---

# The cryptography component

The cryptography component allows you to manage and administrate your server's cryptography key pair, and/or your
server's public keys. The latter are public keys belonging to others, allowing you to securely communicate
with other Magic servers, and/or clients, using cryptography features such as cryptographic
signatures, and encrypting communication between servers.

![Cryptography](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crypto-receipt.jpg)

## Your server's cryptography key pair

Your server's cryptography key pair is a public/private key pair associated with your server. By sharing your public key
with other Magic servers, and/or clients, you can have others sending you encrypted data, in addition
to cryptographically sign data your server sends, and have others verify your signatures to ensure the
data originated from you.

## Public cryptography key pairs

The public keys section are public cryptography keys imported into your server, and allows your server to
encrypt data to the owners of these keys, to such securely communicate with others by encrypting data sent
to the other party. It also allows you to verify cryptographic signatures originated from others, to such
ensure the data was not tampered with in any ways before reaching your server.

## Cryptography receipts

These are your cryptography receipts, implying receipts for cryptographically signed payloads sent by other
parties as a part of [cryptographically secured lambda invocations](/tutorials/crypto-lambda-http/).
