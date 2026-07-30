---
title: Dashboard
description: The Magic Dashboard allows you to manage your Magic Cloud backend by providing a graphical user interface towards your backend cloudlet.
header:
  image: /assets/images/hero/dashboard.png
  og_image: /assets/images/hero/dashboard-og.png
  image_description: The Magic dashboard
---

The Magic Dashboard is how you would manage your cloudlet. When you login to your cloudlet, you will be greeted by the dashboard's landing page, showing key numbers about your cloudlet - its Magic version, and how many endpoints, users, scheduled tasks, and log items it has.

## Your cloudlet is an AI agent (MCP)

Every Magic cloudlet can act as an AI agent through its built-in [MCP server](/tutorials/how-to-connect-the-mcp-server/). Connect an orchestrator AI - such as Claude, Claude Code, Cursor, or Codex - to your cloudlet, and it can discover and invoke your endpoints as tools, query your databases, generate new Hyperlambda, and even build new tools for itself on demand. As soon as the MCP module is installed, the dashboard's landing page shows your MCP URL together with a _"Copy MCP URL"_ button. This is the preferred way to work with Magic - you orchestrate, and the AI builds and runs your backend for you.

## The landing page

When you log in, the dashboard typically resembles the following.

![Screenshot of the Magic Dashboard](/images/dashboard.jpeg)

Below the key numbers, the landing page gives you quick access to the things you'll reach for most often. The _Chatbot Wizard_ crawls a website, turns what it finds into training data, and gives you an embeddable AI chatbot in a few minutes. A _"What everything does"_ section explains every part of your cloudlet and where to find it, and a _Tasks_ section lets you execute your scheduled tasks on demand.

## Create an AI chatbot

The fastest way to experience Magic's AI capabilities is to create a chatbot straight from the dashboard's landing page. Provide a website URL to the Chatbot Wizard, choose a model and a persona, and click _"Create chatbot"_. The wizard crawls the site, scrapes each page it finds, and turns the content into training data (RAG data) for your chatbot - reporting its progress in real time as it works its way through the site.

![Screenshot of the dashboard crawling and scraping a website to create an AI chatbot](/assets/images/scraping-website-for-chatbot-data.png)

A few minutes later your chatbot is ready, and you can embed it on your website, or use it as the foundation for an AI agent. From here you manage its training data and configuration using the [Machine Learning component](/dashboard/machine-learning/). Read more about the entire process in the [Chatbot Wizard documentation](/dashboard/chatbot-wizard/).

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

In addition to the above, there's also the profile component, allowing you to change your password, and change some other settings related to your profile.

## Generate token

The most important additional component is probably the _"Generate Token"_ component, that allows you to create long lasting JWT tokens, you can use when interacting with your cloudlet from other systems. Below is a screenshot.

![Generate JWT token component](/images/generate-token.jpeg)

This allows you to create a token you can use to authorize HTTP requests towards your cloudlet, if you need other systems to have extended rights towards your cloudlet. Tokens should be passed into your cloudlet as Bearer tokens in the Authorization HTTP header.
