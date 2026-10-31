---
title: "How to use [apply]"
description: "How to use [apply] - This slot takes an expression in addition to a list of arguments, and \"applies\" the arguments unto the expression's result node set, allowing you to perform dynamic substitutions on lambda hierarc..."
guide: true
slots: ["apply"]
---

The reference page of [`apply`](/reference/slots/core/apply/) has its arguments, constraints and declaration.

This slot takes an expression in addition to a list of arguments, and _"applies"_ the arguments unto the expression's
result node set, allowing you to perform dynamic substitutions on lambda hierarchies such as the following illustrates.

```
.lambda
   foo
      arg1:{some_arg}
      some-static-node:static-value

apply:x:-
   some_arg:value of argument
```

After execution of the above Hyperlambda you will have a result resembling the following.

```
apply
   foo
      arg1:value of argument
      some-static-node:static-value
```

Notice how the nodes from your template lambda object have been copied as children into your **[apply]**
node, while during this _"copying process"_, the arguments you supplied to **[apply]** have been used
to perform substitutions on all nodes in your template lambda having a value of `{xxx}`, where xxx is
your argument name. In the above example for instance the `arg1:{some_arg}` template node had its value
replaced by the value of the **[some_arg]** node passed in as a parameter to **[apply]**. If the name of
the argument to **[apply]**, matches the value of your template node wrapped inside curly braces - Then
the value of your argument to apply becomes the _new value_ of your template node after substitution has
been performed.

Only node values starting out with `{` and ending with `}` will be substituted, and you are expected to provide
all arguments found in the template lambda object, or the invocation will fail, resulting in an exception. This
allows you to create _"template lambda objects"_ that you dynamically transform into something else, without
really caring about its original structure, but rather only its set of dynamic substitution arguments. This
slot leaves all other nodes as is.

Basically, the way it works, is that it takes your expression, and recursively iterates each node below the
result of your expression, checks to see if the node's value is an argument such as e.g. `{howdy}` -
And if so, it substitutes the `{howdy}` parts with the value of the argument you are expected to supply to your
invocation having the name **[howdy]**.

You can also reference the same argument multiple times in your template, in addition to create arguments that
are lambda objects instead of simple values. Below is an example of both of these constructs.

```
.lambda
   foo
      foo1:{arg1}
      foo2:{arg1}
      foo3:{arg2}

apply:x:-
   arg1:int:5
   arg2
      this:is
         an:entire
         lambda:object
      used_as_an_argument:int:7
```

The above will result in the following.

```
apply
   foo
      foo1:int:5
      foo2:int:5
      foo3
         this:is
            an:entire
            lambda:object
         used_as_an_argument:int:7
```

Above you can also see how typing information is not lost, since the **[foo1]** and **[foo2]** nodes
are both having integer values of 5 after apply is done executing. At the same time you can see how
the **[foo3]** node instead of having a simple value applied, actually ended up with a copy of all
children passed in as **[arg2]**. You can also substitute names of nodes, such as the following
illustrates.

```
.lambda
   foo
      {arg1}:value-is-preserved

apply:x:-
   arg1:foo1
```

The above of course results in the following.

```
apply
   foo
      foo1:value-is-preserved
```

This is a fairly advanced slot, but it's the heart of the generator, allowing us to generate HTTP endpoints,
starting out with some template file, which is dynamically changed, according to input arguments supplied during
the crudification process. You can also combine transformations of names, values, and children in the
same template nodes. The process is also recursive in nature, performing substitutions through the entire
hierarchy of your template lambda.
