---
title: "How to use [magic.db.mysql.indexes]"
description: "How to use [magic.db.mysql.indexes] - This slot returns all indexes for the specified [connection-string]/[database]/[table] combination."
guide: true
slots: ["magic.db.mysql.indexes"]
---

This slot returns all indexes for the specified **[connection-string]**/**[database]**/**[table]** combination.
Below is example usage.

```
signal:magic.db.mysql.indexes
   connection-string:generic
   database:magic
   table:users_roles
```

The above would return all indexes in your _"users\_roles"_ table.
