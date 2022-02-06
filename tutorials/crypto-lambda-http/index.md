---
title: Cryptographically secured HTTP lambda invocations
description: In this article we show you how to cryptographically sign your Hyperlambda for then to transmit it to another server, having that server securely execute your Hyperlambda, without compromising security in the process.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-crypto.jpg"
---

# Cryptographically secured HTTP lambda invocations

This tutorial covers the following parts of Magic and Hyperlambda.

* How to create cryptographically signed HTTP invocations
* How lambda invocations are stored giving the server a receipt of invocation
* How Magic avoids replay attacks on lambda invocations
* Tips and tricks for how to apply these constructs in your own Micro Service architecture

This is one of those oddball things you've probably never seen before, arguably turning your Magic
server into a crypto wallet and a financial transaction server, by allowing you to securely
execute Hyperlambda code created by a 3rd party client - And have receipts giving you a guarantee
of that the executed code was in fact created by _one specific client_. In many ways, it could be
argued that this creates a _"blockchain"_ type of technology for generic HTTP lambda invocations,
providing code to your server, that you can securely execute, while getting a cryptographic
receipt of that the code that was executed was indeed created by a _specific client_.

## The internals of the process

If we start out imagining a client creating a Hyperlambda invocation to another server the process
becomes as follows.

1. The client's Hyperlambda payload is cryptographically signed with his private key
2. The payload is transmitted to the server
3. The server verifies that the cryptographic signature is valid
4. The server verifies no payloads with the same **[.request-id]** has been successfully executed before
4. The server looks up the execution rights associated with the public key
5. The Hyperlambda in the payload is executed, _only_ allowing for the slots that are _"whitelisted"_ to be executed
6. A receipt containing the cryptographically signed payload is persisted on the server
7. The server cryptographically signs the response and returns it to the client
8. The client verifies the cryptographic signature in the response returned by the server

If any of the above steps are failing for any reasons, the execution is not considered to be successful.
Fail conditions might include for instance.

* The payload has been tampered with after having been cryptographically signed
* The public key the payload was signed with does not exist on the server
* The public key the payload was signed with is _disabled_ on the server
* The payload tries to invoke a slot it is not allowed to invoke according to its _"whitelist"_
* A payload with the same **[.request-id]** has been successfully executed previously on the server
* The server's response is not signed with the key the client has associated with the domain it sent the request to

This allows you to exchange public keys with another Magic server, and/or your own Magic installations, associate
an authorisation object with the other party's public key, for then to have the owner of that key create
Hyperlambda code that your server _securely executes_ - Arguably _"reversing the responsibility of code"_, where
the server is no longer responsible for declaring its code, but rather the client provides a lambda object
that your server executes. We refer to this as IoC on code declaration, because it becomes the equivalent
of _"inversion of control"_ in regards to who gets to decide what code to execute. The core of this feature
is a dynamic slot called **[magic.crypto.http.eval]**. This slot requires two arguments; A **[url]** argument,
and a **[.lambda]** argument, that will be serialised as Hyperlambda and transmitted to the specified URL, and
executed on the server. In addition, there exists a PATCH HTTP endpoint with the relative URL
of `magic/system/crypto/eval-id` that is responsible for executing the specified Hyperlambda on the server
side.

## Code example

Use the _"Eval"_ menu item from your Magic Dashboard and execute the following code.

```
guid.new
unwrap:x:+/**/.request-id

signal:magic.crypto.http.eval

   url:"http://localhost:4444/magic/system/crypto/eval-id"
   .lambda

      .request-id:x:@guid.new
      vocabulary
      slots.vocabulary
      add:x:./*/return
         get-nodes:x:@vocabulary/*
         get-nodes:x:@slots.vocabulary/*
      return
```

**Notice** - You might have to change the port number in the above snippet depending upon whether or not you're
running Magic through its Docker images or not.
If you open your _"Crypto"_ menu item afterwards, and you expand the _"Receipts"_ tab, you will see
something resembling the following.

![Cryptography receipt](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crypto-receipt.jpg)

The ID above is the value returned from **[guid.new]**, and simply a randomly generated id associated
with your request, created by the client - Allowing the client to persist the invocation.
More importantly though, from the server's perspective, this becomes the equivalent of
a _"transaction identifier"_. Since the id is also a part of the payload itself, and hence a part of the
message the cryptographic signature was generated from, this prevents _"replay attacks"_, where an adversary
can pick up your payload, and replay the same payload again. This is accomplished by checking if the
**[.request-id]** part of the payload has been previously executed, and if so aborting the execution,
returning an error to the client. To see this in action try to execute the following Hyperlambda _twice_,
and notice how the first invocation typically succeeds, while the second invocation fails.

```
signal:magic.crypto.http.eval
   url:"http://localhost:4444/magic/system/crypto/eval-id"
   .lambda

      .request-id:not-a-unique-request-id
      return:Will fail the second time
```

You might have to change the port number in the above snippet depending upon whether or not you're
running Magic through its Docker images or not.

## Importing public keys

Magic allows for anyone to import their public keys into your key database by simply visiting your dashboard
and clicking the _"Crypto"_ menu items. Importing a public key does not require a user to be authenticated,
allowing any random bypasser to import his or her key, but the key will not be enabled before explicitly
enabled by a root user on the server where the key was imported. Importing a public key typically looks like
the following.

![Importing a public cryptography key](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/import-public-key.jpg)

However, after the key is imported it is by default _not_ enabled, implying the user still cannot use
it to execute arbitrary Hyperlambda on your server. A root user still needs to explicitly _enable_ the key
through the _"Crypto"_ menu item by clicking the _"Enabled"_ checkbox for the specified key as illustrated
below.

![Enabling a public cryptography key](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/enable-public-key.jpg)

When the key is enabled, the owner of the private key associated with the public key can execute any slot
listed in the above CodeMirror Hyperlambda editor, and the owner of the server can add as many or as few
slots here as he or she wants to. Which slots a server administrator allows for will probably vary according
to his or her trust level on an individual per key based level, but at the very least common courtesy dictates
that the slots **[add]**, **[get-nodes]**, **[return-nodes]**, **[vocabulary]** and **[slots.vocabulary]** are
enabled, since this allows the owner of the public key to invoke the server's cryptography endpoint and ask
it what types of slots it is allowed to pass into the endpoint by constructing some Hyperlambda resembling
the first Hyperlambda snippet at the beginning of this document.

**Warning** - Be careful with what slots you allow others to execute on your server. If you for instance allow
for deleting files on your server, some malicious key owner might delete all files on your system - And it might
not even be the owner of that server's fault either, but rather because his server has been hacked by some other
malicious adversary, resulting in that the other party's server starts doing things the owner of that server
wouldn't do in the first place himself.

## Endpoint internals

The endpoint `magic/system/crypto/eval-id` is encapsulated in the file called _"eval-id.patch.hl"_ that can
be found within your _"/system/crypto/"_ folder. The most important tasks this endpoint has are as follows.

* Verify that payload is cryptographically signed with a private key matching a public key that is enabled and imported into the backend
* Ensure the Hyperlambda is executed within a **[whitelist]** invocation matching the slots whitelisted on the public key

The last part above is what prohibits the Hyperlambda from executing slots it is not allowed to execute, since
it temporarily changes the behaviour of the **[eval]** slot, such that only slots found inside of its **[vocabulary]**
argument are legally allowed to be signaled. However, there is one part of this equation you need to be
careful with, which is that when a dynamic slot is signaled, the **[whitelist]** is turned _off_. Without
this feature every slot a dynamic slot is internally using would have to be whitelisted in order to be able
to invoke the dynamic slot, which of course would defeat the purpose, and render the functionality useless.

This implies that if a dynamic slot is executing a lambda object specified by the caller, the **[whitelist]**
restrictions can be completely bypassed, resulting in a malicious adversary being able to execute slots he or she
should _not_ have access to execute. Hence, as a general rule of thumb, you
should _never whitelist dynamic slots that are executing lambda objects specified by the caller_. Let's repeat
that once more to make sure it sticks.

> NEVER, EVER, EVER whitelist dynamic slots that are executing lambda objects specified by the caller

Internally the endpoints, and the associated slot, are using the cryptography slots
from [magic.lambda.crypto](/documentation/magic.lambda.crypto/) - Feel free to study this project to gain further
understanding about cryptography in Magic and Hyperlambda. Also notice that the Hyperlambda payload is _not_ encrypted.
This is anyways typically redundant, since for cryptography in HTTP invocations you'd typically want to
resort to and trust TLS or Transport Layer Security, and encrypting the payload only adds overhead
for the client and server during communication. The point here is anyways not to encrypt data, but rather
to ensure data originates from a specific client, similarly to how crypto currency transactions are
cryptographically signed, ensuring nobody but some wallet owner is allowed to transfer money from his wallet
to some other wallet of his chosing.

The **[.request-id]** argument supplied as you create an HTTP invocation can be any string. However, it has
to be globally unique, implying using a Guid or a piece of text, plus some Guid, or your company name, etc,
as the request id is probably smart to avoid having your IDs clash with other clients' IDs.

## Micro services and super scalable distributed systems

In addition to the obvious use cases, such as financial transactions, document signing, legal things, etc -
This also allows you to create a micro service environment, publicly exposing endpoints over an
insecure connection, such as the World Wide Web - While still providing guarantees of that nobody except
those clients explicitly given permissions on your server are legally allowed to provide Hyperlambda
code to your server and have your server execute their code.

Since the whole idea also is that _the client supplies the code_, this also allows your
system to go through evolutionary iterations, changing its behaviour, _without_ having to patch or
change your servers in any ways, since the client is the party providing the actual code to be executed.
Hence, upgrading your client, effectively changes the behaviour of your server. Needless to say, but in
a Micro Service environment where you might have dozens, and sometimes thousands of heterogeneous server
instances, this approach eliminates an entire axiom in regards to maintaining your system(s) - Simplifying
things significantly, since you no longer need to patch your servers, but only your clients.

## Warning! Don't go berserk

This feature is incredibly powerful, but it also carries some overhead. For
instance, the payloads needs to be cryptographically signed by the client. The server needs to verify
the signature and parse the Hyperlambda, building a lambda object from it. Execution rights needs to
be retrieved from the database, and a receipt for the execution of the lambda object needs to be persisted
into the database. Hence, you should not use this feature for things where execution speed is crucial,
but rather smaller payloads, occasionally transmitted between clients and servers, and not for things
needing to handle thousands of requests per second.
However, when you need such features, you _really_ need it - And if used correctly, and _sparsely_,
this feature is an incredibly useful tool, to both scale out (**securely**), and more easily build
heterogeneous server environments, without having to try to predict what the future might hold in
regards to its requirements.

* Continue with [Customised authentication](/tutorials/auth-internals/)
