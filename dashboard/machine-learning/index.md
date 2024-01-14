---
title: Machine Learning
description: Magic allows you to automatically generate your own private AI based Machine Learning model based upon OpenAI and ChatGPT
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/machine-learning.jpg"
---

Magic's Machine Learning component allows you to create your own AI based machine learning model, either by
crawling your website and scraping it for data, or by manually uploading your own training data, resulting in a private
and custom _"machine learning model"_. Machine learning in Magic is built upon OpenAI's
API and is similar to ChatGPT.

Magic contains a lot of additional services, such as the ability to monitor or supervise
usage, storing questions and answers into your database, and use these as the foundation for reinforced learning to
improve your model's accuracy over time. You can also use historical requests for business intelligence, or lead generation.

You can crawl and scrape your website for training data, or upload your own training data in a wide variety of formats,
such as XML, JSON, YAML, CSV, or PDF.

You can use either RAG/VSS or fine-tuning. We recommend using RAG for 99% of use cases since it eliminates AI hallucinations,
resulting in higher accuracy, and is also significantly less expensive.

## Use cases

* Expert law system, answering legal questions for your clients
* Medical expert advice system based upon AI and machine learning, giving you help when diagnosing patients and clients
* Support chatbot for your enterprise, giving your client support for whatever questions they might have
* Automated sales expert systems, converting leads on your website into paying clients
* Cognitive assistants, helping your employees with some specific task at hand

The advantage of creating your own Machine Learning model is that you can create a private and custom artificial
intelligence. This can become a much _"sharper"_ intelligence than the publicly available ChatGPT, with
knowledge about your particular problem domain, problems ChatGPT is not able to correctly provide answers to.

To understand what I mean here go to [ChatGPT](https://chat.openai.com) and ask it about your
company. Chances are that ChatGPT have no idea how to answer your questions correctly. If you scrape your
company's website, and/or upload your own training data, you could create a _"custom version of ChatGPT"_ that
is able to answer support requests, and/or convince leads and potential clients to become
paying customers, etc. This is of course _impossible_ with the general ChatGPT implementation, but
can sometimes be created in some few minutes using Magic Cloud.

This is one of the primary services [AINIRO.IO](https://ainiro.io) is providing, and we have a lot of experience with building high quality AI chatbots. If you want us to create you a chatbot, you can create a demo chatbot on our website, or [contact us here](https://ainiro.io/contact-us).

## Crawling your website

To crawl and scrape your website, create a type, then click the _"Import"_ button on your type and provide it with your website's URL.

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

![Scraping your website from machine learning](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/machine-learning.jpg)

## Types

A _"type"_ is a collection of training snippets. When a chatbot is asked a question, it will use VSS search to find training data that is relevant to your question from one specific _"type"_. Then it will transmit this training data as _"context"_ to OpenAI, and have OpenAI answer questions using the _"context"_ as its source of information.

You can create many types in Magic, and therefor many chatbots solving different problems.

![List of machine learning types](/assets/images/machine-learning-types.jpeg)

Once you're done with importing training snippets into your type, you'll have to click _"Vectorize"_ on your type before the data can be used by your chatbot.

### Configuring your type

A single machine learning type has dozens of configuration settings, for everything you can imagine. Its most important settings can be found in its _"Type"_ tab.

![Configuring your machine learning type](/assets/images/configuring-your-machine-learning-type.jpeg)

The most important parts from above is the _"System message"_. This becomes the equivalent of a ChatGPT _"instruction"_, telling the type how to behave. Below is an example system instruction to give you an example.

> You are Frank, a sales executive for Acme, Inc. Follow these rules when replying to my questions:
> 
> * You must answer all my questions exclusively based upon the information found in the context
> * You may suggest relevant products and services you find in the context
> * You should respond with short answers unless asked to elaborate
> * You must respond with Markdown
> * You should return relevant images and hyperlinks formatted as Markdown
> * You may use emojis if it makes sense
> * If you cannot find the answer to the question in the context, then inform the user that you are only configured to answer questions about Acme, Inc. and that the user should provide some keywords for you to find relevant information

## Training snippets

Magic supports fine tuning your own machine learning model, but we recommend using RAG to 99% of our clients.
RAG is much less expensive, and most of the time also much more accurate. RAG works by using OpenAI's embeddings
API to create embeddings for your training snippets, for then to create embeddings for questions asked
towards your type.

This allows us to use _"AI search"_ to find training snippets relevant to the question asked, for then to
pass this as _"context data"_ to OpenAI to answer questions.

It could be argued that we don't ask OpenAI to answer questions, since we already know the answer - Instead we're
using OpenAI to reassemble the answer into a sentence that makes sense according to what questions the model
is being asked. This has huge benefits, such as for instance almost completely eliminating AI hallucinations,
and allowing ChatGPT to answer questions it's got no idea about how to answer.

One training snippet is one such atomic piece of information. Typically as we transmit _"context"_ to OpenAI, we will transmit multiple training snippets, and choose the most relevant training snippets as we create this context. This allows Magic to _"freely associate"_, and choose training data from multiple different sources as it's creating your context.

A single answer might use data from two different PDF documents, 5 XML documents, and 3 web pages

### Managing your training snippets

Training snippets can be automatically created as we scrape your website, upload documents, or even manually created. When we setup a chatbot a lot of the work is actually related to _"washing your training data"_ to further increase the quality of the chatbot.

![Editing one training snippet](/assets/images/editing-one-training-snippet.jpeg)

If you turn on caching on a single training snippet, the snippet will be _"hard cached"_, which implies that if it scores at the top for some query, it will be returned _"as is"_, without being transmitted to OpenAI. This can be beneficial for things you want to return exactly as is, without transforming before displaying to the end user.

In general you should be very careful with caching too many snippets, since it might result in inferior quality.

### Adding Hyperlambda code to training snippets

A single training snippet can also contain Hyperlambda. If this training snippets scores as the first for some query, only this training snippet will be used, and the Hyperlambda code will be executed before the snippet is sent to OpenAI to answer the user's question. Below is an example of such a training snippet.

**How many questions have you answered lately?**

```
The last 14 days I have answered { {

data.connect:[generic|magic]
   data.scalar:select count(*) from ml_requests
   return:x:-


} } questions from happy users.
```

Notice, the `{` and `}` characters have spaces between them. Remove these in your own Hyperlambda snippets to ensure the Hyperlambda is executed.

If the user asks the questions; _"How many questions have you answered"_, the type will match the above training snippet, and the Hyperlambda will be executed. After executing the Hyperlambda, the context will end up resembling the following.

> The last 14 days I have answered 123 questions from happy users.

This will then be transmitted to OpenAI as context data, allowing it to use this to answer your question. This allows your chatbot to work with real time data, and connect itself to any additional data source, to dynamically create context data it sends to OpenAI.

## History tab

Once you've created a machine learning model in Magic, you can turn on supervised. This implies that
Magic will store each question and answers it's given. This data can serve as reinforcement
learning material later, and can also work as an L1 cache, where once your model is asked
a question it has been asked before, it no longer needs to query OpenAI's API for the completion,
but can return its previous answer.

The _"supervised"_ feature also allows you to _"monitor"_ your machine learning model, to verify
it is functioning optimally, allowing you to correct it where it fails and provide the correct answer -
For then to later upload this to OpenAI's API as _"reinforcement fine tuning material"_, or use
it as RAG by creating new training snippets based upon existing questions/answers.

You can easily turn on and off both machine learning caching, and machine learning
supervision, by editing the configuration for your snippet or model.

Notice, caching on the type only works for non-GPT types, implying types where you're using for instance `text-davinci-003` as your completion model. If you turn on caching on your type, it will return cached answers given the same question.

![Turning on caching in the history tab](/assets/images/caching-on-history-requests.jpeg)

To turn on caching in the history tab, you need to first turn on caching for your type, and then turn on
caching for individual previous requests you want to cache.

Caching on the training snippet however, works for all types, and will use the matching training snippet only
if the cached training snippet scores as the top matching snippet for a question. This makes the training snippet
cache capable of returning answers from the cache also when the question is _not_ an exact match of a previous
question. This makes training snippet caching _"broader"_, which might result in it returning an incorrect answer.

As a general rule of thumb _you should be very careful with caching_. At AINIRO.IO we barely ever use it ourselves
when we're configuring types for our clients.

## Questionnaires

A chatbot can also ask its users initial questions before the user is allowed to access the chatbot. This can
be useful for gathering information such as the user's name and email address, and is a part of our lead generation
features.

To create a questionnaire, you will typically first create a questionnaire, for then to add questions such as the following.

```
* Before we start I will need your name to ensure you get a high quality personalized experience => type=message
* What is your name? => context=1
* What is your email?
* Thank you, you can now ask me anything related to the company in the context => type=message
* If you want to contact us you can just leave your name and email in the chatbot, with a short message 😊 => type=message
```

![Creating a new questionnaire](/assets/images/creating-questionnaire.jpeg)

The first message above becomes a message, and the chatbot will _not_ wait for the user to answer before it shows question
number 2. This is due to the _"type"_ parts at the end being _"message"_. The second question will have its answer
transferred to OpenAI, allowing your chatbot to know the name of your users, and use this in its conversations. This
is due to the _"context"_ having a value of _"1"_.

If you ommit the context, or set its value to _"0"_, this data will never be sent to OpenAI, allowing you to gather
the email address of your users, without compromising your user's privacy in any ways.

Only when the user has finished the above questionnaire, he or she will gain access to the chatbot, allowing them to
use machine learning to answer their questions. To create a new questionnaire, click the _"Questionnaire"_ tab, for then to click the _"Add"_ button. Give your questionnaire a name, choose a type, and optionally provide it with an action.

![Creating a new questionnaire](/assets/images/new-questionnaire.jpeg)

When you're done with the above, you can provide your questionnaire with questions. _"single-shot"_ implies each individual user will only be asked these questions _once_. _"sendgrid-subscribe"_ implies an action the chatbot will invoke once the user has finished the questionnaire. You can create your own Hyperlambda slots that will be invoked after a questionnaire is done as follow.

```
slots.create:magic.questionnaires.action.MY-ACTION

   // Sanity checking invocation.
   validators.mandatory:x:@.arguments/*/name
   validators.mandatory:x:@.arguments/*/email
   validators.email:x:@.arguments/*/email
```

For then to provide _"MY-ACTION"_ as the action to perform after the questionnaire is finished.

Notice, to get structured data inside your slot you will have to apply a _"name"_ attribute for each question you
want to semantically handle inside your slot, such as follows.

```
* What is your name? => name=name
* What is your email? => name=email
```

The above questionnaire will invoke your slot with a **[name]** and **[email]** argument once it's done.

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

### Magic's integrated support chatbot

In addition Magic integrates a support chatbot directly into its dashboard. This provides you with
integrated help directly from the dashboard. Click the chat button in the top right corner in your
dashboard to access this chatbot.

![Magic's integrated support chatbot](/assets/images/integrated-chatbot.jpeg)

### Magic's integrated help system

Another crucial component related to machine learning in Magic is its integrated help system. If you're
in Hyper IDE and you don't understand some snippet of Hyperlambda, you can mark this Hyperlambda, and click
F1. This will use machine learning to explain the selected Hyperlambda for you.

![AI help system](/assets/images/ai-help-system.jpeg)

## Create your own AI chatbot

You can create your own ChatGPT based chatbot with Magic. To get the JavaScript
needed to include your bot on your own website, only takes a couple of seconds, and can
be done as you are configuring your machine learning model.

As long as you have a website where you can somehow add a JavaScript file, Magic will
do the rest, associate your bot with your model, also your custom model, and render a
chat window wrapping your own AI model for asking questions.

You can see an example of such a chatbot in the bottom/right corner of this page.

However, the easiest way to create your own chatbot is probably to start out with the [Chatbot Wizard](/dashboard/chatbot-wizard/).

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL_iESc2yi8IUCwO1TDft2oAfrUvJHuzU9" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
