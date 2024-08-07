---
title: Hyperlambda
description: Hyperlambda is a relational file format allowing you to create execution trees, replacing XML as a dynamic markup language for declarative programming and Low-Code and No-Code workflow creation.
header:
  image: /assets/images/hyperlambda-wizard.webp
  image_description: Wizard flying through the air symbolizing the power of Hyperlambda
---

Hyperlambda is at the core of Magic. It's the primary axiom around which everything evolves. Technically it's _not_ a programming language, even though you can create anything in it that you can create in any other programming language. In its purest form, it's a relational file format, similar to XML and JSON, that allows you to declaratively create execution trees, that just so happens to allow for executing functionality.

Such execution trees can be automatically created by the machine itself to a much larger extent than traditional programming languages allows for, allowing the software developer to become more of an _"orchestrator"_ than an actual player. There's a reason we say the following about Magic Cloud.

> Where the Machine Creates the Code

Hyperlambda is implemented in C# and runs on .Net Core version 8, but you rarely have to consider this, unless you want to extend Hyperlambda with your own keywords, or use it as a DSL.

## Hyperlambda example

Below is an example Hyperlambda snippet to show you its syntax.

```
// Illustrates how to use a [for-each] loop to iterate some node-set.
.data
   item1:Hello from Item1
   item2:Hello from Item2
   item3:Hello from Item3
for-each:x:@.data/*
   log.info:x:@.dp/#
```

The above code _"declares"_ a `for-each` loop, that iterates through each of our **[.data]** node's children, and creates a log entry with its value as it iterates. The above invocation to **[for-each]** is referred to as a _"slot invocation"_, and the **[for-each]** slot is implemented in C#, specifically in the [magic.lambda](/plugins/magic.lambda/#how-to-use-for-each) project. Typically we refer to such slots in Magic's documentation using square brackets and bold text.

Hyperlambda contains slots for all the most important programming constructs, such as **[if]**, **[while]**, **[slots.create]**, **[execute-file]**, etc - Allowing you to use it as if it was a programing language, even though technically it's not. Most of these slots are declared in the project called _"magic.lambda"_ - But Magic actually contains almost 40 satellite projects, most of whom contains separate slots, that are somehow extending Magic with things such as database functions, file functions, etc.

* [See documentation for all plugins](/plugins/)
* [Read more about magic.lambda](/plugins/magic.lambda/)

## Hyperlambda structure

Hyperlambda is based upon nodes. Nodes have the following attributes.

* Name - Must be a string
* Value - Can be any object
* Children - Its children nodes

The name is separated from its value by a `:`, and children are found beneath a node, with 3 additional SP characters to _"scope"_ them as children of its above node. In the above example, our **[.data]** node has 3 children; **[item1]**, **[item2]**, and **[item3]**.

Contrary to JSON, Hyperlambda does _not_ require unique names. JSON maps to fields, which is a dictionary - While Hyperlambda nodes have a _list_ of children and is not using a dictionary that requires unique names. This has huge syntactic advantages, making it much less verbose, while still being ridiculously fast to parse. To illustrate the advantage, try to imagine how you would declare a segment in JSON having two consecutive **[if]** nodes. To give you an idea below is an example JSON segment illustrating this.

```json
{
   [
      {
         "name": "if",
         "value": "@SOME_EXPRESSION",
         "type": "expression",
         "args": [
            {
               "name": "log.info",
               "value": "YES!",
               "type": "string"
            }
         ]
      },
      {
         "name": "else",
         "value": "@SOME_EXPRESSION",
         "type": "expression",
         "args": [
            {
               "name": "log.info",
               "value": "Nope!",
               "type": "string"
            }
         ]
      }
   ]
}
```

In Hyperlambda the equivalent of the above JSON would resemble the following.

```
if:x:@SOME_EXPRESSION
   log.info:Yes!
else
   log.info:Nope!
```

Using YAML would simplify the above JSON, but still not even come close to the simplicity of the Hyperlambda structure. Still Hyperlambda benefits from all the advantages of JSON, such as being easy to parse, extremely fast, and easy to dynamically change, since it's an object with children that you can insert new objects into and modify dynamically.

Being able to dynamically change your code is of course crucial as you create code that generates and maintains code, similarly to how being able to dynamically mutate objects in JavaScript is crucial to manipulate data. The last point sums up the advantage of Hyperlambda, since instead of imagining Hyperlambda as static and immutable code, try to instead to imagine it as data, which just so happens to be possible to execute since it's a graph object mapping towards `if` constructs, `while` constructs, function invocations, etc.

> Hyperlambda's purpose is to be a mutable piece of executable code that you can change according to your needs

## Lambda objects and Hyperlambda

Hyperlambda is the name of the file format in its text representation, while lambda is the name of the nodes in memory, after having been parsed into a graph object. This distinction is similar to XML, operating with XML DOM or the XML Document Object Model, and XML itself being a file format. It is also similar to how JavaScript and JSON works, where JSON is a file format describing data, but also at the same time it's actually JavaScript too, or _"a JavaScript object"_ to be precise.

It could be argued that Hyperlambda is a simplified and humanly readable alternative to XML and JSON.

* [Read more about nodes](/plugins/magic.node/) to understand the difference between lambda objects and Hyperlambda.

## Lambda expressions

Lambda expressions are what allows you to reference nodes in your lambda objects. They're similar to XPath, but have more features, and are in general more powerful.

Technically Hyperlambda doesn't have variables. This is because _everything_ is a potential variable in Hyperlambda. However, by convention the Hyperlambda executor will not evaluate nodes starting with a `.` character. This allows you to declare _"data segments"_ by prepending your node's name with a dot, such as illustrated in our above example with our **[.data]** node.

Without the dot character in our above example, the Hyperlambda execution engine would attempt to invoke **[data]** as a _"slot"_. Since there's no slot named **[data]**, this would result in a runtime error or an exception.

* [Read more about lambda expressions](/plugins/magic.node/#lambda-expressions)

## Hyperlambda types

Hyperlambda is a functional programming language and does not allow for declaring classes or types. However, it does contain basic support for native types such as integers, strings, date and time objects, etc. Such type declarations are squeezed in between the name of your node and its value such as follows.

```
.foo1:int:5
.foo2:long:55
.foo3:string:Howdy world
```

String is the default type unless another type is explicitly declared, and strings only needs `"` or `'` if they contain colons (`:`) or quoting characters as a part of their values. Strings are treated the same way as in C#, except Hyperlambda doesn't support extrapolated strings, only `@"` and `"` types of strings.

* [Read more about Hyperlambda types](/plugins/magic.node/#hyperlambda-types)

## Hyperlambda execution

You can use the [Hyperlambda Playground](/dashboard/hyperlambda-playground/) to play with Hyperlambda, and execute snippets of Hyperlambda code in _"immediate"_ mode.

The Hyperlambda execution engine, or the **[eval]** slot from [magic.lambda](/plugins/magic.lambda/#how-to-use-eval), executes nodes sequentially from top to bottom, assuming everything is a slot, unless it starts with a `.` character. Most slots require arguments, which sometimes are given in the form of lambda objects, such as illustrated below.

```
.source
   foo1:bar1
   foo2:bar2
.destination
add:x:@.destination
   get-nodes:x:@.source/*
```

The above **[add]** node for instance, is given a lambda object containing one child node, being **[get-nodes]**. Our above **[get-nodes]** invocation is executed first, becoming the source for our **[add]** invocation - Resulting in the following result after execution.

```
.source
   foo1:bar1
   foo2:bar2
.destination
   foo1:bar1
   foo2:bar2
add:x:@.destination
```

As you can see we created a copy of each child node of our **[.source]** node, and appended these into our **[.destination]** node.

* [Read more about eval](/plugins/magic.lambda/#how-to-use-eval)

## Reference documentation

The most important parts of Hyperlambda is implemented in the following projects. If you want to dive deep into Hyperlambda you should probably read the documentation to both of these projects.

* [magic.lambda](/plugins/magic.lambda/)
* [magic.node](/plugins/magic.node/)
