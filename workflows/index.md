---
title: Workflows
description: A workflow is a collection of chained actions, where each action can take as input the output produced by previous actions.
header:
  image: /assets/images/wizard-magically-creating-things.png
---

A workflow is a chained collection of actions, where each action can produce output, that consecutive actions can consume as input. The most famous example of a workflow system is probably MWF, or Microsoft Workflow Foundation.

Magic implements workflows using [Hyperlambda](/hyperlambda/), which largely eliminates the need to visualise workflows using charts, and allows the user to use the source code as the primary means to edit and maintain the workflow. Watch the following video to understand how such workflows are built.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/ITz1ASqsWoM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Advantages

Being able to _"drag'n'drop"_ backend code together the way we do in the above video, have huge benefits. First of all it significantly lowers the bar for software development, allowing people without prior software development experience to create backend code. Secondly, it makes it much faster to create said code. I clocked myself in regards to this, and found that in theory I could create 604,000 lines of code per month. Obviously using LOC as a measure for productivity is normally not a good thing, but these were production ready lines of code, highly secure, scalable, and performing in regards to all neutral metrics.

In the following video I am creating a complete registration API in 15 minutes to illustrate the point.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/Ntunzh-DdaY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

The point being that creating a registration API manually is a task that might take weeks of manual coding. Doing it in 15 minutes obviously has advantages, especially considering the skill level required to accomplish the above, which is close to nothing.

Creating a registration API using C#, GoLang, or Java, typically requires years of training, in addition to knowledge about a _"bajillion"_ things. In Magic you can do it after some few minutes of watching a YouTube video - And you can implement it 1,860 times faster than a senior software developer can in most other programming languages, assuming the industry average of 325 lines of code per month is correct.

## Declarative programming

Workflows are based upon actions, and each action is an _"atomic piece of functionality that does something useful"_. This implies you do not lose much flexibility when using workflows, and at least in theory you could create anything using Magic workflows you could create using traditional coding.

However, since workflows in Magic are based upon Hyperlambda, this allows you to sprinkle in Hyperlambda directly into your workflow where required, and even invoke C# code when called upon. So you get the best of both worlds; Declarative programming as your primary tool of choice, with the ability to hook into the CLR and C# when required through Hyperlambda.

## Functional programming

This is facilitated for by functional constructs. Each slot in [Hyperlambda](/hyperlambda/) takes a node-set as its input, and returns another node-set after executing. This is what allows for _"chaining"_ Hyperlambda actions such as illustrated in the above video.

Combined with [lambda expressions](/plugins/magic.node/#lambda-expressions), this allows you to chain _"function invocations"_ or slots, where the output from one slot is used as input to the next.

## Actions

Actions are the basic atomic building blocks of workflows, and an action is defined as _"the smallest piece of code that does something useful"_. This allows you to create chains of actions that somehow implements your business logic, _without_ having to manually write the code yourself.

An action again is just a declaratively created snippet of Hyperlambda code itself, wired together using Hyperlambda, allowing you to create custom actions you can later reference in your own workflows. Below is the _"file-load"_ action to illustrated how an action looks like.

```
/*
 * Loads the specified [file] and returns to caller as [content].
 */
.arguments
   file
      type:string
      mandatory:bool:true
.icon:insert_drive_file

// Loads the specified file.
load-file:x:@.arguments/*/file

// Returning result of above invocation to caller.
yield
   content:x:@load-file
```

To extend your workflows with your own custom actions is as easy as creating a Hyperlambda file using for instance [Hyper IDE](/dashboard/hyper-ide/), and store it in your _"/etc/workflows/actions/"_ folder.

## Meta programming

The above constructs allows for _"meta programming"_, where the machine assembles the code required to create functionality, allowing the software developer to become more of an _"orchestrator"_, while having the internals of your actions encapsulate the nitty gritty stuff. Or as we say ...

> Where the Machine Creates the Code

* [Read more about Hyperlambda](/hyperlambda/)
