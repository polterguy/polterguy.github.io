---
title: "How to use [sql.update]"
description: "How to use [sql.update] - This slot allows you to update one or more records, in a specified [table]."
generated: true
guide: true
---

This is the guide to [`sql.update`](/reference/slots/sql/sql.update/), whose reference page has its arguments, constraints and declaration.

This slot allows you to update one or more records, in a specified **[table]**. Just like create, it requires
one mandatory argument, being **[values]**, implying columns/values you wish to update. This slot also takes
an optional **[where]** argument, which is described further down in this document. Its simplest version can be
imagined as follows.

```
sql.update
   table:table1
   values
      field1:howdy
```

The above of course will result in the following.

```sql
sql.update:update 'table1' set 'field1' = @v0
   @v0:howdy
```

**Notice**, if you don't apply a **[where]** argument, then *all* records in your table will
be updated - Which is highly unlikely what your intentions are. Hence, make sure you apply a
**[where]** argument as you invoke this slot.
