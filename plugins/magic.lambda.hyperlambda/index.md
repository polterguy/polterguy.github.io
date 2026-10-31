---
title: magic.lambda.hyperlambda
---

This is the Hyperlambda parser and generator in Magic, and allows you to parse Hyperlambda, in addition
to generate Hyperlambda. More specifically, this project provides you with the following slots.

* __[hyper2lambda]__ - Transforms a piece of Hyperlambda (text) to a lambda hierarchy
* __[lambda2hyper]__ - Transforms a lambda hierarchy to Hyperlambda (text)
* __[hyperlambda.verify-slots]__ - Verifies that all slots referenced in executable statement position of a Hyperlambda snippet exist

Using these slots, you can both easily create, serialize, and parse Hyperlambda to lambda, and vice versa.
Below is an example of parsing a piece of text as Hyperlambda, for then to dynamically execute it afterwards.

```
.hl:@"log.info:""This was logged from a piece of text"""

hyper2lambda:x:-

eval:x:-
```

You can also reverse the process, such as the following illustrates.

```
.hl
   log.info:This is some example logging invocation

lambda2hyper:x:-/*
```

The above two slots, allows you to dynamically generate plain text from a lambda structure, and vice versa,
allowing you to for instance persist execution objects and structured data into files, your database, or for
that matter transmit it over the network to another machine. Below is an example of dynamically
loading a Hyperlambda file from disc, for then to execute it. Notice, in order to have the following
snippet work, you'll need an actual file called _"foo.hl"_ inside of your backend's _"files/"_ folder.

```
io.file.load:/foo.hl

hyper2lambda:x:-

eval:x:-
```

**Notice** - Both of these slots can optionally be given a **[comments]** argument with a value of `true`,
at which point both **[lambda2hyper]** and **[hyper2lambda]** will preserve comments, and persist these as
**[..]** nodes into your lambda, and reverse the process for the other direction. This allows you to keep the
comments of your Hyperlambda parts as semantic nodes, as you handle your Hyperlambda and node hierarchy.

## How to use [hyper2lambda]

This slot creates a semantic lambda object (graph object) from the specified text. Below is an example
of usage.

```
.hl:@"log.info:""This was logged from a piece of text"""
hyper2lambda:x:-
```

The above of course produces an executable lambda object from your specified Hyperlambda text.

## How to use [lambda2hyper]

This slot creates a Hyperlambda string from your specified lambda object. This allows you to
transfer your Hyperlambda to some other server, and/or persist it to disc. Below is example
usage.

```
.hl
   log.info:This is some example logging invocation
lambda2hyper:x:-/*
```

## How to use [hyperlambda.verify-slots]

This slot statically verifies a piece of Hyperlambda without executing it, and is useful for checking generated
Hyperlambda before you run it. A slot name that doesn't exist is silently treated as an inert data node by the
evaluator, and this slot surfaces such names. The Hyperlambda to verify is given as the value of the slot, either as
a string or as an expression leading to a string. If no value is given, the slot verifies its own children instead.
Below is an example.

```
.hl:@"try
   missing.try
.catch
   eval"

hyperlambda.verify-slots:x:@.hl
```

The slot returns `false` if the Hyperlambda is invalid, and `true` if it is valid, in which case it has no children.
When it returns `false`, every missing slot name is returned as an unnamed child node, and the example above
returns `missing.try` this way.

The slot verifies the root level of the Hyperlambda, in addition to the bodies of slots such as **[try]**,
**[.catch]**, **[.finally]**, **[switch]**, **[case]**, **[default]** and **[eval]**, to any depth. Nodes whose
names start with a `.`, such as variables, comments and **[.arguments]**, are not treated as slot invocations, and
arguments such as the **[table]** and **[where]** nodes of **[data.read]** are not checked as slots.

In addition to missing slots, the slot also reports the following as **[invalid-invocation]** child nodes.

* A slot that requires a primary value, but is invoked without one.
* A slot that requires either a primary value or child nodes, but is invoked with neither.
* A child argument that the slot's signature doesn't declare.
