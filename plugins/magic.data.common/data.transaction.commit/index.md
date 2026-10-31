---
title: "How to use [data.transaction.commit]"
description: "How to use [data.transaction.commit] - Although you should be careful with database transactions, sometimes you really need them."
generated: true
guide: true
---

The reference page of [`data.transaction.commit`](/reference/slots/data/data.transaction.commit/) has its arguments, constraints and declaration.

Although you should be careful with database transactions, sometimes you _really_ need them. For those cases you
can use the following 3 slots to create, rollback, and/or commit transactions towards your underlying database.

* __[data.transaction.create]__ - Creates a new database transaction
* __[data.transaction.commit]__ - Commits an existing open transaction
* __[data.transaction.rollback]__ - Roll back an existing open transaction

**Notice** - The default logic for a database transaction, is that unless it's _explicitly committed_
before leaving scope, it will roll back by default. Below is an example of a transaction that will
rollback, since it's not explicitly committed before leaving scope.

```
data.connect:sakila
   data.transaction.create
      data.execute:delete from film_actor

      /*
       * If you uncomment the line below the
       * transaction will be committed, resulting
       * in that everything from your film_actor
       * table will be deleted.
       */
      //data.transaction.commit

data.connect:sakila

   /*
    * Notice, this still returns 5462 items, since
    * transaction was implicitly rolled back above.
    */
   data.scalar:select count(*) from film_actor
```

A transaction typically follows your connection, implying to count items
after the transaction has been rolled back, we'll need a _new_ connection, as the
above example illustrates.
