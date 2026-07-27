---
title: Dashboard
description: The Magic Dashboard allows you to manage your Magic Cloud backend by providing a graphical user interface towards your backend cloudlet.
header:
  image: /assets/images/finding-components.webp
  image_description: Wizard standing in his laboratory trying to find out what Magic spell he should use
---

The Magic Dashboard is how you would manage your cloudlet. When you login to your cloudlet, you will be greeted by the dashboard's landing page, showing key numbers about your cloudlet - its Magic version, and how many endpoints, users, scheduled tasks, and log items it has. This typically resembles the following.

![Screenshot of the Magic Dashboard](/images/dashboard.jpeg)

Below the key numbers, the landing page gives you quick access to the things you'll reach for most often. If your cloudlet has the MCP module installed, it shows the MCP URL you hand to an AI agent so it can discover and invoke your endpoints as tools. The _Chatbot Wizard_ crawls a website, turns what it finds into training data, and gives you an embeddable AI chatbot in a few minutes. A _"What everything does"_ section explains every part of your cloudlet and where to find it, and a _Tasks_ section lets you execute your scheduled tasks on demand. If you prefer to learn by video, the series below walks you through configuring your cloudlet, mostly focusing on creating AI chatbots.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-width: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL_iESc2yi8IUCwO1TDft2oAfrUvJHuzU9" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Components

Below is the documentation for each individual dashboard component.

* [SQL Studio](/dashboard/sql-studio/)
* [Hyper IDE](/dashboard/hyper-ide/)
* [Endpoint Generator](/dashboard/endpoint-generator/)
* [Hyperlambda Generator](/dashboard/hyperlambda-generator/)
* [Endpoints](/dashboard/endpoints/)
* [Users & Roles](/dashboard/users-roles/)
* [Task Manager](/dashboard/task-manager/)
* [Plugins](/dashboard/plugins/)
* [Machine Learning](/dashboard/machine-learning/)
* [Log](/dashboard/log/)
* [Hyperlambda Playground](/dashboard/hyperlambda-playground/)
* [Databases](/dashboard/databases/)
* [Configuration](/dashboard/configuration/)
* [Chatbot Wizard](/dashboard/chatbot-wizard/)

In addition to the above, there's also the profile component, allowing you to change what theme to use, change your password, and change some other settings related to your profile.

## Generate token

The most important additional component is probably the _"Generate Token"_ component, that allows you to create long lasting JWT tokens, you can use when interacting with your cloudlet from other systems. Below is a screenshot.

![Generate JWT token component](/images/generate-token.jpeg)

This allows you to create a token you can use to authorize HTTP requests towards your cloudlet, if you need other systems to have extended rights towards your cloudlet. Tokens should be passed into your cloudlet as Bearer tokens in the Authorization HTTP header.
