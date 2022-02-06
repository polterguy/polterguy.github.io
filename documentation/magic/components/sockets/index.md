---
title: Web Sockets and SignalR
description: Using web sockets is easily achieved with Magic by simply clicking a button. Hyperlambda contains native support for web sockets through SignalR, and allows you to use this as you see fit in your own apps literally in seconds.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-sockets.jpg"
---

# Web Sockets and SignalR

The sockets component allows you to subscribe to and publish socket messages. This is useful when
debugging and developing modules that somehow is using the integrated socket slots from Magic.
To understand how Magic's socket library is tied together refer to [this document](/documentation/magic.lambda.sockets/).
The sockets component allows you to subscribe to any type of socket message, for then to see messages
as they are published to your _"channel"_, allowing you to more easily debug and develop your
modules that are using sockets. Below is a screenshot of how subscribing to a socket message
should look like.

![Sockets](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sockets.jpg)

If you subscribe to socket messages named _"foo"_ for then to later click the publish button and
publish a message named _"foo"_ you can see how you're notified of this message in your sockets
component automatically.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
