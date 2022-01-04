
# Magic Lambda Slots

This project provides the ability to create, modify, inspect, and delete dynamic slots for Magic. More specifically,
this project provides the following slots.

* __[signal]__ - Invokes a dynamically create slot that has been created with the __[slots.create]__ slot
* __[slots.create]__ - Creates a dynamic slot, that can be invoked with the __[signal]__ slot
* __[slots.get]__ - Returns the entire lambda object for a slot that has been previously created with the __[slots.create]__ slot
* __[slots.delete]__ - Deletes a slot that has been previously created with the __[slots.create]__ slot
* __[slots.exists]__ - Returns true of the given slot exists
* __[return-nodes]__ - Returns a bunch of nodes to caller from inside of your slot
* __[return-value]__ - Returns a single value to caller from inside of your slot
* __[return]__ - Returns either a list of nodes, or a single value, or both, depending upon the results of its expression,
or whether or not it has a static value, or a list of nodes
* __[slots.vocabulary]__ - Returns the names of all dynamically created slots

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

### [slots.create]

Creates a dynamic slot that can be invoked using **[signal]**. Below is an example.

```
slots.create:foo
   return-value:int:57
```

Notice, slots aren't serialised in any ways, implying if your web server restarts its process, your previously created
dynamic slot is remove. If you want to make sure your slots becomes a permanent part of your application, you need to
make sure you are somehow creating it during server startup, which can normally be done on a per module basis, by putting
a Hyperlambda file into your module's _"magic.startup"_ folder, which makes sure the code is executed during startup
of your web app.

### [signal]

Invokes a previously created dynamic slot. Assuming you have executed the above code snippet, you can invoke the slot using
the following Hyperlambda.

```
signal:foo
```

After evaluating the above Hyperlambda, the **[signal]** node will end up having a value of _"57"_.

**Notice** - This slot obeys by the rules of **[whitelist]** invocations from magic.lambda, allowing you to
declare a list of dynamic slots, which are exclusively allowed to be invoked temporarily inside of an
invocation to whitelist, allowing you to restrict some piece of potentially unsafe code to *only* signal
a pre-defined list of dynamically created slots. Below is an example.

```
slots.create:foo1
   return-value:Safe
slots.create:foo2
   return-value:Unsafe
whitelist
   vocabulary
      signal
      signal:foo1
   .lambda

      // Assuming you have a [foo1] slot created, this will work
      signal:foo1

      // This will throw, since [foo2] is not whitelisted
      signal:foo2
```

Basically, _only_ the slots declared in the above **[vocabulary]** will be allowed to be invoked inside
of the above **[.lambda]** object. You must have your dynamic slots declared as **signal:slot-name**,
such as the above illustrates. And in order to signal dynamic slots *at all*, you'll need to (obviously)
whitelist **[signal]** itself, as illustrated in the above code. Read more about **[whitelist]** in 
the magic.lambda project.

### [slots.get]

Returns the entire lambda code for a previously created dynamic slot. Example can be found below.

```
slots.create:foo
   return-value:int:57
slots.get:foo
```

### [slots.delete]

Deletes a previously created dynamic slot. The following example _will throw an exception_.

```
slots.create:foo
   return-value:int:57
slots.delete:foo

// Throws exception, since [foo] no longer exists.
slots.get:foo
```

### [return-nodes]

Returns a bunch of nodes (lambda) from your slot. Can only be invoked from the inside of
a dynamically created slot. Example below.

```
slots.create:foo
   return-nodes
      integer-value:int:57
      string-value:Foo bar
slots.invoke:foo
```

### [return-value]

Returns a single value from your slot. Can only be invoked from the inside of
a dynamically created slot. Example below.

```
slots.create:foo
   return-value:This becomes the returned value from your slot
slots.invoke:foo
```

### [slots.exists]

Returns true if the specified slot exists. Example can be found below.

```
slots.create:foo
   return-value:Blah, blah, blah ...
slots.exists:foo
slots.exists:DOES-NOT-EXISTS
```

### [slots.vocabulary]

Returns the names of all dynamically created slots to caller. Example can be
found below.

```
slots.vocabulary
```

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.slots](https://github.com/polterguy/magic.lambda.slots), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.slots/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.slots)
