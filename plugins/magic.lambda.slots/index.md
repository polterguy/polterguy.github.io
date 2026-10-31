---
title: magic.lambda.slots
moved_anchors: {"how-to-use-execute": "/plugins/magic.lambda.slots/execute/", "how-to-use-return-nodes": "/plugins/magic.lambda.slots/return-nodes/", "how-to-use-return-value": "/plugins/magic.lambda.slots/return-value/", "how-to-use-signal": "/plugins/magic.lambda.slots/signal/", "how-to-use-slotscreate": "/plugins/magic.lambda.slots/slots.create/", "how-to-use-slotsdelete": "/plugins/magic.lambda.slots/slots.delete/", "how-to-use-slotsexists": "/plugins/magic.lambda.slots/slots.exists/", "how-to-use-slotsget": "/plugins/magic.lambda.slots/slots.get/", "how-to-use-slotsvocabulary": "/plugins/magic.lambda.slots/slots.vocabulary/", "how-to-use-try-signal": "/plugins/magic.lambda.slots/try-signal/"}
---

The magic.lambda.slots project provides the ability to create, invoke (signal), modify, inspect, and delete
dynamic slots in Hyperlambda. More specifically, this project provides the following slots.

* __[\[signal\]](/plugins/magic.lambda.slots/signal/)__ - Invokes a dynamically create slot that has been created with the __[slots.create]__ slot
* __[\[execute\]](/plugins/magic.lambda.slots/execute/)__ - Alias for **[signal]** except it will **[unwrap]** all descendant nodes explicitly
* __[\[try-signal\]](/plugins/magic.lambda.slots/try-signal/)__ - Invokes a dynamically create slot that has been created with the __[slots.create]__ slot, but will _not_ throw exceptions if the slot doesn't exist
* __[\[slots.create\]](/plugins/magic.lambda.slots/slots.create/)__ - Creates a dynamic slot, that can be invoked with the __[signal]__ slot
* __[\[function\]](/plugins/magic.lambda.slots/function/)__ - Alias for **[slots.create]**
* __[\[slots.get\]](/plugins/magic.lambda.slots/slots.get/)__ - Returns the entire lambda object for a slot that has been previously created with the __[slots.create]__ slot
* __[\[slots.delete\]](/plugins/magic.lambda.slots/slots.delete/)__ - Deletes a slot that has been previously created with the __[slots.create]__ slot
* __[\[slots.exists\]](/plugins/magic.lambda.slots/slots.exists/)__ - Returns true of the given slot exists
* __[\[return-nodes\]](/plugins/magic.lambda.slots/return-nodes/)__ - Returns a bunch of nodes to caller from inside of your slot
* __[\[return-value\]](/plugins/magic.lambda.slots/return-value/)__ - Returns a single value to caller from inside of your slot
* __[\[return\]](/plugins/magic.lambda.slots/return/)__ - Returns either a list of nodes, or a single value, or both, depending upon the results of its expression,
or whether or not it has a static value, or a list of nodes
* __[\[yield\]](/plugins/magic.lambda.slots/yield/)__ - Alias for **[return-nodes]** but similarly to **[execute]** it will **[unwrap]** all descendant nodes explicitly
* __[\[slots.vocabulary\]](/plugins/magic.lambda.slots/slots.vocabulary/)__ - Returns the names of all dynamically created slots

```
/*
 * First we create a dynamic slot.
 */
slots.create:foo
   return-value:int:57

/*
 * Then we invoke it.
 */
signal:foo
```

After evaluation of the above Hyperlambda, the value of the __[signal]__ node will be 57. Notice, if you
invoke __[slots.create]__ for a slot that has already been created, the old slot will be overwritten with the
new lambda object you pass into it. Also notice that if you try to invoke a slot that doesn't exist, or you try
to get its content, an exception will be thrown.

Also realize that when you create a slot, it is not persisted in any ways - Implying if the web server process
is restarted, your slot will disappear. To avoid this, put the creation of your slot inside a file
in a folder called _"magic.startup"_ in your module's folder, e.g. _"/files/modules/foo-module/magic.startup/create-slot.hl"_.
All files inside of modules that exists within a _"magic.startup"_ folder will be executed every time your web
server restarts for some reasons.
