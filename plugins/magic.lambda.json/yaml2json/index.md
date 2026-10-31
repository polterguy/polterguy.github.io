---
title: "How to use [yaml2json]"
description: "How to use [yaml2json] - The [yaml2json] slot converts the specified YAML input string to a JSON string."
generated: true
guide: true
---

The reference page of [`yaml2json`](/reference/slots/core/yaml2json/) has its arguments, constraints and declaration.

The **[yaml2json]** slot converts the specified YAML input string to a JSON string. Basic usage is as follows.

```
.yaml:@"foo: howdy
bar: jo
howdy: !!bool true
children:
- howdy
- some
"
yaml2json:x:@.yaml
json2yaml:x:-
```

The above results in the following.

```
{
  "foo": "howdy",
  "bar": "jo",
  "howdy": true,
  "children": [
    "howdy", "some"
  ]
}
```

Notice, the above have been formatted for brevity. The actual JSON result will _not_ be formatted, or having indentation to ensure
result is as compact as possible.
