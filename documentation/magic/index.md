---
title: Magic middleware documentation
description: The Magic middleware is the parts wiring up Magic, allowing you to use Magic in your own projects, providing you with a default backend for your own frontend apps, authentication, authorisation, and CRUD endpoints wrapping your database(s).
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/Aista-Magic-Cloud.jpeg"
---

# Magic's Dashboard

The Magic Dashboard is your primary tool when you're using Aista Magic Cloud, and it contains a graphical
user interface for managing your Magic installation, allowing you to solve all sort of different tasks
related to your cloudlet. Using the navbar at the top of your dashboard allows you to manage all aspects
of your Magic Cloudlet, such as your scheduled tasks, machine learning models, Hyperlambda code, etc.

![Your Magic dashboard](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/Aista-Magic-Cloud.jpeg)

In addition the dashboard contains some key performance indicators and charts, showing you how often
others are authenticating to your cloudlet, your last 10 log items, etc. The first time you open your dashboard,
you will see a YouTube that guides you through how to get started with Magic and Hyperlambda. We recommend
that you watch this video to understand how to use Magic.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/pJHuUiItrnc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Aista Magic Cloud contains the following parts

* [Endpoint generator component](/documentation/magic/components/crudifier/backend/)
* [Frontend generator component](/documentation/magic/components/crudifier/frontend/)
* [SQL endpoint generator component](/documentation/magic/components/crudifier/sql/)
* [The database component](/documentation/magic/components/databases/)
* [SQL Studio](/documentation/magic/components/sql/)
* [Machine Learning and AI](/documentation/magic/components/machine-learning/)
* [Hyper IDE](/documentation/magic/components/hyper-ide/)
* [Hyperlambda Playground](/documentation/magic/components/evaluator/)
* [Endpoints](/documentation/magic/components/endpoints/)
* [Plugins component](/documentation/magic/components/bazar/)
* [Tasks component](/documentation/magic/components/tasks/)
* [Users and roles component](/documentation/magic/components/auth/)
* [Cryptography component](/documentation/magic/components/crypto/)
* [Health check](/documentation/magic/components/assumptions/)
* [Sockets](/documentation/magic/components/sockets/)
* [Configuration component](/documentation/magic/components/config/)
* [Profile component](/documentation/magic/components/profile/)
* [Log](/documentation/magic/components/log/)
* [HTTP endpoints in Magic](/documentation/magic/endpoints/)
* [Dynamic Hyperlambda slots in Magic](/documentation/magic/slots/)
