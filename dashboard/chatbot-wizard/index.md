---
title: Chatbot Wizard
description: Magic allows you to create an AI chatbot that you can embed on your website. Point Magic to your website, automatically scrape your site, and you're done.
og_image: "/images/custom-chatgpt-chatbot.jpg"
header:
  image: /assets/images/wizard-magically-pulling-ai-chatbots-our-of-cauldron.webp
---

The Chatbot Wizard component allows you to rapidly create an AI website chatbot powered by OpenAI that you can embed on your website. It's not as powerful as the [Machine Learning](/dashboard/machine-learning/) component, but much easier to use. You can start out with the Chatbot Wizard, for then to later configure your model with the Machine Learning component.

![Screenshot of scraping your website for custom AI chatbot RAG data](/images/custom-chatgpt-chatbot.jpg)

You'll need an OpenAI API account, and provide Magic with your API key. You can optionally configure reCAPTCHA if you want to, but Magic contains Magic CAPTCHA out of the box, which should be good enough for most. Once you've done this, you can provide your website URL, click a button, and some few minutes later you've got an AI chatbot you can include on your website. Once you're done with this process, you can further configure your model using the Machine Learning component, manually adding training snippets, edit training snippets, etc.

In the bottom/right corner of this page you can try our chatbot to understand roughly what you'll end up with.

## Create your own AI chatbot

The process of creating an AI chatbot is fairly straight forward. The following guides you through everything you need to know to get started.

### 1. Configuring Magic with your OpenAI API key

To create your own AI chatbot you first have to supply Magic with your OpenAI API key.

![Screenshot of configuring Magic with your OpenAI API key](/assets/images/chatbot-wizard-configure-openai.jpeg)

If you don't have an OpenAI API key you can click [here](https://platform.openai.com/api-keys) to go to OpenAI's platform and create one. Notice, you have to _make at least one payment to OpenAI before you're given access to GPT4_.

Your API key should resemble the following;

```
sk-xyGHa45xyzQWEghjKLMNOaBCdQHHllsdf345SFGfdg
```

The above is obviously _not_ a valid API key, but simply provided to illustrate roughly how it looks like.

### 2. Configuring Magic with reCAPTCHA keys - OPTIONAL

To avoid having your chatbot overrun by bots, you should use some sort of CAPTCHA library. Magic contains its own PoW-based CAPTCHA library, but you might want to use Google reCAPTCHA as an alternative here. You can create a Google reCAPTCHA key pair for free by clicking [here](https://www.google.com/recaptcha). Copy and paste bot the site-key and the secret into the dialog asking you for your reCAPTCHA settings.

![Screenshot of providing Magic with your reCAPTCHA keys](/assets/images/chatbot-wizard-configure-recaptcha.jpeg)

Since Magic contains its own internal PoW-based CAPTCHA library, this step is optional, and you can just ignore it unless you want extract tight security for your chatbot.

### 3. Scraping your website

Before you click start, you can choose a flavor, how many pages you want to scrape, what base model from OpenAI to use, if you want to automatically recrawl the website once every 24 hours, and if you want to automatically vectorize the website once you're done scraping it. You can also choose a _"flavor"_ which is a template for a system message or OpenAI instruction. If you choose a flavor with the word _"DYNAMIC"_ in its name, the system message will be dynamically created according to the landing page of the website you are crawling, and typically produce a mugh higher quality chatbot for you. We recommend using _"Frank - DYNAMIC"_ here.

Finally you can scrape your website. Provide the chatbot wizard with your website's URL, and click the _"Start"_ button.

![Screenshot of scraping your website to create an AI chatbot using the Chatbot Wizard](/assets/images/chatbot-wizard-scrape-website.jpeg)

If you provide a sub-URL such as for instance `foo.com/blogs`, the scraper will only scrape pages beneath `/blogs`. This allows you to scrape an explicitly defined sub-portion of your website, and such have some control over which pages are being scraped.

When the process is done, Magic will show you an embed dialog allowing you to copy the JavaScript inclusion script required to embed your chatbot on your site.

![Screenshot of the Chatbot Wizard being finished with scraping a website](/assets/images/chatbot-wizard-after-scraping-2.jpeg)

At this point you can already embed your chatbot on your website. Choose your theme, title, button text, etc - And click the _"Copy HTML"_ button. This will put the HTML required to embed your chatbot on your website onto your clipboard. The settings you can choose when embedding implies as follows.

* Follow up - Whether or not the chatbot should display follow questions. Notice, requires a special system instruction instructing OpenAI to generate follow up questions.
* References - If the chatbot should provide citations from your website
* RTL - For Arabic, Hebrew, Farsi and other right to left language
* Clear button - If the chatbot should have a _"start new session"_ button
* Copy button - If the chatbot should have a _"copy response to clipboard"_ button
* New tab - If the chatbot should open all hyperlinks in new tabs

If you want to see how the different themes looks like, you can try all different themese [here](https://ainiro.io/blog/try-our-chatbot-themes).

For a complete walkthrough of the entire process, including things not discussed in this article, you can watch the [following YouTube playlist](https://www.youtube.com/watch?v=VdF8F6tvgqQ&list=PL_iESc2yi8IUCwO1TDft2oAfrUvJHuzU9).

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-width: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL_iESc2yi8IUCwO1TDft2oAfrUvJHuzU9" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

When you're done with the above you probably want to use the [Machine Learning component](/dashboard/machine-learning/) to further configure and manage your chatbot.
