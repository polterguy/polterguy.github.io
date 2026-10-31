---
title: "How to use [convert]"
description: "How to use [convert] - This slot converts the value of an expression from its original type, to whatever [type] declaration you supply as its argument."
generated: true
guide: true
---

The reference page of [`convert`](/reference/slots/core/convert/) has its arguments, constraints and declaration.

This slot converts the value of an expression from its original type, to whatever **[type]** declaration you
supply as its argument.

```
.foo:57
convert:x:-
   type:int
```

**Notice** - You can also base64 encode and decode `byte[]` with this slot, by passing in _"base64"_ or
_"from-base64"_ as your **[type]** argument. The value of the object you want to convert must obviously support
conversion to the specified type, and will throw an exception if no conversion is possible, such as if you
for instance try to convert the string of _"foo-bar"_ to an integer.
