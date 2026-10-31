---
title: Machine Learning
description: Create your own machine-learning model in Magic by scraping any website into RAG training data, answering domain questions with vector search.
header:
  image: /assets/images/hero/machine-learning.webp
  og_image: /assets/images/hero/machine-learning-og.png
  image_description: Machine Learning models
faq:
  - q: "What is the Machine Learning component in Magic?"
    a: "It allows you to create your own private AI models by crawling websites or uploading files, turning the content into RAG training data. Under the hood it uses OpenAI, combined with RAG and VSS towards your own database, giving you accurate, domain specific answers without your data ever leaving your cloudlet's database."
  - q: "Can I import files to my model?"
    a: "Yes. Click Import on your model and either crawl a website, or upload files in a wide variety of formats - XML, JSON, YAML, CSV, PDF and more. Each file is turned into training snippets automatically."
  - q: "How do I create an AI chatbot from my website?"
    a: "Create a model, click Import, provide your website's URL, and Magic crawls and scrapes the site, turning every page into training data. For an even faster start, the Chatbot Wizard on the dashboard's landing page does all of this with one click."
  - q: "What is a training snippet?"
    a: "One atomic piece of information, consisting of a prompt and a completion. When answering a question, Magic picks the most relevant snippets - potentially from many different sources - and transmits them as context to OpenAI, which answers using only that context."
  - q: "Can an AI agent remember things between sessions?"
    a: "Yes. Connected over MCP, an agent can save anything worth keeping - a fact, a preference, a decision, or reusable Hyperlambda - as a training snippet with create-memory, and find it again later with search-memory, which combines keyword search and search by meaning. Memories go into the default type unless you name another one, and every connected tool sees the same ones."
  - q: "What does Vectorize do, and why do I need it?"
    a: "Vectorising creates embeddings for your training snippets, enabling VSS (Vector Similarity Search) to find the most relevant snippets for each question. You must click Vectorize on your model after importing training data, before the model can be used."
  - q: "Does my chatbot hallucinate?"
    a: "RAG and VSS drastically reduce hallucinations, since the model answers exclusively from your own training data instead of inventing facts. This also makes it significantly less expensive than fine-tuning."
  - q: "Can I edit or clean training snippets after importing?"
    a: "Yes. Every snippet can be edited manually, and the snippet editor has its own AI bar allowing you to clean, reformat, or compress individual snippets with a plain English instruction - the AI transforms the snippet and writes the result back for you."
  - q: "Can I search through my training data?"
    a: "Yes, both with plain text filtering and with Vector search, which finds snippets by meaning rather than keywords - useful for verifying what context your model would use for a particular question."
  - q: "What are widgets?"
    a: "Micro apps rendered inside the chat stream itself - forms, calculators, booking widgets, and similar. You add them from the training data tab, and the chatbot displays them in the middle of the conversation when a user's question matches the widget's prompt."
  - q: "What are AI functions?"
    a: "Installable functions that turn your model into an AI agent - allowing the chatbot to query your database, trigger workflows, or create training snippets, according to instructions provided by the user in natural language."
  - q: "How do I embed my chatbot on my website?"
    a: "Click Embed on your model, configure theme, colours, position and behaviour, and copy the generated script tag into your website's HTML. The chatbot then runs on your site, answering from your training data."
  - q: "Can I monitor what users ask my chatbot?"
    a: "Yes. The History tab stores questions and answers, letting you review and improve your model over time - and use historical requests for business intelligence or lead generation. Supervised models can also be corrected by editing bad answers into new training data."
moved_anchors: {"adding-hyperlambda-code-to-training-snippets": "/dashboard/machine-learning/training-snippets/#adding-hyperlambda-code-to-training-snippets", "ai-functions": "/dashboard/machine-learning/ai-functions/", "configuring-your-model": "/dashboard/machine-learning/models/#configuring-your-model", "count-albums": "/dashboard/machine-learning/ai-functions/#count-albums", "crawling-your-website": "/dashboard/machine-learning/crawling/", "history-tab": "/dashboard/machine-learning/memory-and-history/#history-tab", "managing-your-training-snippets": "/dashboard/machine-learning/training-snippets/#managing-your-training-snippets", "memory---what-ai-agents-remember": "/dashboard/machine-learning/memory-and-history/", "models": "/dashboard/machine-learning/models/", "periodically-re-crawl-site": "/dashboard/machine-learning/crawling/#periodically-re-crawl-site", "spicing": "/dashboard/machine-learning/crawling/#spicing", "training-snippets": "/dashboard/machine-learning/training-snippets/", "widgets": "/dashboard/machine-learning/training-snippets/#widgets"}
---

Magic's Machine Learning component allows you to create your own AI based machine learning model, either by crawling your website and scraping it for data, or by manually uploading files, resulting in a private and custom _"machine learning model"_. Machine learning in Magic is built upon OpenAI's API and is similar to ChatGPT, and under the hood it's using RAG and VSS towards your own database to extract context as it's answering questions using OpenAI.

<img src="/assets/images/machine-learning-component.webp" alt="Screenshot of the Machine Learning component showing a model&#x27;s training data" loading="lazy" width="2400" height="1500">

Magic contains a lot of additional services, such as the ability to monitor or supervise usage, storing questions and answers into your database, and use these to review and improve your model's accuracy over time. You can also use historical requests for business intelligence, or lead generation. In addition it ties into Magic's AI Agent abilities, allowing you to integrate AI functions triggering AI workflows from instructions provided by the user.

You can crawl and scrape your website for training data, or upload your own files in a wide variety of formats, such as XML, JSON, YAML, CSV, or PDF. Magic uses RAG/VSS to power your model, which eliminates AI hallucinations, resulting in higher accuracy, and is also significantly less expensive.

## In this section

* [Crawling Your Website](/dashboard/machine-learning/crawling/): To crawl and scrape your website, create a model, then click the "Import" button on your model, and provide it with your website's URL.
* [Models and Configuration](/dashboard/machine-learning/models/): A "model" is a collection of training snippets.
* [Training Snippets](/dashboard/machine-learning/training-snippets/): Magic uses RAG for your machine learning model, which we recommend for 99% of our clients.
* [AI Functions](/dashboard/machine-learning/ai-functions/): This is a subject on its own, but basically a machine learning model has the ability to execute AI functions.
* [Memory and History](/dashboard/machine-learning/memory-and-history/): A training snippet is just a prompt and a completion, which makes it a good place for an AI agent to keep what it learns.

## Use cases

* Expert law system, answering legal questions for your clients
* Medical expert advice system based upon AI and machine learning, giving you help when diagnosing patients and clients
* Support chatbot for your company, giving your clients support for whatever questions they might have
* Automated sales expert systems, converting leads on your website into paying clients
* Cognitive assistants, helping your employees with some specific task at hand
* AI Agents serving as AI assistants performing tasks for you according to your instructions

The advantage of creating your own Machine Learning model is that you can create a private and custom AI chatbot. This can become a much _"sharper"_ intelligence than the publicly available ChatGPT, with knowledge about your particular problem domain, problems ChatGPT is not able to correctly provide answers to.

To understand what I mean here go to [ChatGPT](https://chat.openai.com) and ask it about your company. Chances are that ChatGPT has no idea how to answer your questions correctly. If you scrape your company's website, and/or upload your own training data, you could create a _"custom version of ChatGPT"_, that is able to answer support requests, and/or convince leads and potential clients to become
paying customers, etc. This is of course _impossible_ with the general ChatGPT implementation, but can sometimes be created in some few minutes using Magic Cloud.

This is one of the primary services [AINIRO.IO](https://ainiro.io) is providing, and we have a lot of experience with building high quality AI chatbots. If you want us to create you a chatbot, you can [create a demo chatbot on our website](https://ainiro.io), or [contact us here](https://ainiro.io/contact-us).

## A Machine Learning platform

Magic's machine learning component is actually horizontally implemented into almost every single component in Magic. Need to use AI from [SQL Studio](/dashboard/sql-studio/), no problem, it's an integrated feature. The same is true for [Hyper IDE](/dashboard/hyper-ide/),
and even help is implemented using OpenAI and ChatGPT. If you need help with some [Hyperlambda](/hyperlambda/) code, just mark it in Hyper IDE and click F1, which will use AI to explain what the code does.

<img src="/images/hyperlambda-ai-help.webp" alt="Screenshot of clicking F1 and have OpenAI explain some Hyperlambda code" loading="lazy" width="2400" height="1500">

You can also use OpenAI to generate code for you. Both Hyper IDE and SQL Studio have a little textbox at the bottom that says _"Where the machine creates the code."_ If you add some piece of instruction here, Magic will invoke OpenAI with your prompt and generate code according to your instructions.

### Magic's integrated support chatbot

In addition, Magic integrates a support chatbot directly into its dashboard. This provides you with integrated help directly from the dashboard. Click the AI chatbot button at the bottom of the navigation sidebar to access this chatbot.

<img src="/assets/images/integrated-chatbot.webp" alt="Screenshot of Magic&#x27;s integrated support chatbot" loading="lazy" width="2400" height="1500">

{% include faq.html %}
