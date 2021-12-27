
# Documentation for Magic

This is the official documentation for Magic, and it contains both reference documentation
and tutorial style type of documentation. If you've just recently started to use Magic, I
suggest you start out with the architectural overview video, move on to tutorials starting
out at the top, and move downwards - For then to read the reference documentation as you need
detailed information about specific parts of Magic.

## Architectural overview

In this video I walk you through the architecture of Magic from a bird's perspective, in addition
to that I illustrate how to create a simple Hello World Hyperlambda app.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/FK0rcAEWtV8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Tutorials

* [Getting started](/tutorials/getting-started/) - Getting Magic up running
* [Database CRUD operations](/tutorials/database-crud/) - Automate the process of creating code
* [SQL Web API](/tutorials/sql-web-api/) - Create HTTP endpoints in SQL
* [Magic beyond CRUD](/tutorials/cloud-ide/) - A guided tour through Magic's Dashboard
* [Web Sockets and SignalR in Magic](/tutorials/web-sockets/) - How to use Web Sockets with Magic
* [Authentication and authorisation](/tutorials/auth/) - How Magic solves authentication and authorisation
* [Hyperlambda Hello World](/tutorials/hello-world-endpoint/) - Your first Hyperlambda endpoint
* [Super DRY code](/tutorials/super-dry/) - Exception handlers and interceptors
* [Threading, async and scaling](/tutorials/threading/) - How Hyperlambda simplifies threading and async
* [HTTP REST invocations](/tutorials/http-rest/) - How Hyperlambda simplifies HTTP REST invocations
* [Dynamic slots](/tutorials/dynamic-slots/) - How to create dynamic Hyperlambda slots
* [Scheduling tasks](/tutorials/task-scheduler/) - How to use Magic to create and schedule tasks
* [Cryptographically secured HTTP Lambda Invocations](/tutorials/crypto-lambda-http/) - Inversion of Code
* [Expressions, slots, and nodes](/tutorials/expressions-slots-nodes/) - Hyperlambda is *really* weird!
* [Authentication internals](/tutorials/auth-internals/) - How to use for instance Windows authentication
* [Using Magic with SQL Server](/tutorials/sql-server/) - Using Magic with Microsoft SQL Server
* [Using Magic with PostgreSQL](/tutorials/postgresql/) - Using Magic with PostgreSQL

## Reference documentation core projects

* [magic.node](/documentation/magic.node/) - Explains nodes, Hyperlambda and Expressions
* [magic.signals](/documentation/magic.signals/) - Magic's Super Signals implementation
* [magic.endpoint](/documentation/magic.endpoint/) - Endpoint resolving in Magic
* [magic.lambda](/documentation/magic.lambda/) - Explains Hyperlambda as a DSL, and its keywords

## Reference documentation plugins

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
* [magic.lambda.pgsql](/documentation/magic.lambda.pgsql/) - Accessing your PostgreSQL server from Hyperlambda
* [magic.lambda.mssql](/documentation/magic.lambda.mssql/) - Accessing your MS SQL Server from Hyperlambda
* [magic.lambda.odbc](/documentation/magic.lambda.odbc/) - Accessing an ODBC connection from Hyperlambda
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

## Utility projects

* [magic.data.common](/documentation/magic.data.common/) - Commonalities for data adapters in Magic
* [magic.library](/documentation/magic.library/) - A single NuGet package helper tying everything easily together
* [magic.deploy](/documentation/magic.deploy/) - How to deploy Magic to your VPS using Docker.
* [magic.clone](/documentation/magic.clone/) - How to clone Magic and its entire codebase.

## Support

If you have a support request of private nature, or another type of request, you can send me
email at [thomas@servergardens.com](mailto:thomas@servergardens.com). If you want to submit a
feature request or a bug report, you can do such through the project's
[GitHub Issues](https://github.com/polterguy/magic/issues).

* [thomas@servergardens.com](mailto:thomas@servergardens.com)

## Build status

Below you can find the build status of all satellite rojects in their respective master branches, and the links
to the GitHub project pages. The build status is only relevant if you want to clone Magic Cloud, and
all of its satellite projects, using for instance [magic.clone](https://github.com/polterguy/magic.clone). The
build status is not relevant if you just want to download the latest code version, and/or use the Docker images,
since we quality assure all projects by making sure all unit tests, builds, and quality gates succeeds before we
create new releases of Magic.

<table>
   <tr>
      <th>Project</th>
      <th>Source</th>
      <th>Build</th>
      <th>Quality</th>
   </tr>
   <tr>
      <td>magic.data.common</td>
      <td><a href="https://github.com/polterguy/magic.data.common">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.data.common/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.endpoint</td>
      <td><a href="https://github.com/polterguy/magic.endpoint">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.endpoint/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda</td>
      <td><a href="https://github.com/polterguy/magic.lambda">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.ad-auth</td>
      <td><a href="https://github.com/polterguy/magic.lambda.ad-auth">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.ad-auth/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.auth</td>
      <td><a href="https://github.com/polterguy/magic.lambda.auth">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.auth/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.caching</td>
      <td><a href="https://github.com/polterguy/magic.lambda.caching">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.caching/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.config</td>
      <td><a href="https://github.com/polterguy/magic.lambda.config">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.config/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.crypto</td>
      <td><a href="https://github.com/polterguy/magic.lambda.crypto">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.crypto/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.csv</td>
      <td><a href="https://github.com/polterguy/magic.lambda.csv">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.csv/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.dates</td>
      <td><a href="https://github.com/polterguy/magic.lambda.dates">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.dates/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.guid</td>
      <td><a href="https://github.com/polterguy/magic.lambda.guid">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.guid/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.guid&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.html</td>
      <td><a href="https://github.com/polterguy/magic.lambda.html">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.html/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.http</td>
      <td><a href="https://github.com/polterguy/magic.lambda.http">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.http/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.hyperlambda</td>
      <td><a href="https://github.com/polterguy/magic.lambda.hyperlambda">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.hyperlambda/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.image</td>
      <td><a href="https://github.com/polterguy/magic.lambda.image">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.image/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.image&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.io</td>
      <td><a href="https://github.com/polterguy/magic.lambda.io">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.io/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.json</td>
      <td><a href="https://github.com/polterguy/magic.lambda.json">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.json/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.logging</td>
      <td><a href="https://github.com/polterguy/magic.lambda.logging">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.logging/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.mail</td>
      <td><a href="https://github.com/polterguy/magic.lambda.mail">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.mail/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.math</td>
      <td><a href="https://github.com/polterguy/magic.lambda.math">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.math/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.mime</td>
      <td><a href="https://github.com/polterguy/magic.lambda.mime">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.mime/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.mssql</td>
      <td><a href="https://github.com/polterguy/magic.lambda.mssql">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.mssql/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.mysql</td>
      <td><a href="https://github.com/polterguy/magic.lambda.mysql">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.mysql/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.odbc</td>
      <td><a href="https://github.com/polterguy/magic.lambda.odbc">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.odbc/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.pgsql</td>
      <td><a href="https://github.com/polterguy/magic.lambda.pgsql">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.pgsql/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pgsql&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.scheduler</td>
      <td><a href="https://github.com/polterguy/magic.lambda.scheduler">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.scheduler/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.slots</td>
      <td><a href="https://github.com/polterguy/magic.lambda.slots">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.slots/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.sockets</td>
      <td><a href="https://github.com/polterguy/magic.lambda.sockets">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.sockets/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.strings</td>
      <td><a href="https://github.com/polterguy/magic.lambda.strings">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.strings/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.lambda.system</td>
      <td><a href="https://github.com/polterguy/magic.lambda.system">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.system/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=alert_status"></td>
   </tr>
   
   <tr>
      <td>magic.lambda.validators</td>
      <td><a href="https://github.com/polterguy/magic.lambda.validators">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.validators/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.library</td>
      <td><a href="https://github.com/polterguy/magic.library">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.library/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.signals</td>
      <td><a href="https://github.com/polterguy/magic.signals">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.signals/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.signals&metric=alert_status"></td>
   </tr>
   <tr>
      <td>magic.node</td>
      <td><a href="https://github.com/polterguy/magic.node">link</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.node/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.node&metric=alert_status"></td>
   </tr>
</table>

# License

Magic is 100% Open Source and free of charge to use. The main backend is licensed as MIT, the dashboard is GPL,
and the plugins are LGPL. This allows you to use Magic to create closed source applications, while also
ensuring improvements to the project itself *stays* Open Source.
