---
title: Chatbot Wizard
description: Magic allows you to create an AI chatbot that you can embed on your website. Point Magic to your website, automatically scrape your site, and you're done.
header:
  image: /assets/images/hero/chatbot-wizard.png
  og_image: /assets/images/hero/chatbot-wizard-og.png
  image_description: The Chatbot Wizard
faq:
  - q: "What is the Chatbot Wizard?"
    a: "The fastest way to create an AI website chatbot. Provide your website URL, and the wizard crawls the site, turns what it finds into training data, and gives you an embeddable chatbot a few minutes later."
  - q: "What do I need before creating a chatbot?"
    a: "An OpenAI API key. Optionally you can configure Google reCAPTCHA, although Magic ships with its own PoW-based Magic CAPTCHA, which is good enough for most."
  - q: "What is a persona?"
    a: "A template for the chatbot's system instruction. Personas with DYNAMIC in their name generate the instruction from your website's landing page, typically producing a much higher quality chatbot."
  - q: "Can I control which pages are scraped?"
    a: "Yes. If you provide a sub-URL such as foo.com/blogs, only pages beneath /blogs are scraped, giving you control over which parts of your site become training data."
  - q: "How do I embed the chatbot on my website?"
    a: "Once created, use the Machine Learning component's Embed button, which gives you a script tag you can paste into your website, with themes and colours you can customise."
  - q: "Can I refine the chatbot afterwards?"
    a: "Yes. The chatbot is a machine learning model, so you manage it with the Machine Learning component - editing training data, changing its model or instruction, adding widgets and AI functions, and monitoring its usage."
---

The Chatbot Wizard component allows you to rapidly create an AI website chatbot powered by OpenAI that you can embed on your website. It's not as powerful as the [Machine Learning](/dashboard/machine-learning/) component, but much easier to use. You can start out with the Chatbot Wizard, for then to later configure your model with the Machine Learning component.

![Screenshot of scraping your website for custom AI chatbot RAG data](/images/custom-chatgpt-chatbot.jpg)

You'll need an OpenAI API account, and provide Magic with your API key. You can optionally configure reCAPTCHA if you want to, but Magic contains Magic CAPTCHA out of the box, which should be good enough for most. Once you've done this, you can provide your website URL, click a button, and some few minutes later you've got an AI chatbot you can include on your website. Once you're done with this process, you can further configure your model using the Machine Learning component, manually adding training snippets, edit training snippets, etc.

## Create your own AI chatbot

The process of creating an AI chatbot is fairly straight forward. The following guides you through everything you need to know to get started.

### 1. Configuring Magic with your OpenAI API key

To create your own AI chatbot you first have to supply Magic with your OpenAI API key.

![Screenshot of configuring Magic with your OpenAI API key](/assets/images/chatbot-wizard-configure-openai.jpeg)

If you don't have an OpenAI API key you can click [here](https://platform.openai.com/api-keys) to go to OpenAI's platform and create one. Notice, you have to _make at least one payment to OpenAI before you're given access to their latest models_.

Your API key should resemble the following;

```
sk-xyGHa45xyzQWEghjKLMNOaBCdQHHllsdf345SFGfdg
```

The above is obviously _not_ a valid API key, but simply provided to illustrate roughly what it looks like.

### 2. Configuring Magic with reCAPTCHA keys - OPTIONAL

To avoid having your chatbot overrun by bots, you should use some sort of CAPTCHA library. Magic contains its own PoW-based CAPTCHA library, but you might want to use Google reCAPTCHA as an alternative here. You can create a Google reCAPTCHA key pair for free by clicking [here](https://www.google.com/recaptcha). Copy and paste both the site-key and the secret into the dialog asking you for your reCAPTCHA settings.

![Screenshot of providing Magic with your reCAPTCHA keys](/assets/images/chatbot-wizard-configure-recaptcha.jpeg)

Since Magic contains its own internal PoW-based CAPTCHA library, this step is optional, and you can just ignore it unless you want extra tight security for your chatbot.

### 3. Scraping your website

Before you click _"Create chatbot"_, you can choose a base model from OpenAI, a _"persona"_, how many pages you want to scrape, and whether the chatbot should be automatically deleted after 7 days. The persona is a template for a system message or OpenAI instruction. If you choose a persona with the word _"DYNAMIC"_ in its name, the system message will be dynamically created according to the landing page of the website you are crawling, and typically produce a much higher quality chatbot for you. We recommend using _"Frank - DYNAMIC"_ here.

Finally you can scrape your website. Provide the chatbot wizard with your website's URL, and click the _"Create chatbot"_ button.

![Screenshot of scraping your website to create an AI chatbot using the Chatbot Wizard](/assets/images/chatbot-wizard-scrape-website.jpeg)

If you provide a sub-URL such as for instance `foo.com/blogs`, the scraper will only scrape pages beneath `/blogs`. This allows you to scrape an explicitly defined sub-portion of your website, and such have some control over which pages are being scraped.

The wizard reports its progress as it crawls your site and turns the pages into training data, and a few minutes later your chatbot is ready. From here you manage and embed your chatbot using the [Machine Learning component](/dashboard/machine-learning/), where you can further edit its training data and copy the HTML snippet required to embed it on your website.

If you want to see what the different chatbot themes look like, you can try all different themes [here](https://ainiro.io/blog/try-our-chatbot-themes).

When you're done with the above you probably want to use the [Machine Learning component](/dashboard/machine-learning/) to further configure and manage your chatbot.

{% include faq.html %}
