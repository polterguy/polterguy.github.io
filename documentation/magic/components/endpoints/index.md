---
title: Browsing your HTTP endpoints
description: Browsing your HTTP endpoints is easy in Magic with the integrated 'Swagger component' that comes with Magic out of the box. This component also allows you to invoke your endpoints, with any payload/arguments you wish, to see the result of your invocation immediately.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-endpoints.jpg"
---

# Browsing your HTTP endpoints

The endpoints component allows you to see all your HTTP endpoints, and also invoke these, similarly
to how Swagger works. From your endpoints menu item you can search for, parametrise, and invoke
your endpoints, allowing you to simulate a client, and play with your endpoints to understand how
they work. Below is a screenshot of how the endpoints component typically looks like.

![Endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg)

Notice, endpoints have a type declaration providing some sort of semantic type of information about
your endpoint, and typically if this type declaration is _"internal"_, the endpoint is _not_
intended for being consumed by your own code, but only for internal usage by Magic.
If you invoke one of your endpoints you can also create an [assumption](/documentation/magic/components/assumptions/)
about your invocation, which becomes the equivalent of an integration tests that's possible to _"replay"_
later, sanity checking some parts of your system, to verify your system is functioning properly.
Below is a screenshot of parametrising an endpoint invocation by adding arguments to it as
you invoke it.

![Parametrising your endpoint invocation](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoint-parameter.jpg)

Magic will automatically determine what type your query parameter is, and show the correct form
control for whatever type is required as input to your endpoint. This implies it will show checbox
elements for boolean arguments, date time pickers for date and time arguments, etc. This component also
support providing JSON payloads to POST and PUT endpoints, using syntax highlighting through CodeMirror.
Below is a screenshot.

![Parametrising your endpoint invocation](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoint-post.jpg)

## Assumptions

When you have invoked an endpoint, Magic allows you to persist your invocation, its response, and automatically
_"replay"_ your invocation later, resulting in an _"assumption"_.
[Assumptions](/documentation/magic/components/assumptions/) are high level automated tests, that allows you to
sanity check your system, providing similar mechanisms to what unit testing provides you with, only at
a much higher abstraction level, since an assumption implies invoking an HTTP endpoint and verifying
its response. Below is a screenshot of the process of creating an assumption after you have invoked your
endpoint.

![Creating an assumption](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/new-assumption.jpg)

## Meta data

As you are browsing your endpoints, and expand individual items, you'll notice that each endpoint shows you a
whole range of _"meta data"_. This gives you high level information about your endpoints, such as for instance.

* Relative URL
* HTTP verb
* Type of endpoint
* What endpoint consumes (JSON, Hyperlambda, form-data, etc)
* What type of result the endpoint produces
* Friendly description for your endpoint
* Authorisation requirements for invoking the endpoint, implying roles users must belong to in order to invoke the endpoint
* Etc, etc, etc

This information is retrieved directly from your Hyperlambda files, and is just one of those things
you get _"for free"_ out of your Magic box. Magic automatically allows you to invoke your user defined endpoints
with this component, also directly from [Hyper IDE](/documentation/magic/components/hyper-ide/). Below is a screenshot
of the latter. Notice, click the _"Invoke"_ button from Hyper IDE to immediately test your endpoint as you create it.

![Hyper IDE Endpoint invocation](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-endpoints.jpg)

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
