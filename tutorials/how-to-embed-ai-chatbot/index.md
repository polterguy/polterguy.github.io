---
title: How to embed your AI chatbot
---

When you're done with creating your machine learning type, and you've quality assured its content, it is time to embed the AI chatbot on your website. This is easily accomplished if you can somehow add a JavaScript inclusion tag on your site. All modern CMS systems have this capability, but the process differs for different platforms, so please check up your system specifically for how to achieve this before proceeding. This tutorial will explain the different query parameters and settings, allowing you to easily create the correct JavaScript embed code, but it will not dive into internals related to specific systems such as WordPress, Umbraco, or Joomla etc.

## The embed form

Your machine learning type has an _"embed"_ button. If you click this button you will be served something resembling the following.

![Embedding your AI Chatbot](/assets/images/embed-ai-chatbot-2.png)

Each setting above reflects one of the following query parameters:

* type - The full name of your machine learning type
* header - The header of the chat window
* button - The text of the chatbot button that opens the window
* rtl - Implies _"right to left"_ and allows for creating a user interface for RTL languages
* color - The color of the text in the chatbot
* start - The _"starting"_ color of the background
* end - The _"ending"_ color of the background
* link - The color of hyperlinks inside the chat window
* theme - The name of your theme / css / skin
* references - If true, will return references from the backend for training snippets having URL citations
* file - Allows for overriding the JavaScript file actually used
* placeholder - The placeholder text for the textbox field in the chat window
* position - Positioning of the chatbot button and window. Must be either _"right"_ or _"left"_
* clear_button - If true, adds a clear button, that allows the user to clear his current session and create a new session
* copyButton - If true, adds a _"copy response"_ button for every response provided by the LLM
* follow_up - If true, adds the required JavaScript parts to support follow up questions. Notice, the system instruction needs to be correctly changed for this to work
* new_tab - If true, opens up all hyperlinks in a new browser tab
* code - If true, will add the required logic to syntax highlight code when the LLM returns code segments
* animation - Allows for referencing an animation CSS selector. Notice, currently only _"ainiro_blink"_ is supported, which you can see on our website
* popup - _"Popup text"_ that's shown 5 seconds after the AI chatbot loads, to make it slightly more _"instrusive"_ and visible. Check our website for an example
* hidden - If true, displays the chatbot's button invisible, allowing you to create your own chatbot button to trigger the actual chatbot window
* sticky - If true, will automatically reopen the chatbot when the user is navigating to a new page, and the chatbot was already visible on the previous page
* attachments - If true, allows your users to attach files and upload these to the LLM
* extra - Additional extra parameters, which can be anything, and is typically used for complex integrations where _"instance information"_ is required on a _"per chatbot window"_ basis

Most of the above query parameters have a GUI equivalent in the embed screen as seen in the above screenshot. Let's dive into some of the most important settings from above and see how they change your AI chatbot's look and feel.

## The colors of your AI chatbot

The AI chatbot is actually using _two_ background colors. These two colors are extrapolated as a linear gradient typically, allowing you to create a _"gradient effect"_ if you wish. The `start` setting is the top color and the `end` setting is the color the gradient will end on.

It is typically smart to use lighter colors as your `start` value and heavier or darker colors in the same spectrum as your `end` value. This creates a _"sun effect"_ and resembles the way things are in real life, since the sun always shines from the top, making darker colors further down in the same object. Exactly how these colors are being used, varies from theme to theme, but below you can see how the _"bubbles"_ theme uses these colors.

![Gradient backgroun color in your AI chatbot](/assets/images/bubbles-theme-gradients.png)

The `link` setting again is for hyperlinks, allowing you to provide a hexadecimal value, that becomes the color of hyperlinks inside the chatbot window. The `color` setting is for plain text. Both of these requires hex values, such as for instance `#fefefe` which is off white.
