---
title: "[sqlite.backup]"
description: "sqlite.backup is a slot in the sqlite namespace of Magic Cloud. Creates a backup of the current SQLite connection."
generated: true
llms: "guide"
slot_json: "/reference/slots/sqlite/sqlite.backup/slot.json"
---

`sqlite.backup` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Creates a backup of the current SQLite connection.

* **Value** (`file-path`), required: Target SQLite database filename under files/data/
* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

### Guide

<!-- guide -->
To create a backup of the database called for instance _"foo"_, you would use code resembling the following.

```
sqlite.connect:[generic|foo]
   sqlite.backup:foo.backup
```

The above will create a backup of your foo database and store it at _"/data/foo.backup"_, allowing you to restore it if
it for some reasons becomes invalid.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.sqlite](/plugins/magic.lambda.sqlite/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `sqlite.backup`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.backup",
  "description": "Creates a backup of the current SQLite connection",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "Target SQLite database filename under files/data/",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "scope": {
      "requires": "sqlite.connection",
      "description": "Requires an open SQLite connection created by [sqlite.connect]"
    }
  }
}
```

</details>

---

[all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.connect` &rarr;](/reference/slots/sqlite/sqlite.connect/)

