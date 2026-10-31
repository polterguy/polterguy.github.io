---
title: "How to use [system.execute]"
description: "How to use [system.execute] - If you only want to execute a specific program in your system you can use [system.execute], and pass in the name of the command as a value."
generated: true
guide: true
---

This is the guide to [`system.execute`](/reference/slots/system/system.execute/), whose reference page has its arguments, constraints and declaration.

If you only want to execute a specific program in your system you can use **[system.execute]**, and pass in
the name of the command as a value. Arguments can be passed either as a single **[args]** string node,
or as children of **[args]**, one argument per child node. You can also
optionally specify **[working-directory]**.

```
system.execute:ls
   args:"-l"
```

Passing arguments as a list.

```
system.execute:python3
   args
      .:-c
      .:"print('hello')"
```

To specify a working directory.

```
system.execute:ls
   args:"-l"
   working-directory:"/"
```

**Notice** - The slot returns stdout as a string, and throws an exception on non-zero exit code, using
stderr if present.
