---
title: Configuring your server
description: Configuring your server can easily be achieved with a root user using the configuration component in Magic. Configuration settings are immediately applied, and changes your server's behaviour instantly.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-configuration.jpg"
---

# Configuring your server

This component allows you to view and edit your server's configuration settings. You server's configuration
is basically your _"appsettings.json"_ file, which is being used in all parts of the system to
retrieve configuration settings, such as for instance when email slots are sending emails, etc.
Below is a screenshot of the component.

![Configuring Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/config-component.jpg)

Notice, you should be careful as you edit your server's configuration settings, since this might
result in that your server becomes erronously configured, resulting in that your system stops working -
In addition to that if you edit your server's configuration erronously, you might open up your server
for malicious adversaries, gaining access to your system.

* [Setup; Create your Magic database](/documentation/magic/components/config/setup-database/)
* [Setup; CRUDify your Magic database](/documentation/magic/components/config/crudify/)
* [Setup; Create your cryptography key pair](/documentation/magic/components/config/crypto/)
* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
