
# Endpoints component

The endpoints component allows you to see all your HTTP endpoints, and also invoke these, similarly
to how Swagger works. From your endpoints menu item you can search for, parametrise, and invoke
your endpoints, allowing you to simulate a client, and play with your endpoints to understand how
they work. Below is a screenshot of how the endpoints component typically looks like.

![Endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg)

Notice, endpoints have a type declaration providing some sort of semantic type of information about
your endpoint, and typically if this type declaration is _"internal"_, the endpoint is _not_
intended for being consumed by your own code, but only for Magic to use internally itself.
If you invoke one of your endpoints you can also create an _"assumption"_ about your invocation,
which becomes the equivalent of an integration tests that's possible to _"replay"_ later,
sanity checking some parts of your system, to verify your system is functioning properly.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
