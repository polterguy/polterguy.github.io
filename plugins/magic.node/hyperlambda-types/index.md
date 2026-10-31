---
title: "Hyperlambda types"
description: "Hyperlambda types - Although the node structure itself can hold any value type you need inside of its Value property, Hyperlambda only supports serialising the following types by default."
generated: true
---

This page is part of the [magic.node](/plugins/magic.node/) documentation.

Although the node structure itself can hold any value type you need inside of its `Value` property,
Hyperlambda only supports serialising the following types by default.

* `string` = System.String
* `short` = System.Int16
* `ushort` = System.UInt16
* `int` = System.Int32
* `uint` = System.UInt32
* `long` = System.Int64
* `ulong` = System.UInt64
* `decimal` = System.Decimal
* `double` = System.Double
* `single` = System.Single
* `float` = System.Single - Alias for above
* `bool` = System.Boolean
* `date` = System.DateTime - _Always_ interpreted and serialized as UTC time!
* `time` = System.TimeSpan
* `guid` = System.Guid
* `char` = System.Char
* `byte` = System.Byte
* `sbyte` = System.SByte
* `x` = magic.node.extensions.Expression
* `node` = magic.node.Node

The type declaration should be declared in your Hyperlambda in between the name and its value, separated by colon (:).
The default type if omitted is `string` and strings do not need quotes or double quotes for this reason. An example
of declaring a couple of types associated with a node's value can be found below.

```
.foo1:int:5
.foo2:bool:true
.foo3:string:foo
.foo4:bar
```

## Extending the Hyperlambda type system

The type system is extendible, and you can easily create support for serializing your own types, by using
the `Converter.AddConverter` method, that can be found in the `magic.node.extensions` namespace.
Below is an example of how to extend the typing system, to allow for serializing and de-serializing instances
of a `Foo` class into Hyperlambda.

```csharp
/*
 * Class you want to serialize into Hyperlambda.
 */
class Foo
{
    public int Value1 { get; set; }
    public decimal Value2 { get; set; }
}

/*
 * Adding our converter functions, and associating them
 * with a type, and a Hyperlambda type name.
 */
Converter.AddConverter(
    typeof(Foo),
    "foo",
    (obj) => {
        var foo = obj as Foo;
        return ("foo", $"{foo.Value1}-{foo.Value2}");
    }, (obj) => {
        var str = (obj as string).Split('-');
        return new Foo
        {
            Value1 = int.Parse(str[0]),
            Value2 = decimal.Parse(str[1]),
        };
    });
```

The above will allow you to serialize instances of `Foo` into your Hyperlambda, and
de-serialize these instances once needed. An example of adding a `Foo` instance into
your Hyperlambda can be found below.

```
.foo:foo:5-7
```

Later you can retrieve your `Foo` instances in your slots, using something
resembling the following, and all parsing and conversion will be automatically
taken care of.

```
var foo = node.Get<Foo>();
```

---

[all of magic.node](/plugins/magic.node/) | [Lambda expressions &rarr;](/plugins/magic.node/lambda-expressions/)
