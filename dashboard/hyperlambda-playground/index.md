---
title: Hyperlambda Playground
description: The Hyperlambda Playground allows you to submit Hyperlambda to your server and have your code executed in 'immediate' mode. This is useful for administrating your Magic server, and/or learning Hyperlambda.
og_image: "/images/eval-component.jpg"
header:
  image: /assets/images/wizard-playing-magic-games-with-children.webp
---

The Hyperlambda Playground component allows you to play with [Hyperlambda](/hyperlambda/) code, and execute your code in _"immediate mode"_, for then to see the result of your execution immediately. The Hyperlambda playground is also a nice starting point to learn Hyperlambda, since it contains a whole range of Hyperlambda snippets that somehow demonstrates Hyperlambda's capabilities, and provides examples for you as you start out learning Hyperlambda. Click the _"Snippets"_ button to load up some snippet, study it, modify it, and then execute it - For then to afterwards see the result of the execution.

![Screenshot of the Hyperlambda Playground Component executing some arbitrary Hyperlambda](/images/eval-component.jpg)

If you create a Hyperlambda snippet you for some reason want to save for later, you can save your Hyperlambda to your _"snippets"_ collection, by clicking the _"Save"_ button, and give your snippet a name. This allows you to create snippets you need to periodically execute, and store these as your _"admin snippets"_, to rapidly execute snippets that somehow executes some Hyperlambda task at will.

## Hyperlambda Playground internals

The Hyperlambda Playground component will transmit your Hyperlambda to the server, where Magic will _"transpile"_ your Hyperlambda into a graph object, referencing CLR _"slots"_ implemented in C#, resulting in being able to dynamically execute code, and returning the result of the invocation to the caller. In such a regard Hyperlambda resembles XML, XSLT and XPath, although with a much less confusing syntax, where executing a snippet of Hyperlambda returns a _"transformed"_ lambda object, which again is serialised as Hyperlambda and returned back to the client. This is why after having executed your Hyperlambda you can see its _"result"_.

Hyperlambda is an input/output execution graph object in such a regard, similar to XML and XSLT, where the output of the execution process, is the Hyperlambda transformed as a consequence of the execution itself. This is why you have both an input and an output part in the Hyperlambda playground.

## Hyperlambda as a meta programming language

Since Hyperlambda is a meta programming language, implying the machine can easily generate functioning Hyperlambda that it executes, this allows you to use the Hyperlambda Playground as a _"software development extension"_, creating snippets of Hyperlambda, that somehow creates or modifies existing Hyperlambda code, and can be dynamically executed on demand.

In the Hyperlambda Playground's snippets collection, you can find some snippets that does such tasks for you, such as one snippet called _"format-hyperlambda"_ that you can parametrise with some folder and execute. Once executed this Hyperlambda snippet will correctly format all code recursively within that folder, by reading all Hyperlambda files inside of this folder recursively, for then to correctly format your files.

You can of course create your own similar snippets, that automatically performs similar types of tasks, for then to save these Hyperlambda files to your snippets collection.

* [Read more about Hyperlambda](/hyperlambda/) to understand how to use this component
