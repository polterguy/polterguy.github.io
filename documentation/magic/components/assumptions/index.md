---
title: Automatically generated integration/unit tests
description: Magic allows you to automatically generate unit tests, or integration tests. The assumptions component allows you to automatically run all such tests to sanity check your system's health.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-assumptions.jpg"
---

# The health check component

The health check component allows you to easily sanity check your system, providing you with a
diagnostic tool, ensuring that your system is functioning as it should. A health check test is basically
an integration test, with one or more _"assumptions"_ about your system, which if not is true
implies your system is not functioning as it should. An example of such a test can be for instance
as follows; _"If you try to login without a password the system should not authenticate you"_. Such assumptions
allows you to ensure your system is functioning, by providing you with _"automated unit testing"_, that
are executed all at once as you modify your system's code. You can create your own health check tests from
the _"Endpoints"_ menu item as you invoke your endpoints.

![Assumptions](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/assumptions.jpg)

The health check component allows you to run all your tests automatically by clicking the _"Run"_ button
in the top/right corner. This will sequentially execute all assumptions in the system, and if one of
your assumptions fails for some reasons, it will show you which assumption failed, easily allowing
you to determine which part of your system is not functioning as it should. This results in a similar
security mechanism as unit tests provides you with, except assumptions are technically
integration tests and not really unit tests.

## Create tests automatically

Magic allows you to create health check tests automatically, eliminating the need to manually write
test code. To create your own health check test open up your _"Endpoints"_ menu item, find an endpoint, invoke it
somehow, and create a new test after having invoked your endpoint.

![Creating a new unit test](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/new-assumption.jpg)

If you check the _"Match response"_ checkbox the response returned from the server needs to be the
exact same in the future for the test to pass. Depending upon your endpoint's semantics this might or might not be the correct
test logic. Obviously, for tests reading data from database tables that could somehow change their content
over time, you should _not_ match the response. If you don't click the checkbox, it will only verify the status
code your server returns. You can also create assumptions for error status codes, such as for
instance; _"If I invoke a non-existing endpoint a 404 status code should be returned from the server"_.
As you create a test, Magic _"records"_ your HTTP invocation, persist its response, and allows you to
automatically _"replay"_ your invocation later, assuming its HTTP response is similar as you replay your test.

## Manually create health check tests

You can also manually create health check tests that contains Hyperlambda you need to execute to verify that your
system is functioning correctly. This is done by creating a Hyperlambda file, store this file in your
_"/etc/tests/"_ folder, and put content into it resembling the following.

```
description:Verifies that 2+2 equals 4.
.lambda
   .no1:int:2
   .no2:int:2
   if
      not
         eq
            math.add:x:@.no1
               get-value:x:@.no2
            .:int:4
      .lambda
         throw:Math error!
```

The idea is to have your test throw an exception if something is wrong. This allows you
to create _"unit tests"_ where you somehow verify that your system is functioning correct, by for instance
invoking dynamically created slots, with assumptions about their return values, etc.
