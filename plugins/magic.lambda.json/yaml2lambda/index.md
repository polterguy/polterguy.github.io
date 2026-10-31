---
title: "How to use [yaml2lambda]"
description: "How to use [yaml2lambda] - The [yaml2lambda] slot converts a YAML input string to a lambda object."
generated: true
guide: true
---

This is the guide to [`yaml2lambda`](/reference/slots/core/yaml2lambda/), whose reference page has its arguments, constraints and declaration.

The **[yaml2lambda]** slot converts a YAML input string to a lambda object. Since YAML arguably is just another representation of
JSON, these slot have been added to this project. Notice, the same constraints applies for YAML as does for JSON, implying
a YAML string can always be converted to a lambda object, but the opposite is not necessary true. Basic usage is as follows.

```
.yaml:@"
foo: howdy
bar: jo
howdy: !!bool true
children:
- howdy
- some
"
yaml2lambda:x:@.yaml
lambda2yaml:x:-/*
```

The above will result in the following.

```
yaml2lambda
   foo:howdy
   bar:jo
   howdy:bool:true
   children
      .:howdy
      .:some
lambda2yaml: /* ... YAML content ... */
```

Internally the **[yaml2lambda]** slot first converts the input YAML to JSON, for then to use the **[json2lambda]**
logic, ensuring the exact same result, regardless of whether or not you start out with JSON or YAML.
