---
layout: post
author: thomas
---

Yesterday we published a [new release of Magic](https://github.com/polterguy/magic/releases).
I normally don't write articles when we create a new release, but I'll make an exception 
this time, simply because this release was kick ass cool, and I've got a point further down
in the article. Most releases just silently improves some part of Magic and Hyperlambda,
you pull its docker images, and some things automagically becomes better, without you noticing
much. However, this release is different. First of all it features non-breaking fundamental
changes to the programming language itself. For instance there's now an **[neq]** slot,
allowing Hyperlambda developers to compare for non-equality without adding the **[not]** slot.
Below is an example.

```
.val:foo
if
   neq
      get-value:x:@.val
      .:bar
   .lambda
      // Condition is true
```

However, even more importantly, is the fact that all comparison slots and conditional slots
can now take their LHS argument as an expression. Previously to achieve the above you'd have
to write something such as follows.

```
.val:foo
if
   not
      eq
         get-value:x:@.val
         .:bar
   .lambda
      // Condition is true
```

With this release you can significantly reduce the number of lines of code for the above
to become the following.

```
.val:foo
if
   neq:x:@.val
      .:bar
   .lambda
      // Condition is true
```

The above two Hyperlambda snippets does the exact same thing, except the last one is 6
lines of code, and the first one is 8 lines of code. Since neutral research in the subject
concludes with that the resource requirements to maintain a piece of code increases proportionally
with the number of lines of code, obviously this is a big thing.
In addition the conditional slots such as **[if]**, **[else-if]**, and **[while]** can now
optionally take their condition as an expression, such as illustrated below.

```
.foo:bool:true
if:x:@.foo
   // Condition is true
```

To achieve the above in a previous version of Magic and Hyperlambda you'd have to write something
such as follows.

```
.foo:bool:true
if
   get-value:x:@.foo
   .lambda
      // Condition is true
```

Yet again cutting the number of lines of code almost in half. Notice how the slot
no longer needs a **[.lambda]** argument. This is true because the slot is using an
expression as its sole argument, which implies there is no longer a need to explicitly
mark your lambda object as such, and the invocation treats the entirety of the **[if]**
slot's arguments as its lambda object.

## Documentation upgrade

In addition to the above programming language improvements, we've also gone through
every single part of Hyperlambda's documentation, and I've literally spoken it out
loudly to myself, every single word in every single article and tutorial, _multiple times_.
The reason for this is because all good text pieces have rhythm and musical qualities, and by
speaking it out loudly to yourself, this rhythm and musical quality more easily shows.
In addition every single video associated with the documentation has been re-created,
with much higher quality, and way more consistency. We've also scrapped a lot of videos
in this process by simply hiding them because they weren't of the quality we want others
to associate with our product.

## Momentum

When I started Magic's current codebase, I had already researched and developed its
ideas for almost 10 years. However, it was still a _"hobby project"_ for more than 2 years.
Last June I found myself without a job, and I started working full time on Magic,
implying 80 hours per week instead of 20. Since then what was started as a _"hobby project"_
has turned into a sustainable company, we've got VC funding, and we're hiring our 4th
employee probably on Monday.

If you compare its codebase back in June 2021 with its features today, you'll probably
notice the thing is at least one order of magnitude better, higher quality, and more easily 
consumed than it was 7 months ago. Something you can also deduct from the fact of that our
NuGet repository currently has some roughly 15,000 daily downloads as I am writing this.
Hence, people have obviously noticed the same thing I'm about to tell you now.

> Magic is "growing up"

## Memory lane

When I wrote the first article about Hyperlambda for MSDN Magazine back in 2017,
Microsoft had to put a disclaimer at the top. The disclaimer basically said the following.

> We believe this guy is bat shit crazy, but we're not sure, so we'll give him a chance

For the record, I don't blaim Michael Desmond for adding the _"probably bat shit crazy disclaimer"_.
Creating a new programming language arguably inspired by YAML, XML, XSLT, and XPath must seem like
madness to most. I'm sure MSDN's Editor in Chief was slightly surprised later though, as he saw the
article entering the _top 20 most read articles published by MSDN Magazine throughout their existence_ over
the next month. FYI, the [next article I wrote](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/june/csharp-make-csharp-more-dynamic-with-hyperlambda)
made it into top 5 ... ;)

Thank you for that chance Michael. Walking out on a limb is scary, but sometimes it's also
very rewarding. I owe you one here.

Anyways, I'm digressing - I guess it's the new year feeling still hanging around, since
we're still in the beginning of the year. However, since June 2021 we've published no less
than _50 releases of Magic and Hyperlambda_, and this article summed up _some_ of _one_
of these releases most important features - And my point with writing this article is
that if you tried out Magic and Hyperlambda 7 months ago, please realise it's almost
a completely different thing today, because most of these releases had an equally
impressive changelog as this release. A former friend of mine used to say the
following about me.

> Is Thomas crazy? Totally, but he's not crazy enough! We're working on it though!

I doubt I'll ever be _that_ crazy ever again, but there are lessons to be learned from
the above story - Which is as follows ...

> Don't dismiss crazy people, crazy is a pre-requisite for brilliance

It's a new year now, and we're writing 2022. Over the last couple of years we've all
been arguably bat shit crazy. Do me a favour though please, don't ignore the crazy guy, or
the crazy girl, they just might be brilliance in the making. Hug your crazy friend this year.
_You_ might need him or her in the future ... ;)

Peace out, _"the crazy guy"_ ...

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/cWGE9Gi0bB0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

