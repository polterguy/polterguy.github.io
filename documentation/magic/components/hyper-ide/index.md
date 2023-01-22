---
title: Hyper IDE, a web based IDE
description: Hyper IDE is a fully fledged integrated development environment, giving you most important features from other IDEs. Hyper IDE works perfectly on your phone, tablet, computer, or any other device you might have access to with a browser.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg"
---

# The Hyper IDE component

Hyper IDE is your _"goto component"_ when you want to create your own modules using Magic and Hyperlambda.
It's a fully fledged web based IDE or Integrated Development Environment, allowing you to edit your code,
create new modules, and contains most things you're used to from a traditional IDE. It is also the natural
extention of Magic's [endpoint generator](/documentation/magic/components/crudifier/backend/), since it
allows you to edit the Hyperlambda endpoint files after Magic has generated your CRUD backend.

![Editing a file in Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg)

Hyper IDE also provides integrated autocomplete if your editor has focus and you click CTRL+SPACE
in Windows or FN+CONTROL+SPACE on your Mac. This allows you to very rapidly create Hyperlambda code,
while having Hyper IDE ensure your code is using existing slots. Click the _"Shortkeys"_ button to see
a list of all keyboard shortcuts Hyper IDE provides. Notice, these keyboard shortcuts are only available
when your code editor has focus. You can also create files and folders, and upload files to your server
through the action buttons drop down menu.

![Hyper IDE autocomplete](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

## Invoking endpoints from Hyper IDE

Hyper IDE allows you to invoke your HTTP endpoints without ever leaving your IDE. This makes it easy for
you to test your code as you are creating it. If you are editing an HTTP endpoint Hyperlambda file, you can click F5,
resulting in something resembling the following.

![Invoking HTTP endpoints from Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-blog.jpg)

For more details about invoking your HTTP endpoints refer to the [endpoints component](/documentation/magic/components/endpoints/).
This component also allows you to automatically generate health check tests, sanity checking your system as you're editing its code.

## Hyper IDE macros

Hyper IDE supports _"macros"_. A macro is an automated
process that somehow creates code, and/or modifies your existing code, 100% automatically. There exists
several macros in Hyper IDE solving everything from automatically documenting your module, to creating file
upload endpoints for you. To execute a macro, first select which module you want to run it for, then click
the macro action button, and parametrise your macro.

![Hyper IDE macros](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/execute-macro.jpg)

## Hyper IDE features

Hyper IDE is not a fully fledged IDE, and cannot compare to something like VS Code or Visual Studio. However,
its purpose is to function as an extention on top of the endpoint generator, giving you code editing capabilities
of your generated Hyperlambda files. You can use Hyper IDE to edit TypeScript, Ruby, HTML and C# code, but we
don't recommend exchanging it with your existing code editor, since other IDEs have much more features than
Hyper IDE. However, the opposite is also correct, implying Hyper IDE have features your existing IDE does not have.

One example of such features is its integrated machine learning and AI features. With Hyper IDE, you can use
OpenAI's API to ask it to create code for you. This resembles the way GitHub CoPilot works, with the difference
being that Hyper IDE's AI models are much more tightly integrated than VS Code's GitHub CoPilot is.

In addition, Hyper IDE supports macros, that automatically generates code for you, by reading meta data
from your existing code, allowing it to semantically understand what your existing code does, before it
applies its changes. This of course only works with Hyperlambda, but gives you some extra _"super powers"_
when it comes to code editing, and can be a real time saver for you when possible to use.

Another difference is that Hyperlambda is a dynamic programming language, implying once you've saved
your Hyperlambda files, you can immediately test your code by executing it from within Hyper IDE.
This results in a much tighter development model than a traditionally compiled programming language
gives you, making it much faster to find bugs and create working code.

## Machine learning in Hyper IDE

Hyper IDE contains an integrated Machine Learning part, based upon OpenAI's ChatGPT, allowing
you to generate code using AI, directly from its IDE. To use this on Hyperlambda, you'll need
to train the existing _"hl"_ model. We suggest using Curie as your base model if you do this.
Curie is first of all significantly less expensive than DaVinci, in addition to that it's
faster than DaVinci. Magic comes with almost 1,000 Hyperlambda training snippets, but we
are constantly adding more machine learning training data to it.

