---
title: "How to use [sqlite.backup]"
description: "How to use [sqlite.backup] - To create a backup of the database called for instance \"foo\", you would use code resembling the following."
generated: true
guide: true
---

The reference page of [`sqlite.backup`](/reference/slots/sqlite/sqlite.backup/) has its arguments, constraints and declaration.

To create a backup of the database called for instance _"foo"_, you would use code resembling the following.

```
sqlite.connect:[generic|foo]
   sqlite.backup:foo.backup
```

The above will create a backup of your foo database and store it at _"/data/foo.backup"_, allowing you to restore it if
it for some reasons becomes invalid.
