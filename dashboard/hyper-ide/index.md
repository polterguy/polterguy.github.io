---
title: Hyper IDE
description: Hyper IDE is a fully fledged integrated development environment, but probably works best with Hyperlambda, and is not intended to replace your primary IDE for JavaScript or HTML.
og_image: "/images/og-hyper-ide-2.jpg"
header:
  image: /assets/images/wizard-flying-through-air-with-hyperlambda-raining-from-stars.webp
---

Hyper IDE is your _"goto component"_ when you want to create your own modules using Magic and Hyperlambda. It's a web based IDE, allowing you to edit your code, create new modules, and contains a lot of things you're used to from a traditional IDE. It is also the natural
extension of Magic's [endpoint generator](/dashboard/endpoint-generator/), since it allows you to edit the Hyperlambda endpoint files after Magic have generated your CRUD backend, and the foundation for [Hyperlambda Workflows](/workflows/).

![Screenshot of editing a Hyperlambda file in Hyper IDE](/images/og-hyper-ide-2.jpg)

Hyper IDE also provides integrated autocomplete if your editor has focus and you click CTRL+SPACE in Windows or FN+CONTROL+SPACE on your Mac. This allows you to very rapidly create Hyperlambda code, while having Hyper IDE ensure your code is using existing slots. Click the _"Shortkeys"_ button to see a list of all keyboard shortcuts Hyper IDE provides. Notice, these keyboard shortcuts are only available when your code editor has focus.

![Screenshot of Hyper IDE's autocomplete feature with Hyperlambda](/images/hyper-ide-actions.jpg)

## Hyper IDE features

Hyper IDE is not a fully fledged IDE, and cannot compare to something like VS Code or Visual Studio. However, its purpose is to function as an extension on top of the endpoint generator, giving you code editing capabilities of your generated Hyperlambda files - In addition to rapidly allowing you to create [workflows](/workflows/) and edit Hyperlambda files.

You _can_ use Hyper IDE to edit TypeScript, Ruby, HTML, and C# code, but we don't recommend replacing it with your existing code editor, since other IDEs have much more features here than Hyper IDE. However, the opposite is also true, implying Hyper IDE have features your existing IDE does not have - Especially in regards to [Hyperlambda](/hyperlambda/).

For a walkthrough of Hyper IDE's most important features you can watch the [following YouTube video](https://www.youtube.com/watch?v=g8r8asbLIkA).

<iframe width="560" height="315" src="https://www.youtube.com/embed/g8r8asbLIkA?si=45Vedtt3-0ros8x6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

One example of such features is its integrated machine learning and AI features. With Hyper IDE, you can use OpenAI's API to ask it to create code for you. This resembles the way GitHub CoPilot works. Another difference is that Hyperlambda is a dynamic programming language, implying once you've saved your Hyperlambda files, you can immediately test your code by executing it from within Hyper IDE by clicking F5. This results in a much tighter development model than a traditional compiled programming language gives you, making it much faster to find bugs and create working code.

If you execute code in immediate mode using F5, and your code requires arguments, Hyper IDE will ask you for what to pass in as arguments. This isn't perfect, and only works for first level arguments - But if you need more complexity, you can always use the [Hyperlambda Playground](/dashboard/hyperlambda-playground/), and/or the [Endpoints Component](/dashboard/endpoints/).

Magic does not separate between code creation and your code's production environment, providing you with instant feedback as you create your code.

## Executing Hyperlambda from Hyper IDE

Hyper IDE allows you to execute Hyperlambda without ever leaving your IDE by clicking F5. This makes it easy for you to test your code as you are creating it, and is the closest you come to the equivalent of a _"debugger"_ in Magic.

If you're creating a workflow, Hyper IDE will communicate everything it does back to the client over web sockets, allowing you to see input arguments to specific actions, and what they return. If an error occurs as you're executing a workflow, Hyper IDE will show you exactly where the error occurred.

![Screenshot of executing a Hyperlambda workflow from Hyper IDE](/assets/images/executing-workflow.jpeg)

## Integrated Hyperlambda AI help

If you mark some Hyperlambda code in Hyper IDE and click F1, it will invoke AINIRO's machine learning type for Hyperlambda, and actually explain your code using natural language.

![Screenshot of Hyper IDE's integrated Hyperlambda F1-based help component](/assets/images/hyperlambda-ai-help.jpeg)

## Machine learning features

Hyper IDE contains a machine learning component, similar to [SQL Studio](/dashboard/sql-studio/), that allows you to have it create code for you using AI.

![Screenshot of how to use AI to generate code in Hyper IDE](/assets/images/use-ai-to-generate-code-in-hyper-ide.jpeg)

If you use the AI chatbot interface in Hyper IDE, you can ask the AI to create, and/or modify your code, and such have _"conversations"_ with the AI about your code - And even use the AI as your _"AI-based pair programming buddy"_. Such requests will be paired to a local type with the same name as your file extension, implying if you're asking the AI to help you when you've got an HTML file open, the AI will search for a type who's name is _"html"_. If the backend does not find such a type, it will resort to using your _"default"_ type.

This allows you to create your own unique models using RAG or fine-tuning, that are matched to your file extensions, to for instance teach the AI about your own code, etc.

## Workflows and declarative programming

Probably Hyper IDE's most important feature is its ability to create code _"declaratively"_. With traditional programming you need to describe the _"how"_. Declarative programming allows you to ignore the _"how"_ and focus on the _"what"_. This trait of Hyper IDE significantly lowers the bar and makes it easier to create working software, also for people without any prior software development experience.

For instance, to invoke Stripe's API to create a subscription or a payment requires knowledge of HTTP, JSON, Stripe's API, etc. With Hyper IDE it's as easy as clicking a button and decorating an _"action"_.

![Screenshot of declarative programming with Hyper IDE allowing you to decorate an action using a graphical user interface](/assets/images/declarative-programming-with-hyper-ide.jpeg)

Actions can be chained together into workflows, where each consecutive action chains output arguments from its previous actions into input arguments to itself.

## Modules

Magic is modularized, allowing you to easily move modules from one machine to another. This is the purpose of your _"/modules/"_ folder, as in each folder inside this folder is considered a module in Magic.

If you're developing a module in your own local installation of Magic, you can mark the folder in the tree control, and click the action button for downloading the folder. This will give you a zip file you can easily upload to another server using the install module action button.

This is also horizontally integrated into [SQL Studio](/dashboard/sql-studio/), allowing you to _"export"_ your database DDL SQL to a module, assuming your module has the same name as your database. If you use this feature, Magic will automatically create your database, and even apply migration scripts if required during installation.

## Continuous Integration and Deployment

You can even connect creation of such modules, and automatically deploying them to production through for instance a GitHub action using CI/CD, by creating a token using your _"username/Generate Token"_ menu item. This give you a JWT token you can use to authenticate a process, such that it's allowed to invoke your `/magic/system/file-system/install-module` endpoint. This will allow you to automatically upload a zip file, and re-install it after uploading it.
