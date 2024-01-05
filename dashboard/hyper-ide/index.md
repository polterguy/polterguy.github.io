---
title: Hyper IDE
description: Hyper IDE is a fully fledged integrated development environment, giving you most important features from other IDEs. Hyper IDE works perfectly on your phone, tablet, computer, or any other device you might have access to with a browser.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg"
---

Hyper IDE is your _"goto component"_ when you want to create your own modules using Magic and Hyperlambda.
It's a web based IDE, allowing you to edit your code,
create new modules, and contains a lot of things you're used to from a traditional IDE. It is also the natural
extention of Magic's [endpoint generator](/dashboard/endpoint-generator/), since it
allows you to edit the Hyperlambda endpoint files after Magic have generated your CRUD backend. However, its most
important feature is probably its ability to easily allow you to create [workflows](/workflows/).

![Editing a file in Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg)

Hyper IDE also provides integrated autocomplete if your editor has focus and you click CTRL+SPACE
in Windows or FN+CONTROL+SPACE on your Mac. This allows you to very rapidly create Hyperlambda code,
while having Hyper IDE ensure your code is using existing slots. Click the _"Shortkeys"_ button to see
a list of all keyboard shortcuts Hyper IDE provides. Notice, these keyboard shortcuts are only available
when your code editor has focus.

![Hyper IDE autocomplete](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

## Executing Hyperlambda from Hyper IDE

Hyper IDE allows you to execute Hyperlambda without ever leaving your IDE. This makes it easy for
you to test your code as you are creating it, and is the closest you come to the equivalent of a _"debugger"_ in Magic.

If you're creating a workflow, it will even communicate everything it does back to the client over web sockets,
allowing you to see input arguments to specific actions, and what they returned as a result. If an error occurs,
it will show you exactly where this error occurred.

## Hyper IDE features

Hyper IDE is not a fully fledged IDE, and cannot compare to something like VS Code or Visual Studio. However,
its purpose is to function as an extention on top of the endpoint generator, giving you code editing capabilities
of your generated Hyperlambda files - In addition to rapidly allowing you to create [workflows](/workflows/) and edit Hyperlambda
files. You can use Hyper IDE to edit TypeScript, Ruby, HTML and C# code, but we don't recommend exchanging it
with your existing code editor, since other IDEs have much more features than Hyper IDE. However, the opposite
is also true, implying Hyper IDE have features your existing IDE does not have - Especially in regards to
[Hyperlambda](/hyperlambda/), which is the axiom around which Magic evolves.

One example of such features is its integrated machine learning and AI features. With Hyper IDE, you can use
OpenAI's API to ask it to create code for you. This resembles the way GitHub CoPilot works.

Another difference is that Hyperlambda is a dynamic programming language, implying once you've saved
your Hyperlambda files, you can immediately test your code by executing it from within Hyper IDE.
This results in a much tighter development model than a traditionally compiled programming language
gives you, making it much faster to find bugs and create working code.

Magic does not separate between code creation and your code's production environment, providing
you instant feedback as you develop.
