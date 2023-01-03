---
layout: post
author: thomas
title: An introduction to Hyperlambda
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/eval-component.jpg"
description: Hyperlambda is a unique programming language, since it allows for your computer to generate most of your code. However, in this article I will show you how to manually code in Hyperlambda.
canonical_url: https://aista.com/blog/an-introduction-to-hyperlambda/
---

The purpose of Hyperlambda is to have a programming language that allows your computer to generate most of your code.
However, sometimes you need to manually modify the generated code yourself, and/or create Hyperlambda code manually,
at which point you'll need to understand Hyperlambda. Hyperlambda is extremely easy to learn though, and you can
probably teach yourself most of its basics in less than 10 minutes. This article is an introduction to Hyperlambda
and gives you an overview of Hyperlambda from a bird's perspective.

## Structure

Syntactically Hyperlambda resembles YAML, however it has its own unique syntax, and even though it has the same readability
traits as YAML, it is _not_ the same. In theory we could have used YAML, JSON, or XML to create Hyperlambda, but that would
increase its verbosity, resulting in more difficult to read code. However, its structure is easily understood in 5 minutes,
since it is literally just a text representation of a tree structure. Hyperlambda's structure is based upon _"nodes"_,
and each node has 3 properties.

* Name
* Value
* Children

To illustrate imagine the following Hyperlambda.

```
.data
   foo1:bar1
   foo2:bar2
```

The above Hyperlambda consists of 3 nodes. The first node is called **[.data]**. This node has two children called **[foo1]**
and **[foo2]**. Both of these nodes have a value each being _"bar1"_ and _"bar2"_. The colon separates the node's name and
its value, and 3 spaces opens up the children collection. To play around with Hyperlambda you can use Magic's _"Evaluator"_
component. Below is a screenshot of a slightly more complex example.

![The Hyperlambda evaluator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/eval-component.jpg)

The above example is of course more complex than our first code snippet, but it still follows the exact same structure
being name/value/children. In the above example the **[while]** node is given two children arguments; One condition node being
its **[lt]** parts, and another lambda object being its **[.lambda]** parts. The **[while]** loop will execute its
**[.lambda]** object for as long as its condition is true. The condition again is an **[lt]** condition, implying _"less than"_.
Translating the above Hyperlambda to English hence becomes the following.

> Execute .lambda while .no has a value less than 20

Inside **[.lambda]** we're creating a log entry before we increment the **[.no]** value. Magic
contains many similar conditions, such as _"more than"_, _"equal"_, etc - In addition to a lot of additional _"keywords"_.
Refer to the [magic.lambda documentation](/documentation/magic.lambda/) for an exhaustive list.

## Code is data

The reasons why Hyperlambda is so good at creating and modifying code, is because there is no difference in Hyperlambda
between _"code"_ and _"data"_ - Implying code _is_ data. The same way we can modify data structures such as XML, YAML, or
the HTML DOM for that matter, Hyperlambda allows for modifying its code. If you want to change the invocation to **[log.info]**
in the above screenshot to **[log.error]** this is as easy as adding the following Hyperlambda to the top of your code.

```
set-name:x:../**/log.info
   .:log.error
```

This trait of Hyperlambda makes it very easy to create _"self evolving code"_, that somehow changes an existing snippet
of code to do something completely different. This trait of Hyperlambda is crucial for its ability to automatically generate
code and is the reason why it can with such ease create and generate code 100% automatically for you. When you think about
_"how weird"_ Hyperlambda is, please understand its _reasons_ for being weird. Hyperlambda's _"weirdness"_ allows us to easily
create templated snippets of code that we use as the foundation for some process automatically generating custom code, by
parametrising our code dynamically, such that we can modify it according to our specific needs.

## Everything is code

The natural realisation of the above is that all data is also code. This creates a problem for us since we might
want to create nodes we don't want to _"execute"_. This is achieved by starting a node's name with a _"."_. This
instructs the Hyperlambda execution engine that this node should not be executed but simply ignored by the
Hyperlambda execution engine. This is what allows us to create _"variables"_, and/or nodes containing _"data"_.
You can see examples of such nodes in our previous code snippets and screenshots.

## Expressions

Hyperlambda doesn't have _"variables"_. This is because _everything_ is a variable in Hyperlambda, including function
invocations, arguments to functions, etc. This creates a problem for us, being that we need some mechanism to modify
node names, node values, and their children collection. This is where expressions comes into the picture. An expression
allows us to reference any node in our Hyperlambda object. An example of such an expression can be seen in the above
screenshot where our invocation to **[get-value]** has the value of `:x:@.no`. Its `:x:` part declares it as an expression
_type_, while the `@.no` part is the actual expression. An expression is similar to chained LINQ statements in that it is a list
of `IEnumerable` objects, that reacts upon each other in a chain. Below is a slightly more complex expression to illustrate
the point.

```
.data
   foo1:bar1
   foo2:bar2
   foo3:bar3

set-value:x:../*/.data/*/foo2
   .:Hyperlambda was here
```

If you execute the above Hyperlambda in your Magic's _"Evaluator"_ component, you will see it changes the value _"bar2"_
to _"Hyperlambda was here"_. This is because the expression we give our **[set-value]** invocation basically says
the following.

> Give me the root node, then all its children, then filter away everything not having the name of '.data', find its children again, and filter away everything not having the name of 'foo2'

When the expression is done filtering our nodes, we're left with only the **[foo2]** node, at which point **[set-value]**
changes its value. To understand expressions and type declarations in Hyperlambda you might benefit from reading
about [magic.node](/documentation/magic.node/) diving deeper into both expressions, iterators, and Hyperlambda's typing
system. However, think of expressions as _"pointers into your Hyperlambda object"_, where each pointer is composed
from a chain of _"iterators"_, where each iterator is separated by a slash (/), and your expression as a whole can
point to zero or more nodes.

## Slots

Hyperlambda doesn't really understand the idea of function invocations. Instead everything is a _"slot"_ in Hyperlambda.
However, for all practical concerns a _"slot"_ is similar to a function invocation in a traditional programming language.
Magic contains hundreds of slots for all sorts of scenarios, and in the documentation for Magic we often refer to
these using square brackets in **bold** text. To modify parts of your Hyperlambda the following slots are your
most important friends.

* __[set-value]__ - Changes the value of one or more nodes
* __[set-name]__ - Changes the name of one or more nodes
* __[add]__ - Adds a bunch of children to some node
* __[insert-before]__ - Inserts a bunch of nodes _before_ some node
* __[insert-after]__ - Inserts a bunch of nodes _after_ some node
* __[remove-nodes]__ - Removes nodes

By combining the above slots you have everything you need to be able to change your Hyperlambda objects as they
are executing, resulting in a Turing complete programming language, even though it technically doesn't have neither
functions nor variables. To see which slots are available you can click **CTRL+SPACE** on Windows or
**FN+CONTROL+SPACE** on a Mac while your code editor has focus to open the autocomplete drop down. Below is a screenshot
of the autocomplete drop down from Hyper IDE.

![Hyperlambda autocomplete](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/autocomplete.jpg)

## Snippets

Magic's _"Evaluator"_ component contains a lot of Hyperlambda snippets illustrating some aspect of Hyperlambda. If
you click the _"Load"_ button you can load existing Hyperlambda snippets demonstrating some aspect of the programming
language for you. The easiest way to start learning Hyperlambda is probably to go through these snippets, understand
what they do, for then to apply similar constructs in your own Hyperlambda. The **[while]** loop in the first screenshot
in this article is one example of such a snippet. You can also save your own snippets as you're playing around with
Hyperlambda. Below is a video where I demonstrate Hyperlambda and what you can achieve with it.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/5Vm5-_rTl5U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Orchestration

Hyperlambda is an _"orchestration programming language"_. This implies that it is a super high level language,
intended for _"orchestrating"_ programming building blocks. For these reasons some would argue it's not
a _"real"_ programming language, which would be a correct assessment. If you're creating quick sort functionality
or polygon rendering algorithms in Hyperlambda, you're doing something wrong. Hyperlambda is _not_ intended for
algorithm heavy snippets, even though technically it _is_ possible to implement anything in it. To understand
Hyperlambda's position, realise its purpose is to sit between your algorithm heavy low level code, and the client,
_"orchestrating"_ your low level building blocks, giving you dynamic capabilities on your code as a whole.

Hyperlambda is for your code the same as YAML is for your pipelines, configurations, and Kubernetes cluster, in
that it allows you to _"configure"_ your code together, using declarative concepts, from a high level abstraction
layer, where you don't have to think about the internal details of your executing code. However, where YAML allows
you to configure deployment of your applications, Hyperlambda allows you to _"configure"_ your application instead
of manually coding it using low level programming languages such as C# or Java. However, when that's said, the
entirety of Magic is actually created in Hyperlambda, implying its middleware, the IDE, the SQL editor, _everything_
in fact, including the crudifier - And you can actually find this code inside your _"system"_ folder if you're
using Hyper IDE to check out its code. If you're using heavy recursion, lots of nested while loops, and dozens
of temporary variables in your Hyperlambda code, you would probably be better creating this part of your code
in C# and expose your C# code as a _"high level slot"_ to your middleware instead.
