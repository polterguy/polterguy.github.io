---
title: "The [where] argument"
description: "The [where] argument - This argument is common for [sql.update], [sql.delete], and [sql.read], in addition to that a [join] will also be logically parsed much the same way as a [where] argument."
generated: true
---

This page is part of the [magic.data.common](/plugins/magic.data.common/) documentation.

This argument is common for **[sql.update]**, **[sql.delete]**, and **[sql.read]**, in addition
to that a **[join]** will also be logically parsed much the same way as a **[where]** argument. The where
argument follows a recursive structure, allowing you to supply multiple layers of `where` criteria,
being applied recursively, using some sort of comparison operator, applied to all conditions in the
same level. Its most basic usage is as follows.

```
sql.read
   table:table1
   limit:-1
   where

      and
         field1:howdy
```

The above would result in the following result.

```
sql.read:select * from 'table1' where 'field1' = @0
   @0:howdy
```

To apply multiple **[and]** criteria, you can simply add them consecutively as follows.

```
sql.read
   table:table1
   limit:-1
   where

      and
         field1:howdy
         field2:world
```

The above results in the following.

```
sql.read:select * from 'table1' where 'field1' = @0 and 'field2' = @1
   @0:howdy
   @1:world
```

If you exchange the above **[and]** with **[or]**, the system will use the `or` operator to
separate your arguments, such as the following illustrates.

```
sql.read
   table:table1
   limit:-1
   where

      or
         field1:howdy
         field2:world
```

The above results in the following result.

```
sql.read:select * from 'table1' where 'field1' = @0 or 'field2' = @1
    @0:howdy
    @1:world
```

You can also nest operators, producing parenthesis, and create complex conditions, such as the following
illustrates.

```
sql.read
   table:table1
   limit:-1
   where

      or
         field1:howdy

         and
            field2:world
            field3:dudes
```

Which results in the following.

```
sql.read:select * from 'table1' where 'field1' = @0 or ('field2' = @1 and 'field3' = @2)
   @0:howdy
   @1:world
   @2:dudes
```

The parent of a list of criteria is deciding which logical operator to separate your conditions
with, contrary to traditional languages, where you separate your conditions with the logical operator, and
explicitly add parenthesis to group your levels. This might seem a little bit weird in the beginning,
but this is a general rule with everything in Hyperlambda, and after a while will feel more natural than
the alternative. The reasons for this is to allow for semantically traversing your lambda objects, allowing
the computer to logically understand what it does more easily - Among other things. Think of the boolean
logical parts of your SQL slots as _"grouping your comparisons"_ or a _"logical function invocation"_ if it helps.

---

[&larr; 'Namespacing' columns](/plugins/magic.data.common/namespacing-columns/) | [all of magic.data.common](/plugins/magic.data.common/) | [Comparison operators &rarr;](/plugins/magic.data.common/comparison-operators/)
