# Hyperlambda Cryptography

Hyperlambda gives you both asymmetric and symmetric cryptography functionality. This allows you to
encrypt, decrypt, and cryptographically sign messages - In addition to transmitting secrets securely
over an inheritingly insecure channel, such as the web for instance. In the video below,
I walk you through how to generate and use an RSA key pair using nothing but Magic's built in slots.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/qcGZb2e92Zo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Combining the above public key cryptography features of Magic, with its built in AES functionality,
arguably gives you the bulk of everything needed to get seriously started with strong cryptography.

## Asymmetric or Public Key Cryptography

The code snippet found below, will create an RSA key pair, then it will use the *public* key to
encrypt some data, for then to use the *private* key to decrypt it afterwards.

```
.data:Some data you want to encrypt

crypto.rsa.create-key
   strength:2048

crypto.rsa.encrypt:x:@.data
   public-key:x:@crypto.rsa.create-key/*/public

crypto.rsa.decrypt:x:@crypto.rsa.encrypt
   private-key:x:@crypto.rsa.create-key/*/private
```

This allows you to generate a key pair, for then to distribute your *public* key, to anyone
wanting to send you encrypted data - Ensuring nobody but *you* can decrypt the data. The key
**[strength]** argument above, can be set to anything. In a real world scenario you probably
want to use at least 4096 bits key strength.

By default, all crypto slots in Magic, will return base64 encoded data, but you can also pass in
a **[raw]** argument to all of the above slots, at which point they will return the raw `byte[]`
buffer of whatever they produced as result. For the key pair itself, this implies returning the
DER encoded `byte[]` value of your key pair.

## Symmetric Cryptography

In addition to the above asymmetric features, Magic also provides symmetric crypto slots.
Below is an example of using AES to encrypt some data.

```
crypto.aes.encrypt:Some super secret data
   password:Your password
crypto.aes.decrypt:x:-
   password:Your password
```

AES is often referred to as *symmetric* cryptography because the same key you use to *encrypt*
your message, is also used to *decrypt* it. Hence, there is *symmetry* in encryption and decryption.
In practice though, symmetric cryptography and asymmetric cryptography is often used in
combination. Usually your private key is often symmetrically encrypted, such that adversaries
getting access to your private key, still cannot retrieve it, since they'll need some sort of
password to return its real value. In addition, in real world examples, a random AES session key
is often asymmetrically encrypted for some recipient's private key, using his public key - For
then to symmetrically encrypt the bulk of the message using AES.

This reduces the size of your encrypted message, and also increase performance during encryption
and decryption, since symmetric cryptography tends to be faster than asymmetric cryptography.
Before we look at combination examples, you might want to have a look at the following video
where I illustrate AES cryptography using Magic.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/uRJdMLHHmhg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## AES + RSA == really cool

In isolation though, both RSA and AES are nifty things, but not really that useful. Only
when combining RSA and AES, we end up with some real world practical use cases for cryptography. Magic of course
contains several _"combination helper slots"_ that helps you out here, reducing the creation of encrypted
and cryptographically signed messages down to a single signal invocation. Below is a piece of Hyperlambda
that combines AES and RSA to encrypt a message intended to be sent over an insecure connection to
some recipient whom you have access to the public key for. For simplicity reasons, we create a key pair
as an integral part of the snippet, but these would normally be things you already have access to, in for
instance some database table, or file, etc.

```
// Recipient's key.
crypto.rsa.create-key
   strength:512

// Sender's key.
crypto.rsa.create-key
   strength:512

// Encrypting some message.
crypto.encrypt:Some super secret message
   encryption-key:x:././*/crypto.rsa.create-key/[0,1]/*/public
   signing-key:x:././*/crypto.rsa.create-key/[1,2]/*/private
   signing-key-fingerprint:x:././*/crypto.rsa.create-key/[1,2]/*/fingerprint

// Decrypting the above encrypted message.
crypto.decrypt:x:-
   decryption-key:x:././*/crypto.rsa.create-key/[0,1]/*/private
   
// Uncomment this line to retrieve signing key's fingerprint
// that you can use to lookup the public key needed to verify the signature
// crypto.get-key:x:-

// Verifying signature of encrypted message.
crypto.verify:x:@crypto.decrypt
   public-key:x:././*/crypto.rsa.create-key/[1,2]/*/public
```

Normally, just before the last invocation to **[crypto.verify]**, you
would invoke **[crypto.get-key]** on the result of the decryption, and use
the fingerprint returned from this invocation to lookup a public key needed
to verify the signature of the message.

You can find many more examples of combining AES with RSA
in [the documentation](/documentation/magic.lambda.crypto/) for the magic.lambda.crypto library, in addition
to information about how the above helper slots is implemented, and their cryptography format, etc.

* [Use case BabelFish](/tutorials/use-case-translation/)
