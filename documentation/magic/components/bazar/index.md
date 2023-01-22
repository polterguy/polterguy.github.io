---
title: The Bazaar, an AppStore for your server
description: With the Bazaar you can rapidly purchase, and/or install free backend micro services on the fly, without interrupting your production environment. Click a button, pay the purchase price if any, download the micro service, and voila! You've got a new micro service solving some problem related to your particular problem.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/bazaar.jpg"
---

# The Plugins component

The plugins component is Magic's integrated _"AppStore"_, and allows you to install backend micro
services on the fly, without interrupting normal usage. It resolves towards Aista's repository of plugins, that
contains several pre-fabricated backend micro services, serving some generic requirement, such as
for instance translations, ticket management, etc. Most plugins automatically takes care of creating
their databases, and other things required to initialise the plugin.

![Magic's plugins](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/bazaar.jpg)

Notice, such plugin micro services _might_ cost you a fee to install into your own Magic backend,
implying you'll have to go through PayPal or some similar payment provider to gain access to install the
plugin.

## Plugins provided by Aista

Below is a list of some of the plugins we provide out of our plugins module.

* Aista CRM, a small SQLite database DDL script creating a CRM type of database for you
* Stripe Payments, allowing you to integrate Stripe payments into your own Hyperlambda solutions
* Tickets, a micro service ticket system, giving you the ability to persist support requests, and answer these
* SQLite Sakila DB, which is MySQL's Sakila database ported to SQLite
* SQLite Northwind DB, which is Microsoft's Northwind database ported to SQLite
* SQLite Chinook DB, which is another SQLite type of database that tracks albums, tracks, artists, etc
* BabelFish, which is a translation micro service making it easy to translate your applications into a whole range of different languages

## How plugins works in Magic

When you install a plugin, a ZIP file is downloaded from our plugins repository, and unzipped into your modules
folder. After unzipping the file, all Hyperlambda files inside of any _"magic.startup"_ folders found inside of your
plugin will be automatically executed, allowing for startup and installation logic. And in fact, if you create
your own micro service module using Hyperlambda, you should create such startup folders yourself, where you
initialise your plugin, by creating slots your module depends upon, creating its initial database if it's
needing a database, etc.

After you have installed a plugin, you can see its code by using [Hyper IDE](/documentation/magic/components/hyper-ide/)
and expand the modules folder for then to expand the folder where your plugin was installed, and look at
its files using Hyper IDE. You can even immediately edit any files this way too, but if you do, you
can no longer update your plugin. If your plugin creates a database of some sort, you can also immediately
look at your database using [SQL Studio](/documentation/magic/components/sql/).
