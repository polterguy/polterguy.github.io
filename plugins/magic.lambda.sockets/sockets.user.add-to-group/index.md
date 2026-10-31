---
title: "How to use [sockets.user.add-to-group]"
description: "How to use [sockets.user.add-to-group] - You can associate a user with one or more groups."
generated: true
guide: true
---

The reference page of [`sockets.user.add-to-group`](/reference/slots/sockets/sockets.user.add-to-group/) has its arguments, constraints and declaration.

You can associate a user with one or more groups. This is done with the following slots.

* __[sockets.user.add-to-group]__ - Adds the specified user to the specified group
* __[sockets.user.remove-from-group]__ - Removes the specified user from the specified group

Below you can find an example of how to add a user to a group, for then to later de-associate
the user with the group.

```
// Associating a user with a group.
sockets.user.add-to-group:some-username-here
   group:some-group-name-here

// Publishing message, now to group, such that 'some-username-here' gets it
sockets.signal:foo.bar
   group:some-group-name-here
   args
      howdy:world

// De-associating the user with the group again.
sockets.user.remove-from-group:some-username-here
   group:some-group-name-here
```

**Notice** - SignalR users might have multiple connections. This implies that once you add a user to
a group, _all_ connections are associated with that group. The message will only be
published to connections explicitly having registered an interest in the `foo.bar` message for our
above example, irrelevant of whether the user belongs to the group or not.
