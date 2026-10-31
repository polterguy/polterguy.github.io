---
title: "[sqlite.load-extension]"
description: "sqlite.load-extension is a slot in the sqlite namespace of Magic Cloud. Loads a SQLite extension into the current connection from child-node arguments."
generated: true
llms: false
slot_json: "/reference/slots/sqlite/sqlite.load-extension/slot.json"
---

`sqlite.load-extension` is a slot in the `sqlite` namespace, in Hyperlambda, the language of Magic Cloud. Loads a SQLite extension into the current connection from child-node arguments.

* **Scope**: requires `sqlite.connection` - Requires an open SQLite connection created by [sqlite.connect]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[file]` | string | yes | SQLite extension filename. |
| `[proc]` | string | no | Optional extension entry point. |
| `[append-platform]` | bool | no | Whether to append the current platform suffix. Default: `true`. |

### Guide

[How to use `sqlite.load-extension`](/plugins/magic.lambda.sqlite/sqlite.load-extension/)

### JSON declaration

This is the complete declaration of `sqlite.load-extension`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sqlite.load-extension",
  "description": "Loads a SQLite extension into the current connection from child-node arguments",
  "signature": {
    "children": {
      "file": {
        "type": "string",
        "kind": "sqlite-extension-file",
        "description": "SQLite extension filename",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "proc": {
        "type": "string",
        "kind": "sqlite-entry-point",
        "description": "Optional extension entry point",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "append-platform": {
        "type": "bool",
        "description": "Whether to append the current platform suffix",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true",
        "role": "Option",
        "projection": "Value"
      }
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

[&larr; `sqlite.execute`](/reference/slots/sqlite/sqlite.execute/) | [all `sqlite.*` slots](/reference/slots/sqlite/) | [`sqlite.read` &rarr;](/reference/slots/sqlite/sqlite.read/)

