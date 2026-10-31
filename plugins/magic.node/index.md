---
title: magic.node
moved_anchors: {"extending-lambda-expressionsiterators": "/plugins/magic.node/lambda-expressions/#extending-lambda-expressionsiterators", "extending-the-hyperlambda-type-system": "/plugins/magic.node/hyperlambda-types/#extending-the-hyperlambda-type-system", "hyperlambda-types": "/plugins/magic.node/hyperlambda-types/", "iterators-in-lambda-expressions": "/plugins/magic.node/lambda-expressions/#iterators-in-lambda-expressions", "lambda-expressions": "/plugins/magic.node/lambda-expressions/", "parsing-hyperlambda-from-c": "/plugins/magic.node/lambda-expressions/#parsing-hyperlambda-from-c"}
---

magic.node is a simple name/value/children graph object, in addition to a _"Hyperlambda"_ parser, allowing you to
create a textual string representations of graph objects easily transformed to its relational graph object syntax
and vice versa. This allows you to declaratively create _"execution trees"_ using a format similar to YAML, for 
then to access each individual node, its value, name and children from your C#, CLR code, or Hyperlambda.

Hyperlambda is perfect for creating a highly humanly readable relational configuration format, or smaller
DSL engines, especially when combined with magic.signals and magic.lambda. Below is a small
example of Hyperlambda to give you an idea of how it looks like.

```
foo:bar
foo:int:5
foo
   child1:its-value
   child2:its-value
```

3 spaces (SP) opens up the children collection of a node, and allows you to create children associated with
some other node. In the example above, the **[child1]** and the **[child2]** nodes, have **[foo]** as their
parent. A colon `:` separates the name and the value of the node - The name is to the left of the colon, and
the value to the right.
You can optionally supply a type between a node's name and its value, which you can see above where we add
the `:int:` parts between one of our **[foo]** nodes' name and value. If you don't explicitly declare a type
`string` will be assumed.


## Traversing Hyperlambda from C#

To traverse the nodes later in for instance C#, you could do something such as the following.

```csharp
var root = HyperlambdaParser.Parse(hyperlambda);

foreach (var idxChild in root.Children)
{
   var name = idxChild.Name;
   var value = idxChild.Value;
   /* ... etc ... */
}
```

**Notice** - When you parse Hyperlambda a _"root node"_ is explicitly created wrapping all your nodes, and
this is the node that's returned to you after parsing. All nodes you declare in your Hyperlambda will be
returned to you as children of this root node.


## String literals in Hyperlambda

Hyperlambda also supports strings the same way C# supports strings, using any of the following string representations.

```
// Single quotes
.foo:'howdy world this is a string'

// Double quotes
.foo:"Howdy world, another string"

// Multiline strings
.foo:@"Notice how the new line doesn't end the string
    here!"
```

Escape characters are supported for both single quote and double quote strings the same way they
are supported in C#, allowing you to use e.g. `\r\n` etc.


## Documenting nodes, arguments to slots, etc

When referencing nodes in the documentation for Magic, it is common to reference them like __[this]__, where
_"this"_ would be the name of some node - Implying in __bold__ characters, wrapped by square [brackets].



## Topics

* [Hyperlambda types](/plugins/magic.node/hyperlambda-types/) - Although the node structure itself can hold any value type you need inside of its Value property, Hyperlambda only supports serialising the following types by default.
* [Lambda expressions](/plugins/magic.node/lambda-expressions/) - Lambda expressions are kind of like XPath expressions, except they will reference nodes in your Node graph object instead of XML nodes.
