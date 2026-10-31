---
title: "How to use [magic.modules.install-module]"
description: "How to use [magic.modules.install-module] - This slot installs a module that has been previously unzipped into your modules folder by making sure all startup files are executed."
guide: true
slots: ["magic.modules.install-module"]
---

This slot installs a module that has been previously unzipped into your modules folder by making sure
all startup files are executed. The slot takes the following argument.

* __[module]__ - Root folder of the module to install Typically you wouldn't want to execute this directly yourself, but rely
upon Magic's middleware to invoke the slot. If you unzip a zip file inside of your _"modules"_ folder,
and/or download a bazar item, this slot will be automatically invoked.
