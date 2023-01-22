---
title: Browsing your HTTP endpoints
description: Browsing your HTTP endpoints is easy in Magic with the integrated 'Swagger component' that comes with Magic out of the box. This component also allows you to invoke your endpoints, with any payload/arguments you wish, to see the result of your invocation immediately.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg"
---

# Endpoints

The endpoints component allows you to see all your HTTP endpoints, and also invoke these, similarly
to how Swagger works. From your endpoints menu item you can search for, parametrise, and invoke
your endpoints, allowing you to simulate a client, and play with your endpoints to understand how
they work. This component hence serves a lot of purposes, one being documenting your endpoints,
while another purpose being testing your endpoint.

![Endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg)

## Hyperlambda endpoint meta data

Notice, Hyperlambda endpoints have a type declaration providing some sort of semantic type of information about
your endpoint, and typically if this type declaration is _"internal"_, the endpoint is _not_
intended for being consumed by your own code, but only for internal usage by Magic.
This meta data is displayed in the endpoint component, and allows you to more easily classify
your endpoints, understanding what an endpoint does.

If you invoke one of your endpoints using the endpoint component, you can also create
a [health check test](/documentation/magic/components/assumptions/) for your invocation, which becomes
the equivalent of an integration tests that can be _"replayed"_ later, sanity checking some parts of your
system, to verify your system is functioning properly.

Magic will automatically determine what type your query parameter is, and show the correct form
control in its endpoint component for whatever type is required as input to your endpoint. This implies
it will show checbox elements for boolean arguments, date time pickers for date and time arguments, etc.
This component also support providing JSON payloads to POST and PUT endpoints, using syntax highlighting
through CodeMirror.

![Endpoint with JSON payload](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoint-post.jpg)

## Health check tests

When you have invoked an endpoint, Magic allows you to persist your invocation, its response, and automatically
_"replay"_ your invocation later, resulting in a _"health check test"_.
Such [health check tests](/documentation/magic/components/assumptions/) are automatic tests, allowing you to
sanity check your system later, providing similar mechanisms to what unit testing provides you with, only at
a much higher abstraction level, since a health check test implies invoking an HTTP endpoint and verifying
its response.

![Creating a health check test](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/new-assumption.jpg)

## Endpoint meta data features

As you are browsing your endpoints, and expand individual items, you'll notice that each endpoint shows you a
whole range of _"meta data"_. This gives you high level information about your endpoints, such as for instance.

* Relative URL
* HTTP verb
* Type of endpoint
* What type of data the endpoint consumes (JSON, Hyperlambda, form-data, etc)
* What type of result the endpoint produces
* Humanly readable description of your endpoint
* Authorisation requirements for invoking the endpoint, implying roles users must belong to in order to invoke the endpoint
* Etc, etc, etc

The endpoint's meta information is retrieved directly from your Hyperlambda files, and is just one of those things
you get _"for free"_ out of the box with Magic. Magic automatically allows you to invoke your user defined endpoints
with this component, also directly from [Hyper IDE](/documentation/magic/components/hyper-ide/).

![Hyper IDE Endpoint invocation](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-endpoints.jpg)
