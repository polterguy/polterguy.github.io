---
title: "Differences between [join] and [where]"
description: "Differences between [join] and [where] - There is one crucial semantic difference between a [join] condition and a [where] condition, which is that the library assumes a join is always between two columns, while a whe..."
generated: true
---

This page is part of the [magic.data.common](/plugins/magic.data.common/) documentation.

There is one crucial semantic difference between a **[\[join\]](/reference/slots/core/join/)** condition and a **[where]** condition, which is
that the library assumes a join is _always_ between two columns, while a where always assume you're _always_
comparing against a static value. This implies that you _cannot_ add static values into your SQL as a part of
your **[\[join\]](/reference/slots/core/join/)** condition, while the opposite is true for a **[where]**.

Although this technically doesn't allow you to create any SQL you want to create, it is still more
in _"the spirit"_ of SQL as a standard - And you can always add your static conditions into your **[where]**
parts, while adding your table comparisons into your **[\[join\]](/reference/slots/core/join/)** conditions. This allows you to create
any _result_ you want to achieve, although technically not any _SQL_ you want to have.

## Explicit arguments declarations for joins

Normally you don't need to worry about this, but sometimes you need to explicitly add an argument to
your CRUD slot invocations if it has a `join` part, and you want one of your
conditions for your join to be a static value of some sort, and not a comparison to your right hand side
table column. This can be accomplished with something such as the following.

```
sql.read
   generate:true
   table:foo
      join:bar
         on
            and
               foo.field1:bar.field2
               foo.field2:@static-value
   @static-value:static value
```

Notice the above **[@static-value]** parts, which becomes a normal argument, instead of trying to join
two fields on two table. The above results in the following lambda being generated.

```
data.read:select * from `foo` inner join `bar` on `foo`.`field1` = `bar`.`field2` and `foo`.`field2` = @static-value limit 25
   @static-value:static value
```

As you can see in the above result, the `@static-value` becomes a *statically* declared condition to your join,
and not assumed to be a reference to a field in your right hand side joined table. This is one of those edge cases
you normally rarely need, but might be useful on rare occasions. The reasons why this works is because the RHS side
of your join condition starts with an `@` character, which assumes you are referencing an argument and not a field
in your joined table. This only has effects on your **[\[join\]](/reference/slots/core/join/)** parts, implying **[xxx.read]** slot invocations,
since these are the only slots supporting joins.
The above is the only exception that allows you to join on static values and not column names. However, as a general
rule of thumb, we encourage users to **[\[join\]](/reference/slots/core/join/)** on table columns and add static values into your **[where]** conditions.

---

[&larr; Joins](/plugins/magic.data.common/joins/) | [all of magic.data.common](/plugins/magic.data.common/) | ['Namespacing' columns &rarr;](/plugins/magic.data.common/namespacing-columns/)
