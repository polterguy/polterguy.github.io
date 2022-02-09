---
title: A web based terminal
description: Magic contains an integrated Terminal component, allowing you to securely execute bash scripts in your backend.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-terminal.jpg"
---

# A web based terminal

The terminal component allows you to directly access your backend server through an interface
wrapping your server's native bash/terminal/shell. This is useful if you for some
reasons need to use native operating system features, and/or programs that does not have
a GUI interface in Magic - Such as for instance when needing to install services and programs
to your backend server. Below is a screenshot of the component.

![Web terminal](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/terminal.jpg)

You can write any bash command into it. What command you can use varies according to what operating
system you have deployed your Magic backend unto. The Terminal component works through connecting
to a web socket channel with the backend, implying if you've deployed Magic into a Kubernetes cluster,
then the load balancing parts of Magic might result in it not being available for you.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
