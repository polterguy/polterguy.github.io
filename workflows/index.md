---
title: Workflows
description: A workflow is a collection of chained actions, where each action can take as input the output produced by previous actions.
---

A workflow is a chained collection of actions, where each action can produce output, that consecutive actions can consume as input. The most famous example of a workflow system is probably MWF, or Microsoft Workflow Foundation. Magic implements workflows using Hyperlambda, which largely eliminates the need to visualise workflows using charts, and allows the user to use the source code as the primary means to edit and read the workflow. Watch the following video to understand how such workflows are built.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/ITz1ASqsWoM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Advantages

Being able to _"drag'n'drop"_ backend code together the way we do in the above video, have huge benefits. First of all it significantly lowers the bar for software development, allowing people without prior software development experience to create backend code. Secondly, it makes it much faster to create said code. I clocked myself in regards to this, and found that in theory I could create 604,000 lines of code per month. Obviously using LOC as a measure for productivity is normally not a good thing, but these were production ready lines of code, highly secure, scalable, and performing in regards to all neutral metrics.

In the following video I am creating a complete registration API in 15 minutes to illustrate the point.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/Ntunzh-DdaY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

The point being that creating a registration API manually is a task that might take weeks of manual coding. Doing it in 15 minutes obviously has advantages, especially considering the skill level required to accomplish the above, which is close to nothing.

## Declarative programming

Workflows are based upon actions, and each action is an _"atomic piece of functionality that does something useful"_. This implies you do not lose much flexibility when using workflows, and at least in theory you could create anything using Magic workflows you could create using traditional coding.

However, since workflows in Magic are based upon Hyperlambda, this allows you to sprinkle in Hyperlambda directly into your workflow where required, and even invoke C# code when called upon. So you get the best of both worlds; Declarative programming as your primary tool of choice, with the ability to hook into the CLR and C# when required.
