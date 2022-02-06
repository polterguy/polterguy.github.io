
# SQL crudifier component

This component allows you to automatically generate an HTTP web API endpoint wrapping some arbitrary SQL statement.
It is similar to the backend CRUD generator, but instead of automatically creating your SQL, it allows you
to provide your own custom SQL, and then securely wrap your SQL into an HTTP web API backend endpoint.
Below is a screenshot of the component.

![SQL web API](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

The process works as follows.

1. Choose your database
2. Choose an HTTP verb and a URL for your endpoint
3. Select which roles should be allowed to invoke your endpoint (optional)
4. Provide arguments to your endpoint (optional)
5. Write your SQL referencing arguments if you provided arguments in the above step

When you've done with the above, simply click the _"Generate"_ button, and you've got an HTTP endpoint
wrapping your SQL. Read [this article](/tutorials/sql-web-api/) to understand this process.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
