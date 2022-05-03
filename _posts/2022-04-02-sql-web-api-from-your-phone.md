---
layout: post
author: thomas
title: Create an SQL web API from your phone
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/phone-sql-api.jpeg"
description: With a web based IDE that is responsive there exists no limits to what you can do, really
---

The following screenshot was literally taken from my iPhone, and yes I am not only writing SQL on my phone, but I am also creating an HTTP API in the same process.

![SQL web API from your phone](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/phone-sql-api.jpeg)

When you go _"all in"_ on compatibility and cross platform some interesting axioms and use cases emerges as a natural consequence. A couple of weeks ago I showed the above feature in [our CRUD generator](https://aista.com) to some colleagues attending a networking event where I live, and one of them even laughed out loud and said.

> I don't think I have ever seen somebody writing SQL on their phone

It might be easy to dismiss the above feature as _"overkill"_ or _"marketing"_, but that's probably because your brain isn't geared to understanding its usefulness. For instance, imagine you're a DB administrator, and you're on vacation, and you need to create a report for your manager extracting SQL for some frontend guy creating a chart of some kind. In the _"old world"_ this would imply having to go back to your hotel room, finding your laptop that you for this sole purpose had to drag with you to the other side of the world, boot it, and sit by your bedside for an hour messing with your SQL. All in all we're probably talking about 2/3 hours of destroyed _"vacation time"_. If you had Magic on your server though, you could probably use your phone from beneath the dinner table, create the HTTP endpoint in some few minutes, without anybody even noticing you were actually working. To illustrate the use case slightly better, let me show you how the above looks like on a computer, and realise you've got access to every single feature in Magic on your phone that you can access from your computer.

![SQL web API from your phone](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/count-actors-blog.jpg)

* Adding arguments to your endpoint? Check!
* Joins and any amount of complexity in your SQL? Check!
* Authorisation and authentication to prevent unauthorised user to access your endpoint? Check!
* Configuring the exact URL you need? Check!
* Scalar values and record sets? Check!
* Having the ability to do all of the above from your phone? Check!

If you want to try it out feel free to [download Magic](https://aista.com). The entire code base is 100% open source, and you can use it as you see fit. It even comes with docker containers for easy deployments to a VPS of your choosing.
