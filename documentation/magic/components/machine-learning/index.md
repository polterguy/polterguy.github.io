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
that you can later use to train your own OpenAI model. OpenAI refers to such training sessions as _"fine tuning"_.

The way the crawler works, is by first checking if your website has a sitemap file. If your site has a sitemap,
it will retrieve all pages referenced in your sitemap file(s). Once it has retrieved an HTML document, it
will chop the HTML into multiple _"training snippets"_, where each Hx element becomes a prompt, and all
paragraphs below your Hx element becomes its completion. It will also preserve bulleted lists and
numbered lists, and unless it's traversing a sitemap, it will also extract all hyperlinks in your page,
and follow hyperlinks it finds to retrieve additional documents for its scraping process.

This process resembles the process Google and other search engines are doing as they crawl your site,
and one of the bonus features of scraping your website, is that you get to some extent see how
search engines sees your website. Hence, it is also a somewhat valuable tool to SEO quality assure your
site. Aista Magic Cloud's crawler explicitly identifies as a crawler, and if you see
_"Aista-MachineLearning-Spider"_ in your webserver's log, you know you've been crawled for
machine learning data by some Magic cloudlet.

## "Smart" machine learning crawling

In addition to _"chopping up"_ each page into Hx and paragraphs, it will also preserve the entire
page and associate all paragraphs with a completion that is associated with your page's H1 tag as
its prompt. It also contains several other _"intelligent"_ parts, resulting in as much learning
material as it can extract from your website, to further strenghten the quality of the final
machine learning model. One example of how Magic is using intelligent crawling is how it will
attempt to take each page it finds using this process, submit to OpenAI using the _"text-davinci-003"_
model to create a summary of your page, which it then saves as more additional training data.

The point about machine learning and AI, is that often the same information must be specified
multiple times to the model before it understands it, and is able to create its associations.
Preferably with smaller modifications, saying the same thing multiple times, with slightly
different words for each iteration. Aista Magic Cloud makes this part as easy as it can,
by creating as much machine learning training material as possible from your original website.

## How much machine learning training data do you need?

How much training data you need to create an effective AI model depends upon what you want
to accomplish. For a chat bot for a website, you typically need thousands of snippets
with training data. The quality of your AI model will never be better than your training data.

Another thing which is important to think about, is what quality your training data has.
The higher quality your website is, and the better structure it has, the better the
end resulting model will become. It's impossible to create an AI model that's better
than whatever data you train it on.

## Machine learning questions/answers log

Once you've created a machine learning model in Magic, you can turn on logging. This implies that
Magic will store each question and answers it's given, and this can be turned on by checking
the _"supervised"_ property as you configure your model. This data can serve as reinforcement
learning material later, and can also work as an L2 cache, where once your model is asked
a question it has been asked before, it no longer needs to query OpenAI's API for the completion,
but can return the previous answer if it's got a good completion for the specified prompt.

The _"supervised"_ feature also allows you to _"monitor"_ your machine learning model, to verify
it is functioning optimally, allowing you to correct it where it fails and provide the correct answer,
for then to later upload this to OpenAI's API as _"reinforcement fine tuning material"_.
You can easily turn on and off both machine learning caching, and machine learning
supervision, by editing the configuration for your model.

## Disclaimer about machine learning an AI

It is important that you supervise your model. This is especially true in the beginning.
Initially as you start out using machine learning and AI, your model will inevitably
produce a lot of bad results, that will seem like random guess work. To accommodate for this,
you should always sanity check your AI model by asking it a lot of different questions,
and see how it responds. When it gives you the wrong answer, you can gointo the requests
parts of Magic's machine learning component, and simply edit its response. As you've acquired
some few hundreds of such _"corrections"_, you can upload these to OpenAI to reinforce
your model, making it stronger and better.

We suggest you still keep on _"supervised mode"_ at least in the beginning as you start
using your AI model and expose it to your users. This allows you to continue gathering
training data as you get to see your model in the real world.

## Magic is scattered with machine learning and AI

Magic's machine learning component is actually horizontally implemented into almost
every single component in Magic. Need to use AI from SQL Studio, no problem, it's
an integrated feature. The same is true for Hyper IDE, and even the help section.
However, in order to use machine learning with Magic, you will need
an [OpenAI API key](https://beta.openai.com/account/api-keys). This will also cost
you some money, but OpenAI gives you a balance of 18 dollars initially. 18 dollars
is typically enough for a training session with some 500 to 1,000 training snippets,
in addition to playing around with your model after you've trained your model.
