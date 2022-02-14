---
layout: post
author: thomas
title: Automatically generate your Unit Tests
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/new-assumption.jpg"
description: With Magic you can automatically generate your Unit Tests by simply clicking a button. This article demonstrates the concept and shows you how to achieve the same with your own HTTP endpoints.
---

Unit Tests is one of those things everybody's talking about, but few have time to actually create. Every time I've been
in a job interview, I've been asked if I am willing to create Unit Tests, and given the impression that if I answered
no I'd not be chosen - Still, every time I've started the job I've been told the following ...

> Unit Tests, we don't have time to write non-productive code

Some companies of course are different, but the majority of companies I've worked for as an enterprise software developer
have told me to not _"waste time"_ on writing unit tests. This approach of course is pure madness, but it's still the reality.
Realising the serious implications of this we created the ability to have Magic automatically create unit tests for you,
by simply clicking a button. In the viewo below I am demonstrating how this works.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/YWW1HcxGetY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

As you're invoking your HTTP endpoints, Magic will actually remember your payload, arguments, the response, status code, etc -
And once you click the _"New assumption"_ button allow you to persist the invocation, for then to later being able to _"replay"_
the invocation. This allows you to create a suite of HTTP endpoint invocations, you can collective replay later in some
few seconds, to sanity check your system, and verify it's healthy and behaving as expected. Below is a screenshot illustrating
a persisted HTTP invocation.

![Automatically generate unit tests](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/assumptions.jpg)

To create such asumptions, all you need to do is to invoke your HTTP endpoint, and click the _"New assumption"_ button
as illustrated below, at which point you can provide a description for your assumption, in addition to a name which
Magic will refer to it as later.

![Creating assumptions](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/new-assumption.jpg)

If you click the _"Match response"_ checkbox, Magic will assume future invocations returns an _exact match_ of the
original HTTP response object. If you leave it off, it will only verify the status code. For endpoints returning
dynamic data, you should for obvious reasons _not_ click the checkbox. However, more important is the fact that Magic
also allows you to replay _error_ invocations, implying invocations that should return some sort of error object to the
caller. Examples could for instance be trying to login without a username or password - Which should obviously result
in some sort of error response. Magic also allows you to manually create assumptions by creating Hyperlambda code
by hand, that becomes a part of your unit test suite, for cases where your logic is too complex for the automated
unit test generator to automatically do the work. You can [read more about assumptions here](/documentation/magic/components/assumptions/) where you can see examples of the latter.
