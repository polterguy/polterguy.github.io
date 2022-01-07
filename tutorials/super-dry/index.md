---
title: Interceptors and exception handlers
description: This article shows you how to create Super DRY code using Hyperlambda, by leveraging interceptors and exception filters, allowing you to create your functionality without having to repeat your code.
---

# Interceptors and exception handlers

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* Interceptors, and how they reduce repetition in your code
* Exception handlers, and how they allow you to keep your exception code in _one_ place

In this tutorial we will have a look at two features that allows you to write _"super DRY code"_. DRY here
refers to _"Don't Repeat Yourself"_, which is an important design principle as you
create software. If you prefer to watch video tutorials having me demonstrating how things are tied together,
you can watch the following video where I walk you through these parts.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/QKQjUhRBwu0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

As illustrated above, any _"exceptions.hl"_ file, and/or _"interceptor.hl"_ file will allow you to
ensure your code becomes DRY. Below is an example of how you could tie these parts together if you wish.
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

If you invoke your endpoint now, you will see everything working. The reasons is because the endpoint
URL resolver will actually combine your _"interceptor.hl"_ file with your _"bar.get.hl"_ file, resulting
in the following combined lambda object.

```
log.info:Interceptor
data.connect:[generic|magic]
   log.info:Endpoint file
   data.read
      table:users
      columns
         username
   return-nodes:x:@data.read/*
```

This of course makes it easy for you to _"outsource"_ commonalities in your folders to a single
file, having everything occurring in one single file, to avoid repeating yourself.
Interceptors are _recursively_ applied, implying if you have multiple _"interceptor.hl"_
files upwards in your hierarchy, then _all_ your interceptors will be applied, creating a combined result,
before your lambda object is executed.

* [Continue with Dynamic Hyperlambda slots](/tutorials/dynamic-slots/)
