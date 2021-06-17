
# Documentation for Magic

This is the official documentation for Magic, and it contains both reference documentation,
and tutorial style type of documentation. If you've just recently started to use Magic, I
suggest you start out with the tutorials, starting out from the top, and move downwards.

## Tutorials

* [Getting started](/tutorials/getting-started/) - Getting Magic up running
* [Database CRUD operations](/tutorials/database-crud/) - Automate the process of creating code
* [SQL Web API](/tutorials/sql-web-api/) - Create HTTP endpoints in SQL
* [Using Magic with SQL Server](/tutorials/sql-server/) - Using Magic with Microsoft SQL Server
* [Magic beyond CRUD](/tutorials/cloud-ide/) - A guided tour through Magic's Dashboard
* [Web Sockets and SignalR in Magic](/tutorials/web-sockets/) - How to use Web Sockets with Magic
* [Authentication and authorisation](/tutorials/auth/) - How Magic solves authentication and authorisation
* [Scheduling tasks](/tutorials/task-scheduler/) - How to use Magic to create and schedule tasks
* [Cryptographically secured HTTP Lambda Invocations](/tutorials/crypto-lambda-http/) - Inversion of Code
* [Hyperlambda Hello World](/tutorials/hello-world-endpoint/) - Your first Hyperlambda endpoint
* [Expressions, slots, and nodes](/tutorials/expressions-slots-nodes/) - Hyperlambda is *really* weird!
* [Authentication internals](/tutorials/auth-internals/) - How to exchange the default authentication with for instance Windows authentication

## Use cases

These are Open Source example apps built with Magic, illustrating usage of Magic in some specific scenario.

* [AnarQ a Social Media use case](/tutorials/anarq-usecase/) - Creating a Social Media backend with Magic

## Reference documentation

* [magic.node](/documentation/magic.node/) - Explains nodes, Hyperlambda and Expressions
* [magic.lambda](/documentation/magic.lambda/) - Explains Hyperlambda as a DSL, and its keywords
* [magic.endpoint](/documentation/magic.endpoint/) - Endpoint resolving in Magic
* [magic.data.common](/documentation/magic.data.common/) - Commonalities for data adapters in Magic
* [magic.http](/documentation/magic.http/) - HTTP REST invocations in Magic from C#
* [magic.signals](/documentation/magic.signals/) - Magic's Super Signals implementation
* [magic.lambda.math](/documentation/magic.lambda.math/) - Math operations from Hyperlambda
* [magic.lambda.http](/documentation/magic.lambda.http/) - Invoking HTTP REST endpoints from Hyperlambda
* [magic.lambda.csv](/documentation/magic.lambda.csv/) - Manipulating CSV from Hyperlambda
* [magic.lambda.json](/documentation/magic.lambda.json/) - Manipulating JSON from Hyperlambda
* [magic.lambda.html](/documentation/magic.lambda.html/) - Manipulating HTML from Hyperlambda
* [magic.lambda.mail](/documentation/magic.lambda.mail/) - Sending and retrieving emails from Hyperlambda
* [magic.lambda.mime](/documentation/magic.lambda.mime/) - Parsing email messages in Hyperlambda
* [magic.lambda.auth](/documentation/magic.lambda.auth/) - Authentication and authorisation from Hyperlambda
* [magic.lambda.ad-auth](/documentation/magic.lambda.ad-auth/) - Authentication through Active Directory or Windows Authentication
* [magic.lambda.dates](/documentation/magic.lambda.dates/) - Allows you to manipulate DateTime objects from Hyperlambda
* [magic.lambda.slots](/documentation/magic.lambda.slots/) - Dynamically create your own slots/functions
* [magic.lambda.mysql](/documentation/magic.lambda.mysql/) - Accessing your MySQL server from Hyperlambda
* [magic.lambda.mssql](/documentation/magic.lambda.mssql/) - Accessing your MS SQL Server from Hyperlambda
* [magic.lambda.image](/documentation/magic.lambda.image/) - Image library, allowing you to generate QR code
* [magic.lambda.crypto](/documentation/magic.lambda.crypto/) - Cryptography helpers for Hyperlambda
* [magic.lambda.guid](/documentation/magic.lambda.guid/) - Creating a guid from Hyperlambda
* [magic.lambda.config](/documentation/magic.lambda.config/) - Accessing configuration values from Hyperlambda
* [magic.lambda.logging](/documentation/magic.lambda.logging/) - Logging from Hyperlambda
* [magic.lambda.caching](/documentation/magic.lambda.caching/) - Caching from Hyperlambda
* [magic.lambda.strings](/documentation/magic.lambda.strings/) - Manipulate strings in Hyperlambda
* [magic.lambda.scheduler](/documentation/magic.lambda.scheduler/) - Create scheduled tasks and workflows from Hyperlambda
* [magic.lambda.validators](/documentation/magic.lambda.validators/) - Validate input in Hyperlambda
* [magic.lambda.hyperlambda](/documentation/magic.lambda.hyperlambda/) - Parse Hyperlambda from text, and vice versa
* [magic.lambda.sockets](/documentation/magic.lambda.sockets/) - Web socket support for Magic using SignalR
* [magic.lambda.system](/documentation/magic.lambda.system/) - System support for Magic to spawn of terminals etc.
* [magic.io](/documentation/magic.io/) - IO operations in Magic
* [magic.library](/documentation/magic.library/) - A single NuGet package helper tying everything easily together

# Support

If you have a support request of private nature, or another type of request, you can send me
email at [thomas@servergardens.com](mailto:thomas@servergardens.com). If you want to submit a
feature request or a bug report, you can do such through the project's
[GitHub Issues](https://github.com/polterguy/magic/issues).

* [thomas@servergardens.com](mailto:thomas@servergardens.com)

# License

Magic is 100% Open Source and free of charge to use. The main backend is licensed as MIT, the dashboard is GPL,
and the plugins are LGPL. This allows you to use Magic to create closed source applications, while also
ensuring improvements to the project itself *stays* Open Source.
