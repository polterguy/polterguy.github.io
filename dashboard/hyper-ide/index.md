---
title: Hyper IDE
description: Hyper IDE is an AI-enabled integrated development environment for Hyperlambda and allows you to build APIs and backends with No-Code constructs.
header:
  image: /assets/images/hero/hyper-ide.webp
  og_image: /assets/images/hero/hyper-ide-og.png
  image_description: Editing Hyperlambda in Hyper IDE
faq:
  - q: "What is Hyper IDE?"
    a: "Hyper IDE is Magic's integrated development environment, running in your browser. It lets you browse and edit every file on your server, with syntax highlighting and autocomplete for Hyperlambda."
  - q: "Can Hyper IDE generate code for me using AI?"
    a: "Yes. Write a description of what you want your code to do, select it, and click Generate - or use the 'Where the Machine Creates the Code' bar below the editor. The Hyperlambda Generator transforms your English into working Hyperlambda in seconds."
  - q: "Is the AI code generation free?"
    a: "For Hyperlambda files, yes - generation goes through Magic's own proprietary model and requires no OpenAI API key. Other languages such as TypeScript, HTML and SQL are generated through OpenAI and require an API key in your configuration."
  - q: "How do I test my code?"
    a: "Since Hyperlambda is a dynamic language, you can save your file and immediately execute it by clicking F5, without compiling anything. If your code requires arguments, Hyper IDE asks you for them before executing."
  - q: "What is the preferred way to build with Magic?"
    a: "Connecting an orchestrator AI - such as Claude, Cursor, Codex or Qoder - to your cloudlet over MCP, and letting the agent generate endpoints, create database schemas, and deploy modules for you. Hyper IDE then becomes where you inspect, tweak, and debug what the agent produced."
  - q: "Can I edit other languages than Hyperlambda?"
    a: "Yes, you can edit TypeScript, Ruby, HTML, C# and other file types, although for those languages a dedicated IDE will typically serve you better. Hyper IDE's strength is Hyperlambda."
  - q: "Does Hyper IDE have Git support?"
    a: "Yes. Every top level folder inside /modules/ and /etc/ can be its own Git repository, and each has a Git action opening a panel where you can see status, commit, push, pull, fetch, and manage branches. Folders that aren't repositories yet can be initialized or cloned into. Commits are attributed to your profile's name and email, and GitHub authentication uses a personal access token from your configuration."
  - q: "Can I build full stack apps with Hyper IDE?"
    a: "Yes. Your cloudlet serves static files from /etc/www/, and the AI bar generates HTML, CSS and JavaScript too - so you can generate a frontend in plain English, wired to the CRUD API the Endpoint Generator created for your database, and host it straight from your cloudlet."
  - q: "How do I move a module to another server?"
    a: "Two ways; download the module folder as a zip and install it on the other server with the install module action - or push the module to GitHub with Hyper IDE's Git support and clone it into the other cloudlet, which also gives you history, branches and rollback."
  - q: "What does F1 do?"
    a: "F1 asks the integrated AI to explain the Hyperlambda code you have selected, giving you instant help understanding unfamiliar code."
---

Hyper IDE is your _"goto component"_ when you want to create your own modules using Magic and Hyperlambda. It's a web based IDE, allowing you to edit your code, create new modules, and contains a lot of things you're used to from a traditional IDE. It is also the natural extension of Magic's [endpoint generator](/dashboard/endpoint-generator/), since it allows you to edit the Hyperlambda endpoint files after Magic has generated your CRUD backend. In addition, Hyper IDE allows you to use AI to generate code using _"vibe coding"_ constructs.

<img src="/assets/images/hyper-ide-hl-autocomplete.webp" alt="Screenshot of editing Hyperlambda code in Hyper IDE with autocomplete triggered" loading="lazy" width="2400" height="1500">

## The preferred way - MCP and an AI orchestrator

While Hyper IDE lets you write and generate code by hand, the _preferred_ way to build with Magic is to let an AI agent do the work for you. Magic exposes an [MCP server](/tutorials/how-to-connect-the-mcp-server/), and the recommended workflow is to connect an orchestrator AI - such as Claude, Cursor, Codex, Qoder, or any other MCP-capable harness - to your cloudlet, and use Magic as that agent's development _and_ deployment platform. Over the same MCP connector the agent can discover your endpoints, generate new Hyperlambda, create database schemas, wire up modules, and deploy them straight into production on your cloudlet. Hyper IDE then becomes the place where you inspect, tweak, and debug what the agent produced.

## Generating code with AI

At the bottom of Hyper IDE's editor you'll find a bar labelled _"Where the Machine Creates the Code"_. Type an instruction here in plain English, click _"Ask"_, and Magic generates or modifies your code according to your instructions - similar to how GitHub CoPilot works.

<img src="/assets/images/use-ai-to-generate-code-in-hyper-ide.webp" alt="Screenshot of how to use AI to generate code in Hyper IDE" loading="lazy" width="2400" height="1500">

Which engine answers depends on the file you have open.

* **Hyperlambda files (`.hl`)** are generated by Magic's own [Hyperlambda Generator](/dashboard/hyperlambda-generator/). Currently this requires _no_ OpenAI API key and is _free of charge_ - the generator is our proprietary model, fine-tuned exclusively on Hyperlambda.
* **Other languages** - such as TypeScript, JavaScript, HTML, CSS, and SQL - are generated through OpenAI, and therefore require you to have an OpenAI API key installed in your cloudlet's configuration.

You can also select some text in the editor and click the _"Generate"_ button to run your selection through the generator, or write a file-level comment describing what you want and generate your code from that.

The bar works like a conversation, so you can keep refining and modifying your code, using it as an _"AI-based pair programming buddy"_. Requests are paired to a local machine learning type with the same name as your file's extension - so with an HTML file open the AI searches for a type named _"html"_, falling back to your _"default"_ type if none exists. This lets you create your own RAG models, matched to your file extensions, to teach the AI about your own code.

Hyper IDE also provides integrated autocomplete if your editor has focus and you click CTRL+SPACE in Windows or FN+CONTROL+SPACE on your Mac. This allows you to very rapidly create Hyperlambda code, while having Hyper IDE ensure your code is using existing slots. Notice, these keyboard shortcuts are only available when your code editor has focus.

In addition to autocomplete, the editor documents your code as you read it - rest your mouse pointer on any slot invocation in a Hyperlambda file, and a tooltip appears explaining what the slot does, using the descriptions your cloudlet's slots declare about themselves. And CTRL+F on Windows or COMMAND+F on your Mac opens search inside the editor, highlighting every match as you type, with ENTER cycling through them - which matters once your Hyperlambda files grow to hundreds of lines.

<img src="/images/hyper-ide-actions.webp" alt="Screenshot of Hyper IDE&#x27;s autocomplete feature with Hyperlambda" loading="lazy" width="2400" height="1500">

## Hyper IDE features

Hyper IDE is not a fully fledged IDE, and cannot compare to something like VS Code or Visual Studio. However, its purpose is to function as an extension on top of the endpoint generator, giving you code editing capabilities of your generated Hyperlambda files - In addition to rapidly allowing you to edit Hyperlambda files and use AI to generate or modify existing code.

You _can_ use Hyper IDE to edit TypeScript, Ruby, HTML, and C# code, but we don't recommend replacing it with your existing code editor, since other IDEs have much more features here than Hyper IDE. However, the opposite is also true, implying Hyper IDE has features your existing IDE does not have - Especially in regards to [Hyperlambda](/hyperlambda/).

Another benefit is that Hyperlambda is a dynamic programming language, implying once you've saved your Hyperlambda files, you can immediately test your code by executing it from within Hyper IDE by clicking F5. This results in a much tighter development model than a traditional compiled programming language gives you, making it much faster to find bugs and create working code.

If you execute code in immediate mode using F5, and your code requires arguments, Hyper IDE will ask you for what to pass in as arguments. This isn't perfect, and only works for first level arguments - But if you need more complexity, you can always use the [Hyperlambda Playground](/dashboard/hyperlambda-playground/), and/or the [Endpoints Component](/dashboard/endpoints/).

Magic does not separate between code creation and your code's production environment, providing you with instant feedback as you create your code.

Hyper IDE also remembers which files you had open, per cloudlet - sign out, come back tomorrow, and your workspace opens the way you left it, with the same files in the same tabs.

## Executing Hyperlambda from Hyper IDE

Hyper IDE allows you to execute Hyperlambda without ever leaving your IDE by clicking the _"Execute"_ button. This makes it easy for you to test your code as you are creating it, and is the closest you come to the equivalent of a _"debugger"_ in Magic. When executing an API endpoint file, you can parametrise the invocation, and the result is shown with its HTTP status code, execution time, and response body.

<img src="/assets/images/hyper-ide-execute-endpoint.webp" alt="Screenshot of executing an API endpoint from Hyper IDE, showing the response" loading="lazy" width="2400" height="1500">

## Integrated Hyperlambda AI help

If you mark some Hyperlambda code in Hyper IDE and click F1, it will invoke AINIRO's machine learning type for Hyperlambda, and actually explain your code using natural language.

<img src="/assets/images/hyperlambda-ai-help.webp" alt="Screenshot of Hyper IDE&#x27;s integrated Hyperlambda F1-based help component" loading="lazy" width="2400" height="1500">

## Creating full stack apps

Hyper IDE isn't limited to backend code - you can create complete full stack applications from it. Since your cloudlet serves static files from `/etc/www/`, and the _"Where the Machine Creates the Code"_ bar generates HTML, CSS and JavaScript too, you can describe the frontend you want in plain English and have the AI build it - wired straight to the CRUD API the [Endpoint Generator](/dashboard/endpoint-generator/) created for your database. The CRM app below was built exactly this way; a SQLite database with 3 tables, a secure API wrapping it, and a working frontend - all generated from natural language.

<img src="/assets/images/home-grown-app.webp" alt="A full stack CRM app with clients, notes and emails, generated from natural language" loading="lazy" width="2436" height="1334">

## Turning your endpoints into AI functions

Hyper IDE also bridges your code and your [Machine Learning models](/dashboard/machine-learning/). Every Hyperlambda endpoint file has a _"Create AI function"_ action, adding that endpoint as an AI function to a model you select - allowing your chatbot or AI agent to invoke it. Folders have the same action, converting _all_ Hyperlambda endpoint files inside the folder into AI functions in one go. Endpoint files also have an _"OpenAPI"_ action, showing you the endpoint's OpenAPI specification.

<img src="/assets/images/hyper-ide-create-ai-function.webp" alt="Screenshot of creating an AI function from a Hyperlambda file, adding it to a machine learning model" loading="lazy" width="2400" height="1500">

## Editing web pages and static files

Hyper IDE isn't only for Hyperlambda. Anything you place under the `/etc/www/` folder is served directly from the root of your cloudlet's domain by the backend, which turns Magic into a web server too. A file saved as `/etc/www/index.html` is served from your site's root, `/etc/www/css/main.css` from `/css/main.css`, and so on. This means you can host a landing page, a complete static website, or the HTML, CSS and JavaScript assets for a single-page application straight from your cloudlet, right next to the APIs that power it. Notice, hidden files and folders - those starting with a dot - are _not_ served, with the exception of `.well-known`, which the backend deliberately exposes so discovery documents remain publicly reachable.

You edit these files the same way you edit any other file in Hyper IDE. Create or open an HTML, CSS, JavaScript, Markdown, or image file underneath `/etc/www/`, and edit it either the good old fashioned way by typing, or with the AI constructs described above - the _"Where the Machine Creates the Code"_ bar and the _"Generate"_ button work for HTML, CSS and JavaScript too. Since these are not Hyperlambda, they're generated through OpenAI, so they require an OpenAI API key in your configuration.

<img src="/assets/images/hyper-ide-editing-web.webp" alt="Screenshot of editing a static web file underneath /etc/www/ in Hyper IDE" loading="lazy" width="2400" height="1500">

When you're editing a file that lives under `/etc/www/`, Hyper IDE gives you a _"Preview"_ action on the file, that opens the served page in a new browser tab, allowing you to see your changes exactly as a visitor to your site would.

## Modules

Magic is modularized, allowing you to easily move modules from one machine to another. This is the purpose of your _"/modules/"_ folder, as in each folder inside this folder is considered a module in Magic.

If you're developing a module in your own local installation of Magic, you can mark the folder in the tree control, and click the action button for downloading the folder. This will give you a zip file you can easily upload to another server using the install module action button.

## Git support

Every module can be its own Git repository, and Hyper IDE has Git built in. Top level folders inside your _"/modules/"_ and _"/etc/"_ folders are treated as repository roots, and hovering such a folder in the tree reveals its action buttons - the branch icon opens the Git panel for that module.

<img src="/assets/images/hyper-ide-git-actions.webp" alt="Screenshot of a module folder&#x27;s action buttons in Hyper IDE&#x27;s file tree, with the Git branch icon among them" loading="lazy" width="2400" height="1500">

For a folder that already is a repository, the panel shows which branch you're on, whether you're ahead of or behind your remote, and every modified and untracked file. From here you can commit all changes with a message, push and pull, fetch from your remote, switch branches, and create new branches. Buttons that cannot possibly work in the repository's current state are disabled - push for instance is only enabled when you actually have commits your remote doesn't.

<img src="/assets/images/hyper-ide-git.webp" alt="Screenshot of Hyper IDE&#x27;s Git panel, showing branch, tracking status and commit actions for a module" loading="lazy" width="2400" height="1500">

Before your first commit, add your GitHub username and a fine-grained personal access token with _"Contents"_ read and write access to your configuration. Open the _"Configuration"_ screen, click the hamburger menu at the top, and choose _"Git…"_ to get a dialog doing this for you.

<img src="/assets/images/hyper-ide-git-settings.webp" alt="Screenshot of the Git settings dialog on the Configuration screen, with GitHub username, token and host" loading="lazy" width="1180" height="1000">

Authentication is injected per invocation over HTTPS; nothing is ever written to the server's global Git configuration, and no SSH keys are involved. Commits are attributed to _you_ - the author name and email are resolved from the authenticated user's profile, so commits made from Hyper IDE show up on GitHub with your name on them, not some shared server identity.

### Publishing a module as a new GitHub repository

To turn an existing module into a brand new GitHub repository, hover the module's folder and click the Git action. If the folder isn't a repository yet, click _"Initialize repository"_ first, then write a commit message and click _"Commit"_. With your first commit in place, click _"Publish to GitHub…"_, and give your new repository a name - it defaults to the module's folder name.

<img src="/assets/images/hyper-ide-git-publish.webp" alt="Screenshot of publishing a module to GitHub from Hyper IDE, prompting for the new repository&#x27;s name" loading="lazy" width="2400" height="1500">

One click later your module exists as a _private_ repository on GitHub, wired up as the module's _"origin"_ remote, with your commit pushed and upstream tracking configured - the panel creates the repository, adds the remote, and pushes in one go. Flip the repository to public on GitHub if that's what you want. Notice, _creating_ repositories requires the account level repository creation permission on your access token, in addition to the _"Contents"_ permission that reading and writing them needs.

### Cloning an existing GitHub repository

To deploy a module you already version control on GitHub, create a new _empty_ folder inside _"/modules/"_ using the new folder action, then open the Git panel on it. A folder that isn't a repository offers you two paths - cloning into it, or initializing it as a new repository. _"Clone into folder"_ is only enabled while the folder is empty, since Git refuses to clone into a folder with existing contents.

<img src="/assets/images/hyper-ide-git-init.webp" alt="Screenshot of Hyper IDE&#x27;s Git panel on a folder that is not yet a repository, offering clone and initialize actions" loading="lazy" width="2400" height="1500">

Click _"Clone into folder"_ and paste the repository's HTTPS URL - cloning checks out whatever the remote's default branch is, and your module is running on the cloudlet with its full history attached.

<img src="/assets/images/hyper-ide-git-clone.webp" alt="Screenshot of cloning a GitHub repository into a module folder in Hyper IDE, prompting for the HTTPS URL" loading="lazy" width="2400" height="1500">

Since modules are self-contained folders, this gives you version control per module; develop a module on one cloudlet, publish it to GitHub, and clone it into another cloudlet - a natural companion to the zip-based module install described above, with history, branches and rollback included.

## Continuous Integration and Deployment

You can even connect creation of such modules, and automatically deploying them to production through for instance a GitHub action using CI/CD, by creating a token using the _"Generate token"_ feature on your Profile screen. This gives you a JWT token you can use to authenticate a process, such that it's allowed to invoke your `/magic/system/file-system/install-module` endpoint. This will allow you to automatically upload a zip file, and re-install it after uploading it.

{% include faq.html %}
