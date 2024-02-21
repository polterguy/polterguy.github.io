---
title: Dashboard
description: The Magic Dashboard allows you to manage your Magic Cloud backend by providing a GUI interface towards the backend.
header:
  image: /assets/images/finding-components.webp
  image_description: Wizard standing in his laboratory trying to find out what Magic spell he should use
---

The Magic Dashboard is how you would manage your cloudlet. When you login to your cloudlet, you will be greeted by PKI charts, displaying important information about your cloudlet. It typically resembles the following.

![The Magic Dashboard](/images/dashboard.jpeg)

In addition to the elements shown in the above screenshot, you will have a _"splash screen"_ you can dismiss, containing some hyperlinks, and also a YouTube playlist that helps you configure and create an AI chatbot. Below is the entire video series if you prefer watching it here.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL_iESc2yi8IUCwO1TDft2oAfrUvJHuzU9" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Components

Below is the documentation for each individual dashboard component.

* [SQL Studio](/dashboard/sql-studio/)
* [Hyper IDE](/dashboard/hyper-ide/)
* [Endpoint Generator](/dashboard/endpoint-generator/)
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

## Profile component

In addition to the above, there's also the profile component, allowing you to change what theme to use, change your password, and change some other settings.

## Generate token

The most important additional component is probably the _"Generate Token"_ component, that allows you to ceate long lasting JWT tokens, you can use when interacting with your cloudlet from other systems. Below is a screenshot.

![Generate JWT token component](/images/generate-token.jpeg)

This allows you to create a token you can use to authorize HTTP requests towards your cloudlet, if you need other systems to have extended rights towards your cloudlet. Tokens should be passed into your cloudlet as Bearer tokens in the Authorization HTTP header.
