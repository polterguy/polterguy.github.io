---
layout: post
author: thomas
title: Have a registration form
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/reg-form.jpg"
description: For weird reasons registration forms seems to have been the curse of my life. You wouldn't think it's all that difficult though; Supply your email address, repeat some password, have the user confirms his email - Really, how difficult can it be?
---

I once worked for a non-disclosed company where we spent two years trying to create a freakin' registration form. We didn't succeed. For the record, I was not project lead in any ways what so ever here. The process is quite simple though.

* Have the user supply an email address
* Have the user repeat some password twice
* Send an email to the user
* Have the user confirm his email address

The above isn't exactly rocket science, right? Still, I've worked with companies capable of turning the above simple process into dozens of HTTP endpoints, require hundreds of seconds to execute, and some companies not even able to pull it through at all. Well, I've got news for you ... ;)

![Registration form](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/reg-form.jpg)

We just released [a new version of Aista Magic Cloud](https://github.com/polterguy/magic/releases/tag/v12.0.0), and the above is one of its features. More importantly though, since the Magic dashboard is a multi backend system, you can couple the dashboard with a backend API URL by choosing some backend you're connected to, copy its URL, and send it to friends, colleagues, and family members to have them automatically register in your backend of choice. The process implies _two_ HTTP invocations to your backend; One for registering, and another to verify your email - And both of these invocations executes in 0.2 seconds in total, assuming you've got it on a VPS that's somewhere within the vicinity of the outer layers of the galaxy known as the Milky Way of course ...

Another detail this release also gives you, is that if you choose to subscribe to our newsletter, you get a promo code. This promo code gives you 100% rebate on _every single micro service module we've got in our Bazar_. Yup, you heard us right, we're giving you every single micro service for free in return for subscribing to our newsletter. That's micro services equalling €1,204 for free for you, _for a limited time though_ may I add. This also allows you to test the double optin parts of our registration form, which is almost the exact same process as the registration form in Magic itself. So update your existing Docker images if you already have Magic installed using Docker, and/or download the latest source of Magic and get started.

* [Get started now](https://docs.aista.com/tutorials/getting-started/)
