---
title: Hyper IDE
description: Hyper IDE is a fully fledged integrated development environment, giving you most important features from other IDEs. Hyper IDE works perfectly on your phone, tablet, computer, or any other device you might have access to with a browser.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg"
header:
  image: /assets/images/wizard-flying-through-air-with-hyperlambda-raining-from-stars.png
---

Hyper IDE is your _"goto component"_ when you want to create your own modules using Magic and Hyperlambda.
It's a web based IDE, allowing you to edit your code,
create new modules, and contains a lot of things you're used to from a traditional IDE. It is also the natural
extension of Magic's [endpoint generator](/dashboard/endpoint-generator/), since it
allows you to edit the Hyperlambda endpoint files after Magic have generated your CRUD backend. Another
important feature is its ability to help you when creating [workflows](/workflows/).

![Editing a file in Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg)

Hyper IDE also provides integrated autocomplete if your editor has focus and you click CTRL+SPACE
in Windows or FN+CONTROL+SPACE on your Mac. This allows you to very rapidly create Hyperlambda code,
while having Hyper IDE ensure your code is using existing slots. Click the _"Shortkeys"_ button to see
a list of all keyboard shortcuts Hyper IDE provides. Notice, these keyboard shortcuts are only available
when your code editor has focus.

![Hyper IDE autocomplete](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

## Hyper IDE features

Hyper IDE is not a fully fledged IDE, and cannot compare to something like VS Code or Visual Studio. However,
its purpose is to function as an extention on top of the endpoint generator, giving you code editing capabilities
of your generated Hyperlambda files - In addition to rapidly allowing you to create [workflows](/workflows/) and edit Hyperlambda
files.

You _can_ use Hyper IDE to edit TypeScript, Ruby, HTML and C# code, but we don't recommend exchanging it
with your existing code editor, since other IDEs have much more features than Hyper IDE. However, the opposite
is also true, implying Hyper IDE have features your existing IDE does not have - Especially in regards to
[Hyperlambda](/hyperlambda/), which is the axiom around which Magic evolves.

One example of such features is its integrated machine learning and AI features. With Hyper IDE, you can use
OpenAI's API to ask it to create code for you. This resembles the way GitHub CoPilot works.

Another difference is that Hyperlambda is a dynamic programming language, implying once you've saved
your Hyperlambda files, you can immediately test your code by executing it from within Hyper IDE by clicking
F5. This results in a much tighter development model than a traditionally compiled programming language
gives you, making it much faster to find bugs and create working code.

If you execute code in immediate mode using F5, and your code requires arguments, Hyper IDE will ask you
for what topasss in as arguments. This isn't perfect, and only works for first level arguments - But if
you need more complexity, you can always use the [Hyperlambda Playground](/dashboard/hyperlambda-playground/),
and/or the [Endpoints Component](/dashboard/endpoints/).

Magic does not separate between code creation and your code's production environment, providing
you with instant feedback as you create your code.

## Executing Hyperlambda from Hyper IDE

Hyper IDE allows you to execute Hyperlambda without ever leaving your IDE by clicking F5. This makes it easy for
you to test your code as you are creating it, and is the closest you come to the equivalent of a _"debugger"_ in Magic.

If you're creating a workflow, it will even communicate everything it does back to the client over web sockets,
allowing you to see input arguments to specific actions, and what they returned as a result. If an error occurs
as you're executing a workflow, Hyper IDE will show you exactly where the error occurred.

![Executing a workflow in Hyper IDE](/assets/images/executing-workflow.jpeg)

## Integrated Hyperlambda AI help

If you mark some Hyperlambda code in Hyper IDE and click F1, it will invoke AINIRO.IO's machine learning type
for Hyperlambda, and actually explain your code using natural language.

![Hyper IDE integrated Hyperlambda help](/assets/images/hyperlambda-ai-help.jpeg)

Notice, this will use AINIRO.IO's machine learning models, and tokens. For now we've opened up this for free usage,
but we might have to charge a fee for this in the future. Other machine learning components are using _your local_ OpenAI types and tokens, such as if you ask the AI to create an HTML page for you, or you're using [SQL Studio](/dashboard/sql-studio/)'s AI features to create SQL for you.

## Machine learning features

Hyper IDE contains a machine learning component, similar to [SQL Studio](/dashboard/sql-studio/), that allows you to have it create code for you using AI.

![Use AI to generate code in Hyper IDE](/assets/images/use-ai-to-generate-code-in-hyper-ide.jpeg)

If you use the AI chat interface in Hyper IDE you can ask the AI to create, and/or modify your code, and
such have _"conversations"_ with the AI about your code - And even use the AI as
your _"AI-based pair programming buddy"_. Such requests will be paired to a local type with the same name
as your file extension, implying if you're asking the AI to help you when you've got an HTML file open,
the AI will search for a type who's name is _"html"_. If the backend does not find such a type, it
will resort to using your _"default"_ type.

This allows you to create your own unique models using RAG or fine-tuning, that are matched to
your file extensions, to for instance teach the AI about your own code, etc.

## Modules

Magic is modularized, allowing you to easily move modules from one machine to another. This is
the purpose of your _"/modules/"_ folder, as in each folder inside this folder is considered a module
in Magic.

If you're developing a module in your own local installation of Magic, you can mark the folder in
the tree control, and click the action button for downloading the folder. This will give you a zip file
you can easily upload to another server using the install module action button.

This is also horizontally integrated into [SQL Studio](/dashboard/sql-studio/), allowing you to _"export"_
your database DDL SQL to a module, assuming your module has the same name as your database. If you use this
feature, Magic will automatically create your database, and even apply migration scripts if required
during installation.
