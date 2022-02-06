---
title: Hyperlambda assumptions to sanity check your system
description: An assumption is basically an automatically generated integration test, similar to a unit test, in that it allows you to sanity check your system automatically, by having your system diagnose itself.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-assumptions.jpg"
---

# Assumptions component

The assumptions component allows you to easily sanity check your system, providing you with a
diagnostic tool, ensuring that your system is functioning as it should. An assumption is basically
an integration test, with one or more _"assumptions"_ about your system, which if not is true
implies your system is not functioning as it should. An example of an assumption can be for instance
as follows; _"If you try to login without a password the system should not authenticate you"_. Magic
is delivered out of the box with a whole range of integrated assumptions, but you can also create your own
assumptions from the _"Endpoints"_ menu item. Below is a screenshot of the assumptions component.

![Assumptions](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/assumptions.jpg)

The assumptions component allows you to run all your assumptions automatically by clicking the _"play"_ button
in the top/right corner. This will sequentially execute all assumptions in the system, and if one of
your assumptions fails for some reasons, it will show you which assumption failed, easily allowing
you to determine which part of your system is not functioning as it should. This results in a similar
security mechanism as unit tests provides you with, except assumptions are technically
integration tests and not really unit tests, and such tests your system from a much higher level.

To create your own assumption open up your _"Endpoints"_ menu item, find an endpoint, invoke it
somehow, and create a new assumption after having invoked your endpoint. Below is a screenshot of this
process.

![Creating an assumption](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/new-assumption.jpg)

If you click the above _"Match response"_ checkbox the response returned from the server needs to be the
exact same in the future, which depending upon your endpoint's semantics might or might not be a correct
assumption. If you don't click the checkbox, it will only verify the status code your server returns.
You can also create assumptions for error status codes, such as for
instance; _"If I invoke a non-existing endpoint a 404 status code should be returned from the server"_.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
