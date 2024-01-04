---
title: Web Sockets in Magic and Hyperlambda
description: Using web sockets is easily achieved with Magic by simply clicking a button. Hyperlambda contains native support for web sockets through SignalR, and allows you to use this as you see fit in your own apps literally in seconds.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sockets.jpg"
---

# Sockets

The sockets component allows you to subscribe to and publish socket messages. This is useful when
debugging and developing modules that somehow is using the integrated socket slots from Magic. The
sockets component allows you to subscribe to any type of socket message, for then to see messages as
they are published to your _"channel"_, allowing you to more easily debug and develop your modules
that are using sockets.

![Sockets](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sockets.jpg)

If you subscribe to socket messages named _"foo"_ for then to later click the publish button and
publish a message named _"foo"_ you can see how you're notified of this message in your sockets
component automatically.

## Sockets internals

Sockets are probably one of the most complex features related to web development. In Magic
we have significantly simplified it, by giving you high level Hyperlambda slots, allowing you
to easily publish socket messages. However, before you can understand how to use sockets, a little
bit of theory is required. First of all, each socket message consists of two primary parts.

* A _"name"_, which is a _"channel"_ where the message will be published
* A _"payload"_, being a JSON object effectively becoming the _"parameters"_ to your message

This implies that if I subscribe to messages named _"foo.bar"_ in my client/frontend code, then every time
somebody publishes a message with the name of _"foo.bar"_, my code will be automatically invoked,
with the payload from my Hyperlambda code that published the message. If somebody publishes
a _"howdy.world"_ message though, my code will _not_ be invoked unless I also subscribe to such messages.
This creates a communication channel that my backend code can _"push"_ messages through
to my frontend, as long as the client and the backend agrees upon the name of the message(s)
published.

### Sockets authorisation

Allowing everyone to listen to socket messages creates a problem, which is that it allows anybody with knowledge of the name of
your _"channel"_ to subscribe to that channel and be notified every time messages are published
in the channel. Socket messages of course might contain sensitive information, not intended for
all. The way this is solved in Magic is by creating a whole range of alternatives for
autorisation related to publishing messages. What this implies is that the backend needs to choose
which type of authorisation it wants to require from clients subscribing to messages, and only
if the client fulfills the authorisation requirements the backend has associated with the message
as it is publishing the message, the client will be notified of the new message, getting access
to its payload. There are 3 levels of authorisation you can apply when publishing a socket message.

* __[roles]__ - Only subscribers belonging to one of the comma separated roles will be notified
* __[groups]__ - Only subscribers being members of one of the comma separated groups will be notified
* __[users]__ - Only subscribers having authenticated with a username from one of the comma separated list of usernames will be notified

In practice what this implies, is that you have to choose _one_ (or zero) of the above authorisation
schemes when publishing a socket message. Below is some Hyperlambda code illustrating publishing
messages such that _only_ root users and admin users will be notified.

```
socket.signal:foo.bar
   roles:root, admin
   args
      message:Hello from backend
```

You can verify the above by subscribing to _"foo.bar"_ messages using the _"Subscribe"_ button
in your sockets component, for then to click the _"Publish"_ button and write _"foo.bar"_ into
the _"name"_ parts of your message, and paste the following into its _"payload"_ parts.

```json
{
  "message": "Hello from backend"
}
```

If you publish the above message once more, but this time only to the group _"group1"_, you will
_not_ be notified. This is because your user is not a member of the _"group1"_ group. Roles and
users authorisation works similarly, but you can only choose _one_ authorisation mechanism, or
entirely leave authorisation out, ensuring that everyone subscribing to your messages will be notified.
Magic's socket library is built on top of SignalR, which contains client side libraries for literally
hundreds of different frameworks, and/or programming languages, allowing you to easily subscribe
to socket messages in Angular, ReactJS, Swift or Java. Which library you'll need for your
client depends upon which programming language, and/or framework you're using to build your client.
