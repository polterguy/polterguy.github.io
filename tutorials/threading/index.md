---
title: Threading and async Hyperlambda programming
description: This article shows you how Magic and Hyperlambda simplifies everything related to multi threading, making everything extremely scalable out of the box, while eliminating complexity from your own code.
---

# Threading and async Hyperlambda programming

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* Creating multiple threads using Hyperlambda
* Synchronizing access to shared resources
* Waiting for multiple threads to finish
* Basic async theory and why it scales better than synchronised programming

Although Hyperlambda is a super high level programming language, it's got very good support for threading,
and due to that it's _implicitly async in nature_, it's also extremely scalable. In this micro tutorial,
we will walk you through some of the concepts related to threading, and explain how threading is simplified
in Hyperlambda, eliminating an entire axiom of problems related to multithreaded programming. If you prefer
to watch YouTube videos of me demonstrating things, feel free to watch the following video.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/36SYdJN_HIc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Slots related to threading

The following slots are the most common slots that are related to threading in Hyperlambda.

* __[fork]__ - Creates a new thread, which by default will be a _"fire and forget"_ thread.
* __[join]__ - Joins multiple threads, effectively waiting for all _"children"_ threads to finish before continuing execution.
* __[semaphore]__ - Synchronizes access to some piece of lambda such that only one thread can enter at the same time.
* __[sleep]__ - Suspends the active thread for x number of milliseconds.

The most important slot of course is the one that creates a new thread and executes it. Consider the following Hyperlambda.

```
fork
   http.get:"https://servergardens.com"
fork
   http.get:"https://gaiasoul.com"
fork
   http.get:"https://dzone.com"
```

The above code creates 3 _"fire and forget"_ threads, that retrieves the documents found
at their specified URLs, and returns without waiting for the threads to finish. Notice that if you execute
the above code in the Hyperlambda _"Eval"_ menu item, it returns instantly, and you will _not_ see the resulting
HTML documents found at the specified URLs in your output. This is because by simply invoking **[fork]**
the way we do above, we are creating _"fire and forget"_ threads where we don't care about the result of our threads,
before continuing execution to the next line of code.
Sometimes you would rather want to create multiple threads executing in parallel, where you want the result
of the invocation of _all_ of the threads before continuing execution. This can be accomplished with the **[join]**
slot, that will wait for _all_ direct children **[fork]** invocations before continuing execution. Consider the
following Hyperlambda.

```
join
   fork
      http.get:"https://servergardens.com"
   fork
      http.get:"https://gaiasoul.com"
   fork
      http.get:"https://dzone.com"
```

If you execute the above Hyperlambda in the _"Eval"_ menu item, you will see that first of all it takes a lot of
more time, probably some 1 second or maybe even more. This is because the Hyperlambda will _wait_ for all 3 threads
to finish before moving onwards. However, if you measure its time, and you execute each of the above HTTP GET
invocations synchronously, you'll probably realise it's 3 times as slow. This is because the above snippet executes
all 3 GET invocations in parallel. Below is the slower version for comparisons.

```
http.get:"https://servergardens.com"
http.get:"https://gaiasoul.com"
http.get:"https://dzone.com"
```

Hence, with the first example above, we can do multiple long lasting jobs in _parallel_, on 3 separate threads,
speeding up our application. Since our code doesn't need to execute 3 HTTP GET invocations consecutively,
but can execute all of these in parallel on different threads, our app becomes much faster. Hence,
the **[join]**/**[fork]** version would probably on average be almost 3 times as fast as the last version.
This is typically quite useful when we're waiting for IO data, such as waiting for HTTP invocations, reading
or writing to the file system, or executing SQL towards our database. Notice, multithreading does _not_
make CPU intensive tasks faster for the record, quite the contrary in fact, since it requires context switching at
the CPU level, and often multiple synchronization objects further reducing your execution speed. _Do not_ abuse
multithreading.

## Hyperlambda and async

A problem that is fairly commonly experienced with multithreading is _"thread pool exhaustion"_. This occurs
when your operating system is asked to create more threads then it has resources to create at the same time.
What Hyperlambda will do though, is to release your threads as it is waiting for IO data.
This _significantly_ increases your application's scalability and increases the amount of simultaneous users it
can handle before your web server, and/or operating system, literally crashes because of _"thread pool starvation"_.
This is referred to as _"async programming"_, and is a core feature in any modern framework, and/or programming
language, allowing your code to scale much better and handle many more requests simultaneously.

What this implies for Hyperlambda specifically, is that after all 3 threads above are created, and we're
waiting for IO traffic from our URLs, there are actually _zero_ threads being consumed by our application,
since all 3 threads are suspended, released back to the thread pool, and only when the network driver
has data to the specific **[http.get]** invocation, the thread is _"re-animated"_, brought back to life,
given a thread to continue execution, and continues its execution.

From a scalability perspective, this results in that an async application is typically several orders of
magnitudes better at scaling than a synchronous application. However, since async programming is extremely
complex, a lot of things can go wrong as you try to implement it in your own code. Hyperlambda
is _async by default_, and there is no _"special syntax"_ required to understand these parts of it.
This makes async programming much easier to implement with Hyperlambda compared to other more low level
programming languages.

## Synchronizing access to lambda objects

Sometimes you need synchronized access to some shared resource. This can for instance be a file or some
other resource, that is shared amongst multiple threads. For such scenarios you've got the **[semaphore]**
slot. The semaphore slot takes one argument, in addition to a lambda object, ensuring that only _one_
thread given the same semaphore name is able to execute its lambda object at the same time. To understand this
concept, realise this is often referred to as _"toilet threading mode"_, since typically only _one_
person is allowed into the same toilet at the same time. A semaphore is kind of like the _"lock"_
on the toilet door, ensuring only one person is getting access. Consider the following Hyperlambda.

```
join
   fork
      semaphore:foo
         http.get:"https://servergardens.com"
   fork
      semaphore:foo
         http.get:"https://gaiasoul.com"
   fork
      semaphore:foo
         http.get:"https://dzone.com"
```

If you measure the above Hyperlambda's execution speed, you will see that it's at least as slow as the synchronous
version, possibly even slower, due to the threading overhead. This is because our **[semaphore]** invocations
basically ensures that only _one_ HTTP GET invocation is able to execute at the same time. The
first thread to execute the semaphore slot, becomes the first thread allowed to execute its HTTP GET invocation,
while the other 2 threads needs to wait for the first thread to finish before they're allowed access to their
lambda object.
The above example is not a very good example of using semaphores, since none of the above threads actually _need_ a
semaphor, but simply provided to allow you to measure the differences in execution speed for the lambda object as
a whole. A better example can be found below.

```
io.file.save:/foo.md
   .:Initial data
join
   fork
      semaphore:foo
         io.file.load:/foo.md
         strings.concat
            get-value:x:@io.file.load
            .:"\r\nThread 1"
         io.file.save:/foo.md
            get-value:x:@strings.concat
   fork
      semaphore:foo
         io.file.load:/foo.md
         strings.concat
            get-value:x:@io.file.load
            .:"\r\nThread 2"
         io.file.save:/foo.md
            get-value:x:@strings.concat
   fork
      semaphore:foo
         io.file.load:/foo.md
         strings.concat
            get-value:x:@io.file.load
            .:"\r\nThread 3"
         io.file.save:/foo.md
            get-value:x:@strings.concat
io.file.load:/foo.md
```

The above Hyperlambda is more relevant, since multiple threads are accessing the same shared resource
simultaneously, being our _"foo.md"_ file of course. By using a **[semaphore]** above, we ensure
that only one thread is allowed to read and write to the file at the same time. Without the
above **[semaphore]** invocations, we'd run the risk of multiple threads writing to the
file simultaneously, resulting in what is commonly referred to as a _"race condition"_.
Read more about Hyperlambda's threading capabilities [here](/documentation/magic.lambda/).

* Continue with [Interceptors and Exception handlers](/tutorials/super-dry/)
