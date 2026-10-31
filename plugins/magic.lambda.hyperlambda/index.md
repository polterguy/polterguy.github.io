---
title: magic.lambda.hyperlambda
moved_anchors: {"how-to-use-hyper2lambda": "/plugins/magic.lambda.hyperlambda/hyper2lambda/", "how-to-use-hyperlambdaverify-slots": "/plugins/magic.lambda.hyperlambda/hyperlambda.verify-slots/", "how-to-use-lambda2hyper": "/plugins/magic.lambda.hyperlambda/lambda2hyper/"}
---

This is the Hyperlambda parser and generator in Magic, and allows you to parse Hyperlambda, in addition
to generate Hyperlambda. More specifically, this project provides you with the following slots.

* __[\[hyper2lambda\]](/plugins/magic.lambda.hyperlambda/hyper2lambda/)__ - Transforms a piece of Hyperlambda (text) to a lambda hierarchy
* __[\[lambda2hyper\]](/plugins/magic.lambda.hyperlambda/lambda2hyper/)__ - Transforms a lambda hierarchy to Hyperlambda (text)
* __[\[hyperlambda.verify-slots\]](/plugins/magic.lambda.hyperlambda/hyperlambda.verify-slots/)__ - Verifies that all slots referenced in executable statement position of a Hyperlambda snippet exist

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
