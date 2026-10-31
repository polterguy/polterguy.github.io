---
title: "How to use [sockets.connection.leave-group]"
description: "How to use [sockets.connection.leave-group] - From within your Hyperlambda files executed by invoking the execute method, you have access to your SignalR connectionId as a context object named \"sockets.connection\"."
generated: true
guide: true
---

The reference page of [`sockets.connection.leave-group`](/reference/slots/sockets/sockets.connection.leave-group/) has its arguments, constraints and declaration.

From within your Hyperlambda files executed by invoking the `execute` method, you have access to
your SignalR connectionId as a context object named _"sockets.connection"_. Below is an example of
how to retrieve the current SignalR connectionId. Notice, this only works from _within_ a socket executed
Hyperlambda file, implying only if you're executing the file using the `execute` method, through your
SignalR socket connection.

```
get-context:sockets.connection
```

This might sometimes be useful, especially if you want to dynamically add only _one_ connection to a group
for instance. To add the currently active connection explicitly to a group for instance, you can use the 
following slots.

* __[sockets.connection.enter-group]__ - Associates the current connection _only_ with the specified group
* __[sockets.connection.leave-group]__ - De-associates the current connection with the specified group

If the user has additional connections, none of the other connections will be modified in any ways. Also
realise that both of these slots can _only_ be used from within a Hyperlambda file executed through a
SignalR socket connection somehow. Below is an example.

```
// Retrieving connectionId
get-context:sockets.connection

// Entering group
sockets.connection.enter-group:x:@get-context
   group:foo-bar-group

// Do stuff here that requires the user to belong to group ...

// Leaving group
sockets.connection.leave-group:x:@get-context
   group:foo-bar-group
```
