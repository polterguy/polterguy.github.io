---
title: Machine Learning
description: Magic allows you to automatically generate your own private AI based Machine Learning model based upon OpenAI and ChatGPT
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/machine-learning.jpg"
---

Magic's Machine Learning component allows you to create your own AI based machine learning model, either by
crawling your website scraping it for data, or by manually uploading your own training data, resulting in a private
and custom _"machine learning model"_. Machine learning in Magic is built upon OpenAI's
ChatGPT, and contains a lot of additional services, such as the ability to monitor or supervise usage, storing
questions and answers into your database, and use these as the foundation for reinforced learning to improve
its accuracy.

![Magic's Machine Learning parts](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/machine-learning.jpg)

You can crawl your website for training data, or upload your own training data in a wide variety of formats,
such as XML, JSON, YAML, CSV, or PDF.

## Use cases

* Expert law system, answering legal questions for your clients
* Medical expert advice system based upon AI and machine learning, giving you help when diagnosing patients and clients
* Support chat bot for your enterprise, giving your client support for whatever questions they might have
* Automated sales expert systems, converting leads on your website into paying clients
* Cognitive assistants, helping your employees with some specific task at hand

The advantage with creating your own Machine Learning model, is that you can create a private and custom artificial
intelligence. This can become a much _"sharper"_ intelligence than the publicly available ChatGPT AI, with
knowledge about your particular problem domain, that the generally available ChatGPT implementation is not
able to provide answers to.

To understand what I mean here go to [ChatGPT](https://chat.openai.com) and ask it about your
company. Chances are that ChatGPT have no idea how to answer your questions correctly. If you scrape your
company's website, and/or upload your own training data, you could create a custom version of ChatGPT that
is able to answer support requests, and/or convince leads and potential clients to become
paying customers, etc. This is of course _impossible_ with the general ChatGPT implementation, but
can sometimes be created in some few minutes using Magic Cloud.

This is one of the primary services [AINIRO.IO](https://ainiro.io) is providing, and we have a lot of experience with building high quality AI chatbots. If you want us to create you a chatbot, you can create a demo chatbot at the previous link, or [contact us here](https://ainiro.io/contact-us).

## How the crawler works

You can upload training data in a wide variety of formats. However, most interestingly for most is that
you can simply point Magic at your website, and it will crawl your website, and scrape it for training data
that you can later use to train your own OpenAI model, or consume using RAG.

The way the crawler works, is by first checking if your website has a sitemap file. If your site has a sitemap,
it will retrieve all pages referenced in your sitemap file(s). Once it has retrieved an HTML document, it
will chop the HTML into multiple _"training snippets"_, where each Hx element becomes a prompt, and all
paragraphs below your Hx element becomes its completion. It will also preserve bulleted lists and
numbered lists, and unless it's traversing a sitemap, it will also extract all hyperlinks in your page,
and follow hyperlinks it finds to retrieve additional documents for its scraping process.

This process resembles the process Google and other search engines are following as they crawl your site,
and one of the bonus features of scraping your website, is that you get to some extent see how
search engines sees your website. Hence, it is also a somewhat valuable tool to SEO quality assure your
site. Magic's crawler explicitly identifies as a crawler, and obeys by all the standard crawler rules from
your robots.txt file.

## Training snippets

Magic supports fine tuning your own machine learning model, but we recommend using RAG to 99% of our clients.
RAG is much less expensive, and most of the time also much more accurate. RAG works by using OpenAI's embeddings
API to create embeddings for your training snippets, for then to create embeddings for questions asked
towards your model/type.

This allows us to use _"AI search"_ to find training snippets relevant to the question asked, for then to
pass this as _"context data"_ to OpenAI to answer questions.

It could be argued that we don't ask OpenAI to answer questions, since we already know the answer - Instead we're
using OpenAI to reassemble the answer into a sentence that makes sense according to what questions the model
is being asked. This has huge benefits, such as for instance almost completely eliminating AI hallucinations,
and allowing ChatGPT to answer questions it's got no idea about how to answer.

## History tab

Once you've created a machine learning model in Magic, you can turn on supervised. This implies that
Magic will store each question and answers it's given. This data can serve as reinforcement
learning material later, and can also work as an L2 cache, where once your model is asked
a question it has been asked before, it no longer needs to query OpenAI's API for the completion,
but can return the previous answer if it's got a good completion for the specified prompt.

The _"supervised"_ feature also allows you to _"monitor"_ your machine learning model, to verify
it is functioning optimally, allowing you to correct it where it fails and provide the correct answer,
for then to later upload this to OpenAI's API as _"reinforcement fine tuning material"_, or use
it as RAG by creating new training snippets based upon existing questions/answers.
You can easily turn on and off both machine learning caching, and machine learning
supervision, by editing the configuration for your model.

## A Machine Learning platform

Magic's machine learning component is actually horizontally implemented into almost
every single component in Magic. Need to use AI from [SQL Studio](/dashboard/sql-studio/),
no problem, it's an integrated feature. The same is true for [Hyper IDE](/dashboard/hyper-ide/),
and even help is implemented using OpenAI and ChatGPT. If you need help with some [Hyperlambda](/hyperlambda/)
code, just mark it in Hyper IDE and click F1, which will use AI to explain what the code does.

![Have AI explain Hyperlambda code](/images/hyperlambda-ai-help.jpeg)

However, in order to use machine learning with Magic, you will need
an [OpenAI API key](https://beta.openai.com/account/api-keys). This will cost
you some money, but OpenAI gives you a balance of 18 dollars initially.

## Create your own ChatGPT bot

You can create your own ChatGPT based chat bot with Magic. To get the JavaScript
needed to include your bot on your own website, only takes a couple of seconds, and can
be done as you are configuring your machine learning model.

As long as you have a website where you can somehow add a JavaScript file, Magic will
do the rest, associate your bot with your model, also your custom model, and render a
chat window wrapping your own AI model for asking questions.

You can see an example of such a chatbot in the bottom/right corner of this page.

The YouTube playlist below will walk you through every single thing you need to know to get your chatbot working. It's divided into sections, allowing you to easily jump to relevant videos, answering whatever questions you've got related to your problem.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL_iESc2yi8IUCwO1TDft2oAfrUvJHuzU9" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
