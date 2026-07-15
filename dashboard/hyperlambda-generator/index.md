---
title: Hyperlambda Generator
description: The Hyperlambda Generator is a proprietary SLM fine-tuned with more than 600,000 training snippets, transforming natural language into working backend code in seconds, without hallucinating function invocations.
og_image: "/images/custom-chatgpt-chatbot.jpg"
header:
  image: /assets/images/wizard-magically-pulling-ai-chatbots-our-of-cauldron.webp
---

Magic contains its own Hyperlambda Generator. This isn't a single component, but goes through most parts of the platform that somehow allow you to create Hyperlambda code. It's built as our own proprietary SLM (Small Language Model), fine-tuned with more than 600,000 training snippets, so it's actually very strong on creating backend code, even though it's using a _"small base model"_.

![Screenshot of the Hyperlambda Generator creating an HTTP CRUD endpoint](/assets/images/hyperlambda-generator.png)

## What makes it different

* **It's fast** - Since it's a small model, it typically generates your code in 1.5 to 5 seconds, allowing you to iterate rapidly, and allowing AI agents to create tools without noticeable delay.
* **It cannot hallucinate function invocations** - Every slot the generated code invokes is verified against the slots that actually exist in your cloudlet before the code is returned. If the model invokes something that doesn't exist, the code is rejected and regenerated - You will never be handed code invoking made-up functions.
* **It's trained exclusively on Hyperlambda** - More than 600,000 training snippets covering the entire platform; database access, HTTP endpoints, authentication, validation, email, file handling, scheduling, etc.
* **It's built for AI agents** - The generator is available over the [MCP server](/tutorials/how-to-connect-the-mcp-server/), allowing a connected AI agent such as Claude to create new endpoints - and hence new tools for itself - on demand.

You have to write _"formal specifications using technical language"_, in order for it to understand what to do. But if you've got some basic knowledge about software development, you should be able to rapidly understand how to use it. Below are some examples of prompts to give you an idea.

* _"HTTP endpoint that selects rows from Artist table in chinook database, including Album rows for each individual artist. Use ArtistId as foreign key"_
* _"Executable Hyperlambda file that sends an email using [name], [email], [subject], and [body] arguments. Endpoint can only be executed by root and admin accounts"_

## How to use it

If you go to Hyper IDE for example, and you create a new Hyperlambda file (extension ".hl"), then a popup dialog will ask you to provide a description and arguments. If you write what you want the code to do for you, and you click _"Save & Generate"_, the description will be sent through our LLM, transforming your English to working Hyperlambda.

**DISCLAIMER** - Magic and Hyperlambda isn't really an _"all purpose language"_, it's an orchestration language. If you're using it for complex algorithms, you're doing something wrong. So whatever description you supply, must be something that is a good fit for Hyperlambda. Below is the result for the above prompt from the screenshot.

```text
/*
 * Endpoint: chinook.artist.read
 * Purpose: Reads artists from chinook database, including albums for each artist.
 * Access: Root users only.
 */
.arguments
auth.ticket.verify:root
data.connect:chinook
   data.read
      table:Artist
   include:x:@data.read/*
      data.read
         table:Album
         where
            and
               ArtistId.eq:x:@.dp/#/*/ArtistId
      yield
         albums:x:@data.read/*
   yield
      artists:x:@data.read/*
```

Notice, if the AI creates wrong code, you can press `CTRL+Z` or `OPTION+Z` on a Mac to undo the generator's changes, at which point you can start over again by pressing `OPTION+Q` or `ALT+Q`, allowing you to edit the text to be more specific.

## Modifying your code with AI

Below your main code view in Hyper IDE and the Hyperlambda Playground, you can see an input textbox that says _"Where the Machine Creates the Code"_. This bar allows you to provide change instructions to the LLM. Examples of prompts you might want to test can be found below.

* Add a name argument and use this when sending the email
* Make the title argument mandatory
* Log all incoming arguments
* Etc ...
