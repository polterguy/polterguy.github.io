---
title: "[cache.list]"
description: "cache.list is a slot in the cache namespace of Magic Cloud. Lists cached keys matching the optional filter."
generated: true
llms: false
slot_json: "/reference/slots/cache/cache.list/slot.json"
---

`cache.list` is a slot in the `cache` namespace, in Hyperlambda, the language of Magic Cloud. Lists cached keys matching the optional filter.

* **Value** (`cache-key`), optional: Optional filter for cache keys
* **Returns**: Returns one child node per cached key matching the optional filter, each with [key] and [value] children

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[offset]` | int | no | Result offset. Default: `0`. |
| `[limit]` | int | no | Maximum number of items to return. Default: `10`. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One cached item; children carry the cache [key] and stored [value]. Can be repeated. |
| _unnamed child node_ / `[key]` | string | no | Cached item key. |
| _unnamed child node_ / `[value]` | string | no | Cached item value. |

Guide: [How to use [cache.list]](/plugins/magic.lambda.caching/#how-to-use-cachelist)

### JSON declaration

This is the complete declaration of `cache.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "cache.list",
  "description": "Lists cached keys matching the optional filter",
  "signature": {
    "input": {
      "kind": "cache-key",
      "description": "Optional filter for cache keys",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "offset": {
        "type": "int",
        "description": "Result offset",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "limit": {
        "type": "int",
        "description": "Maximum number of items to return",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "10",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "cache-key-list,node-list",
      "element-kind": "cache-entry,lambda-tree",
      "description": "Returns one child node per cached key matching the optional filter, each with [key] and [value] children",
      "children": [
        {
          "type": "lambda",
          "kind": "cache-entry",
          "description": "One cached item; children carry the cache [key] and stored [value]",
          "required": false,
          "mode": "Value",
          "cardinality": "ZeroOrMore",
          "role": "StructuredObject",
          "projection": "StructuredTree",
          "children": {
            "key": {
              "type": "string",
              "kind": "cache-key",
              "description": "Cached item key",
              "required": false,
              "mode": "Value",
              "cardinality": "ExactlyOne",
              "role": "Option",
              "projection": "Value"
            },
            "value": {
              "type": "string",
              "kind": "cache-value",
              "description": "Cached item value",
              "required": false,
              "mode": "Value",
              "cardinality": "ExactlyOne",
              "role": "Option",
              "projection": "Value"
            }
          }
        }
      ]
    }
  }
}
```

</details>

---

[&larr; `cache.get`](/reference/slots/cache/cache.get/) | [all `cache.*` slots](/reference/slots/cache/) | [`cache.set` &rarr;](/reference/slots/cache/cache.set/)

