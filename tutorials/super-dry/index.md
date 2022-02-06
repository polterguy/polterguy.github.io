---
title: Interceptors and exception handlers in Hyperlambda
description: This article shows you how to create Super DRY code using Hyperlambda, by leveraging interceptors and exception handlers, allowing you to create your functionality without having to repeat your code.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-exceptions-interceptors.jpg"
---

# Interceptors and exception handlers in Hyperlambda

This tutorial covers the following parts of Magic and Hyperlambda.

* Interceptors, and how they allow you to create DRY code
* Exception handlers, and how to keep your error handling in one place

In this tutorial we will have a look at two features that allows you to write _"Super DRY code"_. DRY here
refers to _"Don't Repeat Yourself"_, and is an important design principle as you
create software. These two features are referred to as _"interceptors"_ and "_exception handlers"_.
Below is an example of how you could tie these parts together.
Make sure you create a new folder within your _"modules"_ folder, name your folder _"foo"_, and put the
following 3 files into that folder.

## exceptions.hl

```
log.error:x:@.arguments/*/message
return
   message:Some error occurred
   status:int:555
```

## interceptor.hl

```
log.info:Interceptor
data.connect:[generic|magic]
   .interceptor
```

## bar.get.hl

```
log.info:Endpoint file

// Unccomment the next line to test exception handlers
// throw:An exception occurred

data.read
   table:users
   columns
      username
return-nodes:x:@data.read/*
```

If you invoke your endpoint now, you will see everything working, even though you're not explicitly opening up a database
connection in your above _"bar.get.hl"_ file. The reasons is because the endpoint URL resolver will actually _combine_
your _"interceptor.hl"_ file with your _"bar.get.hl"_ file, resulting in the following combined lambda object.

```
// Fetched from "interceptor.hl"
log.info:Interceptor
data.connect:[generic|magic]

   // Fetched from "bar.get.hl"
   log.info:Endpoint file
   data.read
      table:users
      columns
         username
   return-nodes:x:@data.read/*
```

This of course makes it easy for you to _"outsource"_ commonalities in your folders to a single
file, having everything occurring in one single file, to avoid repeating yourself.
Notice, interceptors are _recursively_ applied, implying if you have multiple interceptors
upwards in your folder hierarchy, then _all_ interceptors will be applied, creating a combined result,
before your lambda object is executed. Exception handlers though are _not_ recursively applied, and
only the _first_ exception handler upwards in your folder structure will be used. Interceptors
are hence said to be _extendable_ , while exception handlers are said to be _overriding_.

To understand the exception handler parts of our code, try to add the following Hyperlambda into
your above _"bar.get.hl"_ file somewhere.

```
throw:Throwing an exception ...
```

Notice how the status code and error message is _"transformed"_ by our exception handler. This is
because our exception handler is invoked with our original exception, and whatever it returns
is what is returned to the client. By creating exception handlers such as above, you get to keep
all your error logic in _one place_, and have common error logic for your modules, allowing
you to for instance translate exception messsages, or create specific exception handlers for
some of your folders, etc.

* Continue with [Dynamic Hyperlambda slots](/tutorials/dynamic-slots/)
