---
title: Plugins
description: Documentation for Magic's integrated plugin component, allowing you to extend your cloudlet with plugins, such as Shopify plugins, WordPress plugins, etc
og_image: "/images/bazaar.jpg"
header:
  image: /assets/images/wizard-creating-useful-things.webp
---

The Plugins component is Magic's integrated _"AppStore"_, and allows you to install backend micro services on the fly, without interrupting normal usage. It resolves towards AINIRO's repository of plugins, that contains several pre-fabricated backend micro services, serving some generic requirement, such as for instance Stripe payments, OpenAI helpers, and registration helpers. Most plugins automatically takes care of creating their databases, and other things required to initialise the plugin.

![Screenshot of the plugins component allowing you to extend your cloudlet](/images/bazaar.jpg)

## How plugins works in Magic

When you install a plugin, a ZIP file is downloaded from our plugins repository, and unzipped into your modules folder. After unzipping the file, all Hyperlambda files inside the _"magic.startup"_ folder will be automatically executed, allowing for startup and installation logic. And in fact, if you create your own micro service module using Hyperlambda, you should create such startup folders yourself, where you initialise your plugin, by creating slots your module depends upon, creating its initial database if it's needing a database, etc.

After you have installed a plugin, you can see its code by using [Hyper IDE](/dashboard/hyper-ide/), and expand the modules folder, for then to expand the folder where your plugin was installed, and look at its files. You can even immediately edit any files this way too, but if you do, you can no longer update your plugin. If your plugin creates a database of some sort, you can also look at your database using [SQL Studio](/dashboard/sql-studio/).
