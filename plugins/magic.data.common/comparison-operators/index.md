---
title: "Comparison operators"
description: "Comparison operators - The project supports the following comparison operators."
generated: true
---

This page is part of the [magic.data.common](/plugins/magic.data.common/) documentation.

## Comparison operators

The project supports the following comparison operators.

* `eq` - Equality comparison, equivalent to `=`
* `neq` - Not equality comparison, equivalent to `!=`
* `mt` - More than comparison, equivalent to `>`
* `lt` - Less than comparison, equivalent to `<`
* `lteq` - Less than or equal comparison, equivalent to `<=`
* `mteq` - More than or equal comparison, equivalent to `>=`
* `like` - Like comparison, equivalent to SQL's `like` comparison
* `in` - Special comparison operator, since it requires a _list_ of values, generating an _"in"_ SQL condition

Everywhere you need to compare one field with another, such as in **[where]** or **[join]**
arguments, you can append a comparison operator to your left hand side column, such as the following
illustrates.

```
sql.read
   table:foo
   where

      and
         field1.neq:xxx
```

Notice the **.neq** parts above, and realise how the above will produce the following SQL.

```sql
select * from 'foo' where 'field1' != @0
```

The above **[field1.neq]** is substituted by the SQL generator to become a `!=` comparison operator
on the `field1` column versus the `xxx` argument. The comparison operator is *always* expected to be the
last parts of your _"LHS"_ (Left Hand Side) parts of your criteria - Implying the *name* of the node.


## The [in] comparison operator

This operator is special, in that it doesn't require the caller to supply _one_ value, but rather a _list_ of values,
from where the column you compare towards must have a value matching at least _one_ of these values. An example can
be found below.

```
sql.read
   table:table1
   where

      and
         table1.field1.in
            :long:5
            :long:7
            :long:9
```

The above will generate the following SQL, in addition to returning 3 parameters to the caller.

```sql
select * from 'table1' where 'table1'.'field1' in (@0,@1,@2) limit 25
```


## Escaping characters

If you by some freak accident happen to have a column in one of your tables that is named for instance `neq`,
you can escape your column name, by prepending a `\` to it. See an example below.

```
sql.read
   table:table1
   where

      and
         table1.\neq:foo
```

Notice how the `\` character above results in the following SQL.

```sql
select * from 'table1' where 'table1'.'neq' = @0 limit 25
```

As you can see, the `\neq` is interpreted as a column name, and not a `neq` operator, and since the equality operator
is the default selected if no operator is supplied, the comparison operator becomes `=`.

You can also escape columns entirely, if you for instance have a column that contains a `.` in its name,
such as we illustrate below.

```
sql.read
   table:table1
   where

      and
         \foo.bar:bar
```

Notice how the above lambda will interpret the `foo.bar` parts as a column name, and not as
column _"bar"_ on _"foo"_. You can see the resulting SQL below.

```sql
select * from 'table1' where 'foo.bar' = @0 limit 25
```


## Extension comparison operators

You can also extend the existing comparison operators with your own, such as for instance having `ltmt`
resulting in `<>`, etc. To do this, you'll have to register your comparison operator using the static
`AddComparisonOperator` method on the `SqlWhereBuilder` class. Below is an example.

```
SqlWhereBuilder.AddComparisonOperator("ltmt", (builder, args, colNode, escapeChar) => {
    builder.Append(" <> ");
    SqlWhereBuilder.AppendArgs(args, colNode, builder, escapeChar);
});
```

The above will give you access to use `ltmt` as a comparison operator, resolving to `<>` in your SQL.


## magic.data.common and meta data

One of the really nice things about this semantic approach to generating SQL is that it
allows you to retrieve meta data from your Hyperlambda snippets, asking questions such as for instance
_"find all files that somehow selects columns from the 'xxx' table"_ - And for that matter, even
dynamically change the table name, using semantic refactoring and replacement concepts. Once you've
crossed the initial step into _meta data traversal_ in Hyperlambda, things like this becomes
second hand nature with Hyperlambda.

---

[&larr; The [where] argument](/plugins/magic.data.common/the-where-argument/) | [all of magic.data.common](/plugins/magic.data.common/)
