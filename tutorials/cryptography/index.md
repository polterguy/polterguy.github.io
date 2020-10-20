# Hyperlambda Cryptography

Hyperlambda gives you both asymmetric and symmetric cryptography functionality. In the video below,
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
   key:x:@crypto.rsa.create-key/*/public

crypto.rsa.decrypt:x:@crypto.rsa.encrypt
   key:x:@crypto.rsa.create-key/*/private
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
password to return its real value.

In addition, a random password is often generated using a cryptographically secure random number
generator (CSRNG), for then to asymmetrically encrypt this password at the top of your
message, for then to use the random password to symmetrically encrypt the body of your message.
This reduces the size of your encrypted message, and also increase performance during encryption
and decryption, since symmetric cryptography tends to be faster than asymmetric cryptography.

Later we will have a look at some use cases, where we apply both of these ideas - But for now,
you might want to watch the following video illustrating symmetric cryptography.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/uRJdMLHHmhg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

* [Use case BabelFish](/tutorials/use-case-translation/)
