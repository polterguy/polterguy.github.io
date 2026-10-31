---
title: Executing lambda objects
description: The [compose], [eval] and [invoke] slots, allowing you to compose lambda objects and execute them dynamically.
moved_anchors: {"how-to-use-compose": "/plugins/magic.lambda/compose/", "how-to-use-eval": "/plugins/magic.lambda/eval/", "how-to-use-invoke": "/plugins/magic.lambda/invoke/"}
---


* [`compose`](/plugins/magic.lambda/compose/) - Compose allows you to dynamically create expressions by supplying it with a list of iterators.
* [`eval`](/plugins/magic.lambda/eval/) - This is the by far most important slot in Hyperlambda, since it's arguably "the heart" of Hyperlambda, allowing Hyperlambda to execute.
* [`invoke`](/plugins/magic.lambda/invoke/) - This slot works similarly to [eval], except it treats the invocation similarly to an invocation to a dynamic slot, allowing you to pass in arguments, and return nodes from the invocation.
