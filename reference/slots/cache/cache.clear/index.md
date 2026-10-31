---
title: "[cache.clear]"
description: "cache.clear is a slot in the cache namespace of Magic Cloud. Clears cached items matching the optional filter."
generated: true
llms: false
slot_json: "/reference/slots/cache/cache.clear/slot.json"
---

`cache.clear` is a slot in the `cache` namespace, in Hyperlambda, the language of Magic Cloud. Clears cached items matching the optional filter.

* **Value** (`cache-key`), optional: Optional filter for cache keys

Guide: [How to use [cache.clear]](/plugins/magic.lambda.caching/#how-to-use-cacheclear)

### JSON declaration

This is the complete declaration of `cache.clear`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "cache.clear",
  "description": "Clears cached items matching the optional filter",
  "signature": {
    "input": {
      "kind": "cache-key",
      "description": "Optional filter for cache keys",
      "required": false,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[all `cache.*` slots](/reference/slots/cache/) | [`cache.count` &rarr;](/reference/slots/cache/cache.count/)

