---
title: Execute code on your server through your browser
description: The evaluator allows you to submit Hyperlambda to your server and have your code executed in 'immediate' mode. This is useful for administrating your Magic server, and/or learning Hyperlambda.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-send-email.jpg"
---

# Execute code on your server through your browser

The evaluator allows you to play with Hyperlambda code, and execute your code in _"immediate mode"_,
for then to see the result of your execution immediately. The evaluator is also a nice starting
point to learn Hyperlambda, since it contains a whole range of _"Hyperlambda snippets"_ that
somehow demonstrates Hyperlambda's capabilities, and provides examples for you as you start out
learning Hyperlambda. Click the _"Load"_ button to load up some snippet, study it, modify it,
and then execute it, for afterwards see the result of the execution immediately. Below is a
screenshot of the evaluator component

![Evaluator component](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/eval-component.jpg)

If you create a Hyperlambda snippet you for some reason want to save for later, you can save your
Hyperlambda into your _"snippets"_ collection by clicking the _"Save"_ button, and giving your
snippet a name. This allows you to create snippets you need to periodically execute,
and store these as your _"admin snippets"_, to rapidly execute snippets that somehow does something
towards your server.

## Internals

The evaluator will transmit your Hyperlambda to the server, where Magic will _"transpile"_ your Hyperlambda
into a graph object, referencing .Net 6 CLR _"slots"_ implemented in C#, resulting in being able to dynamically
execute code, and returning the result of the invocation to caller. In such a regard Hyperlambda resembles
XML, XSLT and XPath, although with a much less confusing syntax, where executing a snippet of Hyperlambda
returns a _"transformed"_ lambda object, which again is serialised as Hyperlambda and returned back to the
client. This is why after having executed your Hyperlambda you can see its _"result"_ below your input
CodeMirror instance, such as illustrated below.

![Hyperlambda result](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/eval-result.jpg)

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
