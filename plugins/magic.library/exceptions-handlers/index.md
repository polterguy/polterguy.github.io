---
title: "Exceptions handlers"
description: "Exceptions handlers - Magic allows you to provide a custom exceptions handler on a per folder level."
generated: true
---

This page is part of the [magic.library](/plugins/magic.library/) documentation.

Magic allows you to provide a custom exceptions handler on a per folder level. This overrides the
default exception logic with a custom exception handler expected to be named _"exceptions.hl"_ and found within
the folder hierarchy where an HTTP invocation is resolved. For instance, if you wish to create your own exception
handler for a specific module called _"foo"_, you can create an exception handler file
called _"/files/modules/foo/exceptions.hl"_, and expect this file to be invoked every time an unhandled exception
occurs, anywhere inside of your _"foo"_ folder.
This allows you to transform an unhandled exception, such as for instance localising it or customising it
in any ways. Your custom exception handler will be invoked with the following arguments.

* __[message]__ - The exception error message
* __[path]__ - The URL that triggered the exception
* __[field]__ - If the exception that was thrown declared a field, this argument will contain the name of the field
* __[status]__ - If the exception that was thrown declared a status code, this argument will contain the status code
* __[public]__ - If the exception that was thrown wants to propagate to the client this will be true

You can return a _"transformed"_ exception from your exception handler, returning the following arguments, that will
end up becoming the response object returned to the client.

* __[message]__ - Message to return as JSON to client
* __[field]__ - Field to return as JSON to client
* __[status]__ - Status code to decorate your HTTP response with

The default exception handler can be found in _"/files/exceptions.hl"_, which will be invoked if no custom exception
handler is declared further down in your folder hierarchy.

---

[all of magic.library](/plugins/magic.library/)
