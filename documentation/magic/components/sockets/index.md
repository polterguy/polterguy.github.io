---
title: The Magic sockets component
description: Magic contains integrated web sockets support, allowing you to easily manage and administrate your socket connections, in addition to debugging and developing modules taking advantage of web sockets.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-sockets.jpg"
---

# The Magic sockets component

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
