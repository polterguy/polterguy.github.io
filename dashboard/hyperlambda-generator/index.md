---
title: Hyperlambda Generator
description: Magic contains a Hyperlambda AI-based generator, allowing you to create your backend APIs using natural language.
og_image: "/images/custom-chatgpt-chatbot.jpg"
header:
  image: /assets/images/wizard-magically-pulling-ai-chatbots-our-of-cauldron.webp
---

Magic contains its own Hyperlambda Generator. This isn't a single component, but goes through most parts of the platform that somehow allows you to create Hyperlambda code. It's built as a custom LLM we have fine tuned on top of OpenAI's GPT-4.1 model, with more than 20,000 training examples, so it's actually very strong on creating backend code, even though it's using a _"small base model"_.

![Screenshot of the Hyperlambda Generator creating an HTTP CRUD endpoint](/assets/images/hyperlambda-generator.png)

You have to write _"formal specifications using technical language"_, in order for it to understand what to do. But if you've got some basic knowledge about software development, you should be able to rapidly understand how to use it. Below are some examples of prompts to give you an ide.

* _"HTTP endpoint that selects rows from Artist table in chinook database, including Album rows for each individual artist. Use ArtistId as foreign key"_
* _"Executable Hyperlambda file that send an email using [name], [email], [subject], and [body] arguments. Endpoint can only be executed by root and admin accounts"_

## How to use it

If you go to Hyper IDE for example, and you create a new Hyperlambda file (extension ".hl"), then a popup dialog will ask you to provide a description and arguments. If you write what you want the code to do for you, and you click _"Save & Generate"_, the description will be sent through our LLM, transforming your English to working Hyperlambda.

**DISCLAIMER** - Magic and Hyperlambda isn't really an _"all purpose language"_, it's an orchestration language. If you're using it for complex algorithms, you're doing something wrong. So whatever description you supply, must be comething that is a good fit for Hyperlambda. Below is the result for the above prompt from the screenshot.

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

## Modifying your code with AI

Below your main code view in Hyper IDE and the Hyperlambda Playground, you can see an input textbox that says _"Where the Machine Creates the Code"_. This bar allows you to provide change instructions to the LLM. Examples of prompts you might want to test can be found below.

* Add a name argument and use this when sending the email
* Make the title argument mandatory
* Log all incoming arguments
* Etc ...
