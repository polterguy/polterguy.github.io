
# Hyperlambda as a Turing complete programming language

Threading in software development implies doing multiple things concurrently, scheduling CPU time for each
of your threads, according to how the operating system schedules your threads. This concept is often referred
to as _"multi tasking"_ and is crucial for any modern operating system, and/or programming language. Hyperlambda
contains several multi tasking related slots.

## [fork]

Forks the given lambda into a new thread of execution, using a thread from the thread pool. This
slot is useful for creating _"fire and forget"_ lambda objects, where you don't need to wait
for the result of the execution before continuing executing the current scope.

```
fork
   info.log:I was invoked from another thread
```

To understand how **[fork]** works, you can imagine your computer's CPU as a single river,
running down hill, and at some point the river divides into two equally large rivers. This is
referred to as _"a fork"_. The analogy of the river becomes important for another reason, which
is the understanding of that the total amount of water is still the same, it's only parted
into two smaller rivers - Implying you cannot _"do more"_ with multi tasking, you can only
equally share the same amount of resources as you had before between two different tasks.
Multi threading does not make your CPU faster, it only schedules your CPU's time on multiple
things, doing these things concurrently.

## [join]

Joins all child **[fork]** invocations, implying the slot will wait until all forks directly below it
has finished executing, and automatically copy the result of the **[fork]** into the original node.

```
join
   fork
      http.get:"https://servergardens.com"
   fork
      http.get:"https://gaiasoul.com"
```

As an analogy for what occurs above, imagine the two rivers from our above **[fork]** analogy,
that forked from one larger river into two smaller rivers, for then again to join up and becoming one
large river again.

## [semaphore]

Creates a named semaphore, where only one thread will be allowed to evaluate the same semaphore at
the same time. Notice, the semaphore to use is defined through its value, implying you can use the same
semaphore multiple places, by using the same value of your **[semaphore]** invocation.

```
semaphore:foo-bar
   /*
    * Only one thread will be allowed entrance into this piece of
    * code at the same time, ensuring synchronized access, for cases
    * where you cannot allow more than one thread to enter at the
    * same time.
    */
```

In the above semaphore _"foo-bar_" becomes the name of your semaphore. If you invoke **[semaphore]** in
any other parts of your Hyperlambda code, with _"foo-bar"_ as the value, only _one_ of your
lambda objects will be allowed to execute at the same time. This allows you to _"synchronize access"_
to shared resources, where only _one_ thread should be allowed to access the shared resource at the same
time. Such shared resources might be for instance files, or other things shared between multiuple threads,
where it's crucial that only one thread is allowed to access the shared resource at the same time.

## [sleep]

This slot will sleep the current thread for x number of milliseconds, where x is an integer value, expected
to be passed in as its main value.

```
// Sleeps the main thread for 1 second, or 1000 milliseconds.
sleep:1000
```

**Notice** - This slot is typically releasing the thread back to the operating system, implying as
the current thread is _"sleeping"_, it will not be a blocking call, and require ZERO physical operating
system threads while it is sleeping. This is true because of Hyperlambda's 100% perfectly `async` nature.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.threading](https://github.com/polterguy/magic.lambda.threading), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.threading/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.threading)
