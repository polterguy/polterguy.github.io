---
title: Chatbot Wizard
description: Magic allows you to create an AI chatbot that you can embed into your website in some few minutes. Point Magic to your website, automatically scrape your site, and you're done.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/custom-chatgpt-chatbot.jpg"
---

The Chatbot Wizard component allows you to rapidly create an AI website chatbot powered by OpenAI that you can embed on
your website. It's not as powerful as the [Machine Learning](/dashboard/machine-learning/) component, but much easier to use.
You can start out with the Chatbot Wizard, for then to later configure your model with the Machine Learning component.

![Scraping your website for custom AI chatbot data](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/custom-chatgpt-chatbot.jpg)

You'll need an OpenAI API account, and provide Magic with your API key. In addition you'll need a reCAPTCHA account,
and provide your site-key and secret to Magic. Once you've done this, you can provide your website URL,
click a button, and some few minutes later you've got an AI chatbot you can include on your website.
Once you're done with this process, you can further configure your model using the Machine Learning component,
manually adding training snippets, edit training snippets, etc.

In the bottom/right corner of this page you can try our chatbot to understand roughly what you'll end up with.

## Create your own AI chatbot

The process of creating an AI chatbot is fairly straight forward. The following guides you through everything you need to know to get started.

### 1. Configuring Magic with your OpenAI API key

To create your own AI chatbot you first have to supply Magic with your OpenAI API key.

![Providing Magic with your OpenAI API key](/assets/images/chatbot-wizard-configure-openai.jpeg)

If you don't have an OpenAI API key you can click [here](https://platform.openai.com/api-keys) to go to OpenAI's platform and create one. Notice, you have to _make at least one payment to OpenAI before you're given access to GPT4_.

Your API key should resemble the following;

```
sk-xyGHa45xyzQWEghjKLMNOaBCdQHHllsdf345SFGfdg
```

Notice, the above is _not_ a valid API key, but just provided to illustrate how it looks like.

### 2. Configuring magic with reCAPTCHA keys

To avoid having your chatbot overrun by bots, you want to use Google reCAPTCHA. You can create a Google reCAPTCHA key pair for free by clicking [here](https://www.google.com/recaptcha). Copy and paste bot the site-key and the secret into the dialog asking you for your reCAPTCHA settings.

![Providing Magic with your reCAPTCHA keys](/assets/images/chatbot-wizard-configure-recaptcha.jpeg)

Before you click start, you can choose a flavor, how many pages you want to scrape, what base model from OpenAI to use, if you want to automatically recrawl the website once every 24 hours, and if you want to automatically vectorize the website once you're done scraping it.

### 3. Scraping your website

Finally you can scrape your website. Provide the chatbot wizard with your website's URL, and click the _"Start"_ button.

![Scraping your website to create an AI chatbot](/assets/images/chatbot-wizard-scrape-website.jpeg)

When the process is done, it will resemble the following.

![Chatbot Wizard is done with scraping a website](/assets/images/chatbot-wizard-after-scraping.jpeg)

At this point you can already embed your chatbot on your website. Choose your theme, title, button text, etc - And click the _"Copy"_ button. This will put the HTML required to embed your chatbot on your own website on your clipboard. The last settings implies.

* References - If the chatbot should provide citations from your website
* Chat - Must be true to enable chatting
* Markdown - If the chatbot should transform the result from Markdown to HTML
* Speech - If true, the chatbot will support speech recognition and speech synthesis
* RTL - For Arabic, Hebrew, Farsi and other right to left language
* Submit button - If the chatbot should have a submit button
* Stream - If the chatbot should stream its results back to the client

For a complete walkthrough of the entire process, including things not discussed in this article, you can watch the [following YouTube playlist](https://www.youtube.com/watch?v=VdF8F6tvgqQ&list=PL_iESc2yi8IUCwO1TDft2oAfrUvJHuzU9).

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL_iESc2yi8IUCwO1TDft2oAfrUvJHuzU9" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

When you're done with the above you probably want to use the [Machine Learning component](/dashboard/machine-learning/) to further configure and manage your chatbot.
