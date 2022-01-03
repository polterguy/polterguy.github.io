
# Cryptographically secured HTTP lambda invocations

This is one of those oddball things you have probably never seen before, arguably turning your Magic
server into a crypto wallet and a financial transaction server, by allowing you to securely
execute Hyperlambda code created by a 3rd party client - And have receipts giving you a guarantee
of that the executed code was in fact created by _one specific client_. In many ways, it could be
argued that this creates a _"blockchain"_ type of technology for generic HTTP lambda invocations,
providing code to your server, that you can securely execute, while getting a cryptographic
receipt of that the code that was executed was indeed created by _a specific client_. Watch
the video below for a walkthrough of how this actually works.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/U5SwKS-S2RI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## The internals of the process

If we start out imagining a client creating an invocation the process becomes as follows.

1. The client's payload is cryptographically signed with his private key
2. The payload is transmitted to the server
3. The server verifies that the cryptography signature is valid
4. The server verifies a payload with the same **[.request-id]** has not been successfully executed previously
4. The server looks up the execution rights associated with the public key
5. The Hyperlambda in the payload is executed, _only_ allowing for the slots that are _"whitelisted"_ to be executed
6. A receipt containing the cryptographically signed payload is persisted on the server
7. The server cryptographcally signs the response and returns it to the client
8. The client verifies the cryptography signature in the response returned by the server

If any of the above steps are failing for some reasons, the execution is not considered to be successful.
Fail conditions might include for instance.

* The payload has been tampered with after having been cryptographically signed
* The public key the payload was signed with does not exist on the server
* The public key the payload was signed with is _disabled_ on the server
* The payload tries to invoke a slot it is not allowed to invoke according to its _"whitelist"_
* A payload with the same **[.request-id]** has been successfully executed previously on the server
* The server's response is not signed with the key the client has associated with the domain it sent the request to

This allows you to exchange public keys between another Magic server and your own Magic installation, associate
an authorisation object with the other party's public key, for then to have the owner of that key create
Hyperlambda code that your server _securely executes_ - Arguably _"reversing the responsibility of code"_, where
the server is no longer responsible for declaring its code, but rather the client provides a lambda object
that your server executes. We refer to this is IoC on code declaration, because it becomes the equivalent
of _"inversion of control"_ in regards to who gets to decide what code to execute.

## Code example

Use the _"Evaluator"_ menu item from your Magic Dashboard and execute the following code.

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

If you open your _"Crypto"_ menu item afterwards, and you expand the _"Receipts"_ tab, you will see
something resembling the following.

![Cryptographic receipt of HTTP Lambda Invocation](https://servergardens.files.wordpress.com/2021/04/crypto-receipt.png)

The *ID* above is the value returned from **[guid.new]**, and simply a randomly generated ID associated
with your request, created by the client - Allowing the client to persist the invocation any ways he wants
to on his side - But of course more importantly from the server's perspective becoming the equivalent of
a _"transaction identifier"_. Since the ID is also a part of the payload itself, and hence a part of the
message the cryptographic signature was generated from, this prevents _"replay attacks"_, where an adversary
can pick up your payload, and replay the same payload again. This is accomplished by checking if the
**[.request-id]** parts of the payload has been previously executed, and if so, aborting the execution,
returning an error to the client. To see this in action try to execute the following Hyperlambda _twice_,
and notice how the first invocation typically succeeds, while the second invocation fails.

```
signal:magic.crypto.http.eval
   url:"http://localhost:4444/magic/system/crypto/eval-id"
   .lambda
      .request-id:not-a-unique-request-id
      return:Will fail the second time
```

## Micro services and super scalable distributed systems

In addition to the obvious use cases, such as financial transactions, document signing, legal things, etc -
This also allows you to create a micro service environment, publicly exposing endpoints over an
insecure connection, such as the World Wide Web - While still providing guarantees of that nobody except
those clients explicitly given permissions on your server are legally allowed to invoke your endpoints.

Since the whole idea also is that _the client supplies the code_, this also allows your
system to go through evolutionary iterations, changing its behaviour, _without_ having to patch or
change your servers in any ways, since the client is the party providing the actual code to be executed.
Hence, upgrading your client, effectively changes the behaviour of your server. Needless to say, but in
a Micro Service environment where you might have dozens, and sometimes thousands of heterogeneous server
instances, this approach eliminates an entire axiom in regards to maintaining your system(s) - Simplifying
things significantly, since you no longer need to patch your servers, but only your clients.

## Warning! Don't go berserk

Yes, I know, once you _get it_, these guys are incredible - But they also carry some overhead. For
instance, the payloads needs to be cryptographically signed by the client. The server needs to verify
the signature and parse the Hyperlambda, building a lambda object from it. Execution rights needs to
be retrieved from the database, and a receipt for the execution of the lambda object needs to be persisted
into the database. Hence, you should _not_ use these guys for things where execution speed is crucial,
but rather smaller payloads, occasionally transmitted between clients and servers, and not for things
needing to handle thousands of requests per second.
However, when you need them, you _really_ need them - And if used correctly, and _sparsely_ may I add,
these guys are an incredible tool for you, to both scale out (**securely**) and more easily build
heterogeneous server environments, without having to try to predict what the future might hold in
regards to its requirements.

* [Documentation](/documentation/)
