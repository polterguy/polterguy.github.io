---
title: Machine Learning component
description: Magic allows you to automatically generate your own private AI based Machine Learning model based upon OpenAI and ChatGPT
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/machine-learning.jpg"
---

# The Machine Learning component

Aista Magic Cloud's machine learning component allows you to create your own AI based machine learning model, either by
crawling your website scraping it for data, or by manually uploading your own training data, resulting in a private
and custom machine learning model, solving your particular need. Machine learning in Magic is built upon OpenAI's
ChatGPT, and contains a lot of additional services, such as the ability to monitor or supervise usage, storing
questions and answers into your database, and use these as the foundation for reinforcement learning to improve
its accuracy.

![Magic's Machine Learning parts](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/machine-learning.jpg)

You can crawl your website for training data, or upload your own training data in a wide variety of formats,
such as XML, JSON, YAML and CSV.

## Use cases for Magic's Machine Learning parts

Use cases might be for instance.

* Expert law system, answering legal questions for your clients
* Medical expert advice system based upon AI and machine learning, giving you help when diagnosing patients and clients
* Support chat bot for your enterprise, giving your client support for whatever questions they might have
* Automated sales expert systems, converting leads on your website into paying clients
* Cognitive assistants, helping your employees with some specific task at hand

The advantage with creating your own Machine Learning model, is that you can create a private and custom artificial
intelligence. This can become a much _"sharper"_ intelligence than the publicly available ChatGPT AI, with
knowledge about your particular problem domain, that the generally available ChatGPT implementation is not
able to provide answers to. To understand what I mean here go to [ChatGPT](https://chat.openai.com) and ask it about your
company. Chances are that ChatGPT have no idea how to answer your questions correctly. If you scrape your
company's website, and/or upload your own training data, you could create a custom version of ChatGPT that
is able to answer support requests, and/or convince leads and potential clients to become
paying customers, etc. This is of course _impossible_ with the general ChatGPT implementation, but
can sometimes be created in some few minutes using Aista Magic Cloud.

## Internals of Magic's Machine Learning crawler

You can upload training data in a wide variety of formats. However, most interestingly for most is that
you can simply point Magic at your website, and it will crawl your website, and scrape it for training data
that you can later upload to OpenAI to fine-tune your own AI model.

The way it works, is by first checking if your website has a sitemap file. If your site has a sitemap,
it will retrieve all pages referenced in your sitemap file(s). Once it retrieves an HTML document, it
will chop it up into multiple _"training snippets"_, where each Hx element becomes a prompt, and all
paragraphs below your Hx element becomes the completion. It will also preserve bulleted lists and
numbered lists, and unless it's traversing a sitemap, it will also extract all hyperlinks in your page,
and follow these, to retrieve additional documents for its scraping process.

This process resembles the process Google and other search engines are doing as they crawl your site,
and one of the bonus features of scraping your website, is that you get to some extent see how
search engines sees your website. Hence, it is also a somewhat valuable tool to SEO QA test your
site. Aista Magic Cloud's crawler even explicitly identifies as a crawler, and if you see
_"Aista-MachineLearning-Spider"_ in your webserver's log, you know you've been crawled for
machine learning data by some Magic cloudlet.

In addition to _"chopping up"_ each page into Hx and paragraphs, it will also preserve the entire
page and associate all paragraphs with a completion that is associated with your page's H1 tag as
its prompt. It also contains several other intelligent bits, resulting in as much learning
material as it can extract from your website, to further strenghten the quality of the final
machine learning model. The point about machine learning and AI, is that often the same
information must be specified multiple times to the model before it understands it, and
is able to create its associations. Aista Magic Cloud makes this part as easy as it can,
by creating as much machine learning training material as possible from your original website.

## Machine learning questions/answers log

Once you've created a machine learning model in Magic, you can turn on logging. This implies that
Magic will store each question and answers it's given, and this can be turned on by checking off
the _"supervised"_ property as you configure your model. This data can serve as reinforcement
learning material later, and can also work as an L2 cache, where once your model is asked
a question it has been asked before, it no longer needs to query OpenAI's API for the completion,
but can return the previous answer if it's got a good completion for the specified prompt.

This feature also allows you to _"monitor"_ your machine learning model, to verify it is
functioning optimally, and where it fails, you can correct it, provide the correct answer,
for then to later upload this to OpenAI's API as _"reinforcement learning material"_.
You can easily turn on and off both machine learning caching, and machine learning
supervision, by editing the configuration for your model.
