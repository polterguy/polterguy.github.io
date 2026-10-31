---
title: "How to use [sockets.signal]"
description: "How to use [sockets.signal] - In addition to the above, you can explicitly publish SignalR events by signaling the [sockets.signal] slot, which will automatically transform the specified children [args] nodes to JSON,..."
generated: true
guide: true
---

The reference page of [`sockets.signal`](/reference/slots/sockets/sockets.signal/) has its arguments, constraints and declaration.

In addition to the above, you can explicitly publish SignalR events by signaling the **[sockets.signal]** slot,
which will automatically transform the specified children **[args]** nodes to JSON, and invoke the specified
method for all connections somehow subscribing to the specified method - Allowing you to filter according
to groups, users and roles if you wish. Below is an example.

```
sockets.signal:foo.bar
   roles:root, admin
   args
      howdy:world
```

The above will invoke the `foo.bar` method, passing in `{"howdy":"world"}` as a JSON string, but only users belonging
to the roles of either `admin` or `root` will be notified. Both the **[roles]** and the **[args]** arguments are optional.
To subscribe to the above invocation, you could use something such as the following in TypeScript.

```typescript
this.connection.on('foo.bar', (args: string) => {
  console.log(JSON.parse(args));
});
```

You can also signal a list of specified users, such as the following illustrates.

```
sockets.signal:foo.bar
   users:user1, user2, user3
   args
      howdy:world
```

In addition to that you can signal a list of specified groups, such as the following illustrates.

```
sockets.signal:foo.bar
   groups:group1, group2, group3
   args
      howdy:world
```

Finally, you can signal a list of specified client connections, such as the following illustrates.

```
sockets.signal:foo.bar
   clients:e6U2Zz6kqHDCEVyEX6v35w, 5uWWytAM8kJ2gfIL0fEw2A
   args
      howdy:world
```

The above will only signal the two specified client connections.

**Notice** - If you signal a group or a list of groups, you'll have to add your users to the group before
you do.
