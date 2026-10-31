---
title: "How to use [magic.auth.change-password]"
description: "How to use [magic.auth.change-password] - Allows a user to change his or her password."
guide: true
slots: ["magic.auth.change-password"]
---

Allows a user to change his or her password. This slot requires the user to be already authenticated and having a valid
JWT token. An example of changing your own password to _"admin2"_ can be found below.

```
signal:magic.auth.change-password
   password:admin2
```

If you invoke the above Hyperlambda, and log out from Magic, you'll need to use _"admin2"_ as your password to
authenticate again. Notice, this slot will evaluate within the context of the _"current user"_, implying the only
person who can change his or her password is the user currently being authenticated.

Yet again, Magic contains helper endpoints for these types of operations, and you would probably never want to
directly invoke the slots yourself, but rather use the helper endpoints from your own frontend if you wish to
use this type of functionality. See the [endpoints](/endpoints/) section for details.
