---
title: "[pgsql.transaction.commit]"
description: "pgsql.transaction.commit is a slot in the pgsql namespace of Magic Cloud. Commits the current PostgreSQL transaction."
generated: true
llms: false
slot_json: "/reference/slots/pgsql/pgsql.transaction.commit/slot.json"
---

`pgsql.transaction.commit` is a slot in the `pgsql` namespace, in Hyperlambda, the language of Magic Cloud. Commits the current PostgreSQL transaction.

* **Scope**: requires `pgsql.transaction` - Requires an active PostgreSQL transaction created by [pgsql.transaction.create]

### Guide

[How to use `pgsql.transaction.commit`](/plugins/magic.lambda.pgsql/pgsql.transaction.commit/)

### JSON declaration

This is the complete declaration of `pgsql.transaction.commit`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "pgsql.transaction.commit",
  "description": "Commits the current PostgreSQL transaction",
  "signature": {
    "scope": {
      "requires": "pgsql.transaction",
      "description": "Requires an active PostgreSQL transaction created by [pgsql.transaction.create]"
    }
  }
}
```

</details>

---

[&larr; `pgsql.select`](/reference/slots/pgsql/pgsql.select/) | [all `pgsql.*` slots](/reference/slots/pgsql/) | [`pgsql.transaction.create` &rarr;](/reference/slots/pgsql/pgsql.transaction.create/)

