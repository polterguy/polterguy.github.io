---
layout: post
author: thomas
title: The Magic setup process
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/setup-explained.jpg"
---

When you first start Magic you will have to configure it. Before I guide you through this process though,
please realise that Magic's frontend dashboard was created to be able to manage _multiple_ backends.
This is the reason it asks you for a _"Backend"_ as you start it. If you're using the source code
ZIP download of Magic, you should provide the following in the backend textbox.

```
http://localhost:5000
```

If you use the docker images you should provide the following.

```
http://localhost:4444
```

If you have installed Magic on a VPS, you need to provide the backend primary URL to your backend,
whatever that is. Then you need to login to your Magic dashboard. Before Magic has configured a database,
and applied a JWT authentication secret, your username and password is `root`/`root`. However, Magic will
ask you to change this immediately after having logged in. Standard values for logging into your backend
using the source code ZIP download can be found below. If you're using docker exchange the URL
to `http://localhost:4444`.

![Default login](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/setup-explained.jpg)

The way Magic determines whether or not to allow you to login with your default credentials or not, is by
checking your `magic:auth:secret` configuration value. You can find this value your backend's _"config/appsettings.json"_
configuration file. Its default value looks like the following.

![Default configuration settings](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/default-auth.jpg)

The important parts here is the _"THIS-IS-NOT-A-GOOD-SECRET-PLEASE-CHANGE-IT"_ part. As Magic logs
you in as a _"root_", it will check this configuration value, and if it finds the above value for
your auth secret, it will guide you through setting up Magic. After you have successfully pointed
Magic to a database, the above value will change to something such as follows.

```
REfmCj8ZlzgtXV3BMG3hPrciAghlBzUQhIRPtPqKl9BAYvvB6hKpXbucDhyldVOiMtZuU815SMlYcueOYmSyIQT7nggsY
```

The idea being that this becomes your JWT secret, providing you with security, allowing Magic to
generate JWT tokens that cannot be reproduced by an adversary. At this point you can no longer
use _"root"_ as your root user's password, but you have to provide whatever password you chose
as you configured your database. Below is a screenshot (light theme) of how Magic will look
like after you've logged into it for the first time.

![Setup database](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-database.jpg)

Whatever you type in the above password field becomes your root user's password. Notice, this
user have _full access_ to everything in Magic, and you should provide a highly secure password here.

When you click _"Next"_ in the above screen, Magic will create a magic database for you, insert a new
root user into it, with the password you provided, and lead you to the next setup screen. When Magic
is done with the above step it will ask you to _"crudify"_ your Magic database. This implies creating
HTTP endpoints wrapping your newly created magic database. This typically resembles the following.

![Crudify magic database](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-crudify.jpg)

Click _"Next"_ in the above screen, at which point you're brought to the following.

![Create cryptography key pair](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-crypto.jpg)

The above setup step will have Magic create a cryptography key pair for your Magic server. This cryptography
key is used a lot of places in Magic, and basically allows Magic to cryptographically secured communicate
with other servers, and/or clients. Notice, as you click the above _"Next"_ button Magic will need some time
to create your cryptography key pair. However, when it's done, your Magic server configuration process is done,
and you can optionally run the assumptions to verify everything is working as it should. Below is a YouTube
video illustrating the process. Notice, if you're not using Docker, you'll have to change the backend URL
I'm using in the video.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/wCOcch2r03A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


