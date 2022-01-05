---
title: Dynamic Hyperlambda slots
description: In this article you will learn how to create dynamic Hyperlambda slots, using nothing but Hyperlambda, for then to reuse your slots in other parts of your Hyperlambda, almost the same way a function works in a more traditional programming language.
---

# Dynamic Hyperlambda slots

A dynamic Hyperlambda slot is the equivalent of what you would refer to as a _"function"_ in other programming
languages, since it allows you to declare a dynamic lambda object that you can pass in arguments to, return arguments
from, and treat the same way you would typically treat a function in a more traditional programming language. Consider the
following code.

```
slots.create:foo.bar
   config.get:"magic:databases:default"
   return:x:-
```

The above create a _"dynamic slot"_ for you that you can invoke using the following.

```
signal:foo.bar
```

Assuming you're using MySQL as your default database provider, the above will return the following.

```
signal:mysql
```

A dynamic slot can contain any amount of Hyperlambda you wish, allowing you to encapsulate your logic
into a single point, from where you can reuse it later as you see fit. Below is an example of a slightly
more useful slot, returning all roles that exists in your particular installation.

```
slots.create:foo.bar.get-roles
   data.connect:[generic|magic]
      data.read
         table:roles
         columns
            name
               as:.
      return:x:@data.read/*/*
```

If you invoke the above slot using the following Hyperlambda ...

```
signal:foo.bar.get-roles
```

... you will have something resembling the following returned to you.

```
signal
   .:admin
   .:blocked
   .:chat-admin
   .:guest
   .:moderator
   .:reset-password
   .:root
   .:translator
   .:unconfirmed
```

## Molding your Hyperlambda

The following slots exists in Hyperlambda allowing you to create, signal/invoke, and administrate your
dynamic slots.

* __[signal]__ - Invokes an already existing dynamic slot slot
* __[slots.create]__ - Creates a new dynamic slot
* __[slots.delete]__ - Deletes an existing dynamic slot
* __[slots.exists]__ - Returns true if the specified dynamic slot already exists
* __[slots.get]__ - Returns the lambda object associated with a slot
* __[slots.vocabulary]__ - Returns all dynamic slots to caller, similar to **[vocabulary]**, except will _only_ return dynamic slots.

All in all, the above slots allows you to administrate your existing slots any ways you see fit. As an interesting
exercise try to invoke the following Hyperlambda, assuming you executed the first Hyperlambda in this tutorial.

```
slots.get:foo.bar
```

The above of course will return the following.

```
slots.get:foo.bar
   config.get:"magic:databases:default"
   return:x:-
```

This is an extremely useful feature of Hyperlambda, since the returned lambda object is semantically returned
to the caller, allowing you to modify existing slots semantically, to inject, remove, or modify any parts
of the lambda object they are executing once invoked. To understand the idea, imagine the following code.

```
slots.create:foo.bar
   config.get:"magic:databases:default"
   return:x:-
slots.get:foo.bar
insert-before:x:-/0
   .
      log.info:[foo.bar] was invoked
add:x:+
   get-nodes:x:@slots.get/*
slots.create:foo.bar
slots.get:foo.bar
```

The last invocation to __[slots.get]__ returns the following.

```
slots.get:foo.bar
   log.info:[foo.bar] was invoked
   config.get:"magic:databases:default"
   return:x:-
```

In the above snippet we _semantically_ retrieved a dynamic slot, for then to inject new slot invocations into it,
and saving our updated slot afterwards. This allows you to look at code as a dynamic living thing, possible to
modify over time, according to your needs, whatever they may be. Arguably allowing you to from within your
live production environment literally _semantically 'patch'_ your existing code. Hence your code is no longer
a _"static"_ thing once deployed, but a living and changeable thing you can _"mold"_ and change as you see
fit. In a way this allows you to treat your Hyperlambda code the same way you treat your relational database
system, by providing CRUD capabilities on your codebase, allowing you to change it over time, almost the same
way you'd change data in your database. This is only possible because of Hyperlambda's extreme meta data
capabilities, implying it is super structured in its format, allowing you to semantically traverse it the
same way you would semantically traverse an XML document, and/or a JSON object.

One favourite of mine is to combine these features with cryptographic lambda invocations, to patch
and administrate a multitude of servers dynamically, giving you orchestration capabilities on your servers,
from a single point of administration, to administer a heterogenous environment consisting of a multitude
of servers.

## Persisting dynamic slots

When you create a dynamic slot, it only exists in memory. If for some reasons your web server falls down, your
slot will cease to exist. To create a dynamic slot that is always re-created as your web server start, and/or your
module is installed, you'll have to put your __[slots.create]__ invocation into a file inside your
module's _"magic.startup"_ folder. For instance, if your module is called _"foo"_, and your slot is
named __[foo.bar]__, typically the full name of this file would be _"/modules/foo/magic.startup/foo.bar.hl"_.
All Hyperlambda files existing within your module's _"magic.startup"_ folder will be automatically executed
as the system restarts, and/or is installed.

## Namespacing your slots

Notice, when you invoke __[slots.create]__ any existing slots with the same name will simply be overwritten.
This is intentional, since it creates a simple _"polymorphistic"_ behaviour. However, this implies you need
to carefully _namespace_ your slots. Our advice is to use the name of your company, then the name of your
application/module, for then to add something describing what your slot actually does. An example of this can
be found below.

```
slots.create:acme-company.foo-module.meaning-of-life
   return:int:42
```

This prevents one module from accidentally interferring with objects in another module, by creating a unique namespace,
internally within your server, and/or also globally to some extent. This makes your code more maintainable
and interoperable in the long run.

* [Continue with tasks and scheduled tasks](/tutorials/task-scheduler/)
