---
title: Magic middleware documentation
description: The Magic middleware is the parts wiring up Magic, allowing you to use Magic in your own projects, providing you with a default backend for your own frontend apps, authentication, authorisation, and CRUD endpoints wrapping your database(s).
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-getting-started.jpg"
---

# Magic's middleware

Magic's middleware gives you a whole range of HTTP endpoints allowing you to administrate your particular
Magic installation, in addition to providing you with UI components you can use to manage your installation.
The middleware is the part you typically _"see"_, and the parts you interact with as you create your
own applications and modules.

## Initialisation

When you start Magic for the first time, the system might need to initialise itself, which implies doing 2
things.

* Create a magic database, insert a root user into it, and initialise the authentication secret
* Create a cryptography key pair for your server

These steps are what you're going through as you initially install Magic, either locally, or on
a VPS of your chosing. The first step requires you to have a database of some sort somewhere, where
Magic can create its internal `magic` database. Magic will use this database for authenticating users,
logging, persisting tasks, etc. If you don't have a database, you can use SQLite.
The 2nd step is required to create a public and private server key pair. This key is used for among
other things cryptographically secured Hyperlambda invocations.

## Magic's file structure

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

## How Magic handles exceptions

The _"exceptions.hl"_ file at the root of your folder structure is the default exception handler
that will be used if no module creates its own exception handler logic to override the default handler.
Most folders have _"README.md"_ files that somehow describes the purpose of the folder. Hyper IDE
is as a general rule of thumb your _"goto component"_ when you need to create something using Magic.

## Dashboard components

* [Log component](/documentation/magic/components/log/)
* [Health check component](/documentation/magic/components/assumptions/)
* [Endpoints component](/documentation/magic/components/endpoints/)
* [Sockets component](/documentation/magic/components/sockets/)
* [Hyper IDE component](/documentation/magic/components/hyper-ide/)
* [Evaluator component](/documentation/magic/components/evaluator/)
* [SQL component](/documentation/magic/components/sql/)
* [Endpoint generator component](/documentation/magic/components/crudifier/backend/)
* [Frontend generator component](/documentation/magic/components/crudifier/frontend/)
* [Tasks component](/documentation/magic/components/tasks/)
* [Users and roles component](/documentation/magic/components/auth/)
* [Users component](/documentation/magic/components/auth/users/)
* [Roles component](/documentation/magic/components/auth/roles/)
* [Config component](/documentation/magic/components/config/)
* [Crypto component](/documentation/magic/components/crypto/)
* [Plugins component](/documentation/magic/components/bazar/)
* [Profile component](/documentation/magic/components/profile/)

## Backend and middleware documentation

* [Endpoints documentation](/documentation/magic/endpoints/)
* [Slots documentation](/documentation/magic/slots/)
