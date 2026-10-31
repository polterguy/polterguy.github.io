---
title: "How to use [magic.db.mysql.databases]"
description: "How to use [magic.db.mysql.databases] - This slot returns all databases the system has access to within the specified connection string."
guide: true
slots: ["magic.db.mysql.databases"]
---

This slot returns all databases the system has access to within the specified connection string. Example
usage can be found below.

```
signal:magic.db.mysql.databases
   connection-string:generic
```

The above would result in a list of databases resembling the following.

```
signal
   ""
      db:information_schema
   ""
      db:magic
   ""
      db:mysql
   ""
      db:performance_schema
   ""
      db:sys
```
