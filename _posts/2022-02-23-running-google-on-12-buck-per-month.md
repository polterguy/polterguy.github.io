---
layout: post
author: thomas
title: Running "Google" on $12 per month
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/supercomputer.jpeg"
description: I just now performed a simple throughput and scalability test of Magic and Hyperlambda, and in this article I go through some of the stuff for show.
---

At my last _"day job"_ we spent roughly €20,000 per month on servers. In the job I had before that, we spent
€8,000 simply on CosmosDB. I don't even dare to imagine how much we spent in total, but I suspect it was in
the millions per month!
There used to be a time when _"machines were cheap and developers were expensive"_. The rationale was
of course that it wasn't cost effective for developers to write good code, since adding more hardware to
the problem solved it. That time is distant history today. To illustrate that point realise that at my
last employer we were 12 developers, and we spent €20,000 per month on servers. Those 20,000 EUROs
would equal to roughly 5 full time senior software developers in Cyprus where I live. This implies that
my former employer spent 30% of his total IT budget on _"cloud infrastructure"_.

> 30% of your IT budget on iron is NOT cheap!

Ignoring whether or not the above is justifiable or not, these servers are using energy, and energy
is a finite resource, and reducing our energy footprint is important as a specie for reasons that should
be obvious to most having either read any science the last 50 years, and/or paid an electricity bill
this last winter. In the video below I am illustrating how a $12 per month droplet from a VPS provider
when combined with Magic can arguably serve 250 simultaneous users, without using even 3% of its CPU.
To create a sustainable future, such figures are not only financially viable, but also probably
environmentally _crucial_. Extrapolating these 3% and 250 users results in that a $12 per month droplet
from a VPS provider can in theory serve 8250 simultaneous users. The sad part is that the company I started out
with at the beginning of this article was serving roughly 250 users _per day_. Magic + a $12 droplet
can serve 8,250 users _per second_. The first company paid $20,000 per month and could serve 250 users
per day. That becomes 2.8 million times more cost effective IT infrastructure in regards to hardware
costs than the mantra of _"developers are expensive and hardware is cheap"_ that resulted in my employer
throwing €20,000 out the window every month. Facts are, the Ethereum network alone is using more electricity
than the _country of Serbia_. You need to _"rethink your thinking"_ my friend.

In case you missed the point, let me emphasise it for you; The difference between your existing legacy
system and Magic is that your existing legacy system will crash down and burst into flames if you
give it 100 simultaneous users. Magic will yawn from boredom if you give it 1 million users on the
same hardware! Simply because of ...

> Magic was NOT built under the assumption of that "hardware is cheap!"

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/RxhTF6TzWJo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
