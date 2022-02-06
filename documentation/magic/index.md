---
title: Magic middleware documentation
description: In this article we will look at the Magic middleware, which is the parts wiring up Magic, allowing you to have authentication and authorisation for your modules, and also allows you to automate and remote large parts of your own Magic backend.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-getting-started.jpg"
---

# Magic middleware documentation

This is the documentation for Magic itself, implying the _"middleware"_ found in Magic's core.
This part documents everything that wires up Magic, and the backend of modules
such as Hyper IDE and the CRUDifier. This is where you will find information about the file system
of Magic, system endpoints, system slots, and everything that makes Magic _"tick"_. This is hence
the documentation of [Magic itself](https://github.com/polterguy/magic).

## File structure

There are 4 primary folders in Magic, these are as follows.

* __etc__ - Your private _"data files"_
* __misc__ - Magic's _"data files"_
* __modules__ - Your own custom modules goes here
* __system__ - Magic's system modules goes here

The _"modules"_ folder and the _"system"_ folders are the only folders that allows for resolving Hyperlambda
endpoints, while the other folders are for helper files, and/or uploaded files. If you use the docker images
of Magic, Magic will automatically update the following folders as you pull the Docker images from Docker hub.

* misc
* system

This implies that you _should not_ edit files in these folders, since if you do, your changes might vanish
the next time you update Magic. You should also not store your own files in these folders, since your files
might disappear the next time you update Magic. The only folder where it's safe to store your own files
and folders within are as follows.

* __etc__ - For dynamic files, uploads and downloads, etc
* __modules__ - For your own custom Hyperlambda modules

The two remaining folders; _"misc"_ and _"system"_ should be kept for Magic's internals, and not tampered
with in any ways. If in doubt, most folders in Magic has README files you can open to see the purpose
of a specific folder, and/or its files - And in fact, becoming acquinted with Magic's file and folder 
structure is probably a smart investment, since everything in Magic is based upon _"conventions"_, implying
folders have semantic value of some sort. As a general rule of thumb you should keep all your Hyperlambda
code inside _"modules"_ and everything else in _"etc"_.

### Creating startup logic

Most modules requires some sort of _"initialisation"_ logic. This can be to for instance create dynamic slots
the module depends upon to function, and/or ensure the module's database exists, etc. This can be accomplished
by creating a folder _inside_ your module and name this module _"magic.startup"_. All files recursively found
inside this folder will be executed as the system starts, and/or the module is installed. You can also create
such startup folders inside of _sub_ folders within your module's main folder.

## Initialisation

When you start Magic for the first time, the system might need to initialise itself, which implies doing 3
things.

* Create a magic database, insert a root user into it, and initialise the authentication secret
* CRUDify the magic database
* Create a cryptography key pair for your server

These 3 steps is what you're going through as you initially install Magic, either locally, or on
a VPS of your chosing. The first step requires you to have a database of some sort somewhere, where
Magic can create its internal `magic` database. Magic will use this database for authenticating users,
logging, persisting tasks, etc.
The second step implies generating CRUD HTTP backend endpoints wrapping this database, to allow
you to interact with it through a client of some sort. The 3rd step is required to create a
public and private server key pair. This key is used for cryptographically secured lambda
invocations, but also in other parts of the system. Below is a screenshot of how this process
looks like as you install Magic initially.

![Configuring Magic initially](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/configuring-magic.jpg)

After you have followed the above process, you can see that inside your _"modules"_ folder there
exists Hyperlambda endpoint files wrapping your entire magic database into CRUD HTTP endpoints.
These files were created in the second step of the above process, and is required to have Magic
functioning properly. Below you can see a screenshot of how the folder structure looks like in
Magic through Hyper IDE.

![Magic folder structure through Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/folder-structure.jpg)

The _"exceptions.hl"_ file at the root of your folder structure is the default exception handler
that will be used if no module creates its own exception handler logic to override the default handler.
Most folders have _"README.md"_ files that somehow describes the purpose of the folder. Hyper IDE
is as a general rule of thumb your _"goto component"_ when you need to create something using Magic.

## Dashboard components

* [Log component](/documentation/magic/components/log/)
* [Assumptions component](/documentation/magic/components/assumptions/)
* [Cache component](/documentation/magic/components/cache/)
* [Endpoints component](/documentation/magic/components/endpoints/)
* [Sockets component](/documentation/magic/components/sockets/)
* [Hyper IDE component](/documentation/magic/components/hyper-ide/)
* [Evaluator component](/documentation/magic/components/evaluator/)
* [SQL component](/documentation/magic/components/sql/)
* [Crudifier component](/documentation/magic/components/crudifier/)
* [Terminal component](/documentation/magic/components/terminal/)
* [Tasks component](/documentation/magic/components/tasks/)
* [Auth component](/documentation/magic/components/auth/)
* [Config component](/documentation/magic/components/config/)
* [Crypto component](/documentation/magic/components/crypto/)
* [Bazar component](/documentation/magic/components/bazar/)
* [Profile component](/documentation/magic/components/profile/)

## Backend/middleware documentation

* [Endpoints documentation](/documentation/magic/endpoints/)
* [Slots documentation](/documentation/magic/slots/)
* [Back to main documentation](/documentation/)
