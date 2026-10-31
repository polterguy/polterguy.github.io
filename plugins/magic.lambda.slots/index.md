---
title: magic.lambda.slots
moved_anchors: {"how-to-use-execute": "/reference/slots/core/execute/#guide", "how-to-use-return-nodes": "/reference/slots/core/return-nodes/#guide", "how-to-use-return-value": "/reference/slots/core/return-value/#guide", "how-to-use-signal": "/reference/slots/core/signal/#guide", "how-to-use-slotscreate": "/reference/slots/slots/slots.create/#guide", "how-to-use-slotsdelete": "/reference/slots/slots/slots.delete/#guide", "how-to-use-slotsexists": "/reference/slots/slots/slots.exists/#guide", "how-to-use-slotsget": "/reference/slots/slots/slots.get/#guide", "how-to-use-slotsvocabulary": "/reference/slots/slots/slots.vocabulary/#guide", "how-to-use-try-signal": "/reference/slots/core/try-signal/#guide"}
---

The magic.lambda.slots project provides the ability to create, invoke (signal), modify, inspect, and delete
dynamic slots in Hyperlambda. More specifically, this project provides the following slots.

* __[\[signal\]](/reference/slots/core/signal/)__ - Invokes a dynamically create slot that has been created with the __[slots.create]__ slot
* __[\[execute\]](/reference/slots/core/execute/)__ - Alias for **[signal]** except it will **[unwrap]** all descendant nodes explicitly
* __[\[try-signal\]](/reference/slots/core/try-signal/)__ - Invokes a dynamically create slot that has been created with the __[slots.create]__ slot, but will _not_ throw exceptions if the slot doesn't exist
* __[\[slots.create\]](/reference/slots/slots/slots.create/)__ - Creates a dynamic slot, that can be invoked with the __[signal]__ slot
* __[\[function\]](/reference/slots/core/function/)__ - Alias for **[slots.create]**
* __[\[slots.get\]](/reference/slots/slots/slots.get/)__ - Returns the entire lambda object for a slot that has been previously created with the __[slots.create]__ slot
* __[\[slots.delete\]](/reference/slots/slots/slots.delete/)__ - Deletes a slot that has been previously created with the __[slots.create]__ slot
* __[\[slots.exists\]](/reference/slots/slots/slots.exists/)__ - Returns true of the given slot exists
* __[\[return-nodes\]](/reference/slots/core/return-nodes/)__ - Returns a bunch of nodes to caller from inside of your slot
* __[\[return-value\]](/reference/slots/core/return-value/)__ - Returns a single value to caller from inside of your slot
* __[\[return\]](/reference/slots/core/return/)__ - Returns either a list of nodes, or a single value, or both, depending upon the results of its expression,
or whether or not it has a static value, or a list of nodes
* __[\[yield\]](/reference/slots/core/yield/)__ - Alias for **[return-nodes]** but similarly to **[execute]** it will **[unwrap]** all descendant nodes explicitly
* __[\[slots.vocabulary\]](/reference/slots/slots/slots.vocabulary/)__ - Returns the names of all dynamically created slots

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
