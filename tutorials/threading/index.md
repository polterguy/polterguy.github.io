
# Threading and async Hyperlambda programming

Although Hyperlambda is a super high level programming language, it's got very good support for threading,
and due to that it's _implicitly async in nature_, it's also extremely scalable. In this micro tutorial,
we will walk you through some of the concepts related to threading, and explain how threading is simplified
in Hyperlambda, eliminating an entire axiom of problems typically related to creating and handling multithreaded
programming. If you prefer to watch YouTube videos of me demonstrating things, feel free to watch the following
video.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/36SYdJN_HIc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Slots related to threading

The following slots are the most common slots that are related to threading in Hyperlambda.

* __[fork]__ - Creates a new thread, which by default will be a _"fire and forget"_ thread.
* __[join]__ - Joins multiple threads, effectively waiting for all _"children"_ threads to finish before continuing execution.
* __[semaphore]__ - Synchronizes access to some piece of lambda such that only one thread can enter at the same time.

The most important slot of course is the one that creates a new thread and executes it. Consider the following Hyperlambda.

```
fork
   http.get:"https://servergardens.com"
fork
   http.get:"https://gaiasoul.com"
fork
   http.get:"https://dzone.com"
```

What the above code does is to create 3 _"fire and forget"_ threads, which simply fetches the documents found
at the specified URLs, and returns without waiting for the threads to finish. Notice though, that if you execute
the above code in the Hyperlambda _"Eval"_ menu item, it returns instantly, and you will _not_ see the resulting
HTML documents found at the specified URLs in your result output parts. This is because by simply invoking **[fork]**
the way we do above, we are creating _"fire and forget"_ threads, were we don't care about the result of our threads,
before continuing execution to the next line of code.

Sometimes you would rather want to create multiple pieces of code, executing in parallel, where you want the result
of the invocation of _all_ of the threads, before continuing execution. This can be accomplished with the **[join]**
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

Hence, with the first example above, we can do multiple long lasting jobs in parallel, on 3 separate threads,
speeding up our own application. Since our code doesn't need to execute 3 HTTP GET invocations consecutively,
but can execute all of these in parallel, on different threads, our app becomes much faster. Hence,
the **[join]**/**[fork]** version would probably on average be almost 3 times as fast as the last version.

This is typically quite useful when we're waiting for IO data, such as waiting for HTTP invocations, reading
or writing to the file system, or executing SQL towards our database. Multi threading does typically _not_
make CPU intensive tasks faster for the record, quite the contrary, since it requires context switching at
the CPU level, and often multiple synchronization objects further reducing your execution speed. _Do not_ abuse
multithreading.

## Hyperlambda is async by default

A problem that is fairly commonly experienced with multithreading is _"thread pool exhaustion"_. This occurs
when your operating system is asked to create more threads than it has resources to create at the same time.
What Hyperlambda will do though, is to actually _suspend and release your threads as it is waiting for IO data_.
This _significantly_ increases your application in regards to scalability, and how many simultaneous users it
can handle, before your web server, and/or operating system, literally crashes. This is referred to as _"async programming"_,
and is a core feature in any modern framework, and/or programming language, allowing your code to scale a _lot_
better.

What this implies for Hyperlambda specifically, is that after all 3 threads above are created, and we're
waiting for IO traffic from our URLs, there is actually _zero_ threads being consumed by our application,
since all 3 threads are suspended, released back to the thread pool, and only when the network driver
has data to the specific **[http.get]** invocation, the thread is _"re-animated"_, brought back to life,
given a thread to continue execution, and continues its execution.

From a scalability perspective, this results in that an async application is typically several orders of
magnitudes better at scaling than a synchronous application. However, since async programming is extremely
complex, a lot of things can go wrong as you try to implement it in your own code. Hyperlambda though
is _async by default_, and there is no _"special syntax"_ required to understand these parts of it.

## Synchronizing lambda objects

Sometimes you need synchronized access to some shared resource. This can for instance be a file or some
other resource, that is shared amongst multiple threads. For these times you've got the **[semaphore]**
slot. The semaphore slot takes on argument, in addition to a lambda object, ensuring that only _one_
thread given the same name is able to execute its lambda object at the same time. To understand this
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
basically ensures that only _one_ HTTP GET invocation is able to execute at the same time. Basically, the
first thread to execute the semaphore slot, becomes the first thread allowed to execute its HTTP GET invocation,
while the other 2 threads needs to wait for the first thread to finish before they're allowed access to their
lambda object.

The above example is not a very good example though, since none of the above threads actually _need_ a
semaphor, but simply given to allow you to measure the differences in execution speed for the lambda object as
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

Without the above **[semaphore]** invocations, we'd run the risk of multiple threads writing to the
file simultaneously, resulting in what is commonly referred to as a _"race condition"_.

Now compare the above code with the equivalent C# or Java example, and you'll rapidly understand
the beauty of the simplified syntax.

## Wrapping up

In this article we walked through some of the threading, async, and scalability features of Magic and Hyperlambda,
to show how Magic simplifies multithreaded programming, and also scales very well due to its async nature.

* [Documentation](/documentation/)
