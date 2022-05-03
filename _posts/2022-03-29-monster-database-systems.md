---
layout: post
author: thomas
title: Monster Database Systems
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/mysql-monster.jpg"
description: A micro tutorial about how to create a registration form using Magic
---

For the record, I would not recommend anyone to stuff 2 billion records into a MySQL database, but it _is_ possible, and [Magic](https://aista.com) handles it just fine. Of course, simply counting 2 billion records takes minutes, and in order to be able to even use it in a Hyperlambda generated CRUD backend you'd have to apply some super aggressive server-side caching constructs, but it _is_ possible as you can clearly see from the following screenshot.

![Monster MySQL database](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/mysql-monster.jpg)

Before tonight I had never even heard of such large MySQL databases I must confess, but Gary Gray, our South African partner is actually handling such monster databases. You can find his company [here](https://dialtonetech.com/). Gary having decades of experience, ranging from VoIP to running his own Linux distro, doesn't seem to be easily scared though.
I guess his mindset was as follows; _"I've got a MySQL database with 2 billion records, I need CRUD operations on it, let's use Magic"_. Well, if it works in MySQL Workbench, it should work in Magic, so I think Gary's arguments were pretty perfect here.

## Monster CRUD systems

The largest database I have ever personally used Magic on was a database with 650+ tables, each table with an average of 25 columns, with some few millions records in. Considering each Hyperlambda endpoint typically ends up at 50 lines of code, each table typically gets 5 files, multipled by 650, we're now up to 162,500 lines of code. Magic of course produced these in a handful of minutes. When I generated a frontend for it, I had to bump my Angular and NodeJS build system's memory, but after some time I figured out these parts too, and Magic produced 1.8 million lines of Angular code for me, and I was able to actually run the thing doing CRUD towards the database without much hassle. All in all the process took me an hour if I remember correctly.

According to neutral studies in the subject the average software developer can produce between 325 and 750 lines of code per month. An average of 550. Dividing 1,965,000 lines of code on 550 implies Magic produced the equivalent of 3,572 months worth of work for me. Further dividing that number by 12 becomes 298 years. Purely mathematically, imagining having a team of 100 software developers, ignoring all other aspects of the problem, we're then looking at 100 developers working for 2.9 years to reproduce something equivalent.

Now of course such figures aren't completely _"fair"_ some would argue, since the code is simple in form, there is no business logic in it, and such simple code can be produced much faster than the _"industry average"_. However, even dividing the numbers by 100 implies having one software developer working for 2.9 years to reproduce what Magic did in minutes.

However, if such numbers are _"fair"_ or not, and if I am exaggerating or not, is really quite irrelevant. The point is that at such numbers, having 2 billion database records, in 650+ tables, with 25+ columns each, there exists _no sane way to manually create software to maintain such amount of data_. Even imagining being able to hire a thousand people for free, working 1,000 times faster than the industry average, to manually create the required code in hours is still not interesting, for one simple reason ...

> Humans creates errors, software systems do not

And when you're dealing with 3,250 HTTP endpoints, some of which returns 2 billion records, and some 15,000 files of Angular code, humans are simply not even remotely interesting as _"problem solvers"_ anymore due to that we get bored, overlooks errors, creates typos and bugs - And the computer does not. It's easy to imagine Magic as a _"cute tool for smaller systems"_, but in many ways this is wrong, and it's arguably a _better_ fit for _"monster systems"_, simply because of one simple reason ...

> Magic doesn't become bored!