---
title: Hyper IDE
description: Hyper IDE is an AI-enabled integrated development environment for Hyperlambda and allows you to build APIs and backends with No-Code constructs.
header:
  image: /assets/images/hero/hyper-ide.webp
  og_image: /assets/images/hero/hyper-ide-og.png
  image_description: Editing Hyperlambda in Hyper IDE
faq:
  - q: "What is Hyper IDE?"
    a: "Hyper IDE is Magic's integrated development environment, running in your browser. It lets you browse and edit every file on your cloudlet, with syntax highlighting and autocomplete for Hyperlambda."
  - q: "Can I debug Hyperlambda in Hyper IDE?"
    a: "Yes. Click Debug instead of Invoke in the execution dialog, and Magic records every slot the file invokes, letting you step through the execution afterwards and see the entire lambda object as it looked after each step."
  - q: "Can I execute an endpoint as a particular role?"
    a: "Yes. The execution dialog has the same Run as dropdown as the Endpoints component. Choose a role and Invoke calls the endpoint with a short lived token minted for that role, so its authorisation and role checks apply as they would to a real caller. Debug always runs as you."
  - q: "Does debugging slow down my cloudlet?"
    a: "No. Recording is opt-in per execution and lives only in memory - code you run normally is completely unaffected, and nothing is written to disk."
  - q: "Can I see what happened when my code throws an exception?"
    a: "Yes, and that is where it helps most. The statement that threw is highlighted in red in both the step list and the code, and every step leading up to it is preserved - so you can see the state your code had built up at the moment it failed."
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
    a: "Yes. Every top level folder inside /modules/ and /etc/ can be its own Git repository, and each has a Git action opening a panel where you can see status, expand any changed file to read its diff, discard changes per file or for the whole repository, commit, push, pull, fetch, and manage branches. Folders that aren't repositories yet can be initialized or cloned into. Commits are attributed to your profile's name and email, and GitHub authentication uses a personal access token from your configuration."
  - q: "Can I build full stack apps with Hyper IDE?"
    a: "Yes. Your cloudlet serves static files from /etc/www/, and the AI bar generates HTML, CSS and JavaScript too - so you can generate a frontend in plain English, wired to the CRUD API the Endpoint Generator created for your database, and host it straight from your cloudlet."
  - q: "How do I move a module to another server?"
    a: "Two ways; download the module folder as a zip and install it on the other server with the install module action - or push the module to GitHub with Hyper IDE's Git support and clone it into the other cloudlet, which also gives you history, branches and rollback."
  - q: "What does F1 do?"
    a: "F1 asks the integrated AI to explain the Hyperlambda code you have selected, giving you instant help understanding unfamiliar code."
  - q: "What keyboard shortcuts does the dashboard support?"
    a: "Ctrl+K opens a command palette jumping to any page, file, endpoint, task or model, Ctrl+. opens Chat Ops, and Ctrl+/ shows an overview of every shortcut - including the editor shortcuts for autocomplete, search, fullscreen, save, execute, and Hyper IDE's file actions."
moved_anchors: {"cloning-an-existing-github-repository": "/dashboard/hyper-ide/git-and-deployment/#cloning-an-existing-github-repository", "continuous-integration-and-deployment": "/dashboard/hyper-ide/git-and-deployment/#continuous-integration-and-deployment", "creating-full-stack-apps": "/dashboard/hyper-ide/ai-generation/#creating-full-stack-apps", "editing-web-pages-and-static-files": "/dashboard/hyper-ide/files-and-modules/", "executing-hyperlambda-from-hyper-ide": "/dashboard/hyper-ide/editor/#executing-hyperlambda-from-hyper-ide", "generating-code-with-ai": "/dashboard/hyper-ide/ai-generation/#generating-code-with-ai", "git-support": "/dashboard/hyper-ide/git-and-deployment/", "hyper-ide-features": "/dashboard/hyper-ide/editor/#hyper-ide-features", "integrated-hyperlambda-ai-help": "/dashboard/hyper-ide/ai-generation/#integrated-hyperlambda-ai-help", "keyboard-shortcuts": "/dashboard/hyper-ide/editor/", "modules": "/dashboard/hyper-ide/files-and-modules/#modules", "moving-around": "/dashboard/hyper-ide/editor/#moving-around", "notes": "/dashboard/hyper-ide/editor/#notes", "publishing-a-module-as-a-new-github-repository": "/dashboard/hyper-ide/git-and-deployment/#publishing-a-module-as-a-new-github-repository", "rewind---stepping-through-an-execution": "/dashboard/hyper-ide/editor/#rewind---stepping-through-an-execution", "the-preferred-way---mcp-and-an-ai-orchestrator": "/dashboard/hyper-ide/ai-generation/", "turning-your-endpoints-into-ai-functions": "/dashboard/hyper-ide/ai-generation/#turning-your-endpoints-into-ai-functions", "when-something-throws": "/dashboard/hyper-ide/editor/#when-something-throws"}
---

Hyper IDE is your _"goto component"_ when you want to create your own modules using Magic and Hyperlambda. It's a web based IDE, allowing you to edit your code, create new modules, and contains a lot of things you're used to from a traditional IDE. It is also the natural extension of Magic's [endpoint generator](/dashboard/endpoint-generator/), since it allows you to edit the Hyperlambda endpoint files after Magic has generated your CRUD backend. In addition, Hyper IDE allows you to use AI to generate code using _"vibe coding"_ constructs.

<img src="/assets/images/hyper-ide-hl-autocomplete.webp" alt="Screenshot of editing Hyperlambda code in Hyper IDE with autocomplete triggered" loading="lazy" width="2400" height="1500">

## In this section

* [Hyper IDE - AI Code Generation](/dashboard/hyper-ide/ai-generation/): While Hyper IDE lets you write and generate code by hand, the preferred way to build with Magic is to let an AI agent do the work for you.
* [Hyper IDE - Editor, Shortcuts and Rewind](/dashboard/hyper-ide/editor/): The dashboard documents its own shortcuts - click CTRL+/ (COMMAND+/ on a Mac) anywhere, and an overview opens listing every shortcut, or find it by opening the command palette with CTRL+K and typing "
* [Hyper IDE - Files and Modules](/dashboard/hyper-ide/files-and-modules/): Hyper IDE isn't only for Hyperlambda.
* [Hyper IDE - Git and CI/CD](/dashboard/hyper-ide/git-and-deployment/): Every module can be its own Git repository, and Hyper IDE has Git built in.

{% include faq.html %}
