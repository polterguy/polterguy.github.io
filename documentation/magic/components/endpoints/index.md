
# Endpoints component

The endpoints component allows you to see all your HTTP endpoints, and also invoke these, similarly
to how Swagger or Open Web API would allow you to do through Swashbuckle. From your endpoints menu item
you can search for, parametrise, and invoke your endpoints, allowing you to simulate a client,
and play with your endpoints to understand how they work. You can also create assumptions about your
endpoints. An assumption is a high level integration test, sanity checking your system, ensuring your
system is working the way it is supposed to work. To create an assumption, invoke any endpoint, for
then to create an assumption.

Notice, endpoints have a type declaration providing some sort of semantic type of information about
your endpoint, and typically if this type declaration is _"internal"_, the endpoint is _not_
intended for being consumed by your own code, but only for Magic to use internally itself.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
