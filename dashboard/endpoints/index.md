---
title: Endpoints
description: Browsing your HTTP endpoints is easy in Magic with the integrated 'Swagger component' that comes with Magic out of the box. This component also allows you to invoke your endpoints, with any payload/arguments you wish, to see the result of your invocation immediately.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg"
---

The Endpoints component allows you to see your HTTP endpoints, and invoke these, similarly
to how Swagger works. From your endpoints menu item you can search for, parametrise, and invoke
your endpoints - Allowing you to simulate a client, to understand how
they work. This component hence serves two purposes; One being documenting your endpoints,
another being testing your endpoints.

![Endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg)

## Hyperlambda endpoint meta data

Hyperlambda endpoints have a type declaration providing some sort of semantic type of information about
your endpoint, and typically if this type declaration is _"internal"_, the endpoint is _not_
intended for being consumed by your own code, but only for internal usage by Magic.
This meta data is displayed in the endpoint component, and allows you to more easily classify
your endpoints, understanding what an endpoint does.

Magic will automatically determine what type your query parameter is, and show the correct form
control in its endpoint component for whatever type is required as input to your endpoint. This implies
it will show checbox elements for boolean arguments, date time pickers for date and time arguments, etc.
This component also support providing JSON payloads to POST and PUT endpoints, using syntax highlighting
through CodeMirror.

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

The endpoint's meta information is retrieved directly from your Hyperlambda files. Magic automatically allows you
to invoke your user defined endpoints with this component.

The endpoints component in Magic is obviouisly not as strong as something such as OpenAPI, Swagger, or Postman - But for Hyperlambda endpoints, it's probably more than enough.
