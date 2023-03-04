---
title: Reference documentation for Magic and Hyperlambda
description: This section contains the reference documentation for Magic and Hyperlambda, and documents all plugins, Hyperlambda the programming language, and every single component in Magic.
---

# Magic and Hyperlambda structure

Aista Magic Cloud is not one project, it's more than 40 projects in fact. Each project encapsulates
some part of Hyperlambda, such as sending emails, parsing XML or JSON, etc. The core projects, or
the most _"important"_ projects if you wish, are the following.

* [magic.node](/documentation/magic.node/) - Nodes, lambda, Hyperlambda and Expressions
* [magic.signals](/documentation/magic.signals/) - Magic's Super Signals implementation or Active Events if you wish
* [magic.endpoint](/documentation/magic.endpoint/) - Endpoint resolving in Magic
* [magic.data.common](/documentation/magic.data.common/) - Commonalities for data adapters in Magic
* [magic.library](/documentation/magic.library/) - A single project wrapping everything together
* [magic.deploy](/documentation/magic.deploy/) - Deploying Magic to your VPS using Docker
* [magic.clone](/documentation/magic.clone/) - Cloning Magic and its entire codebase

The following are the _"plugins"_ projects for Magic and Hyperlambda, typically implementing one or more
slots each, whom in its combined results becomes the programming language called Hyperlambda. These are the parts
that allows you to interact with your database, apply authentication and authorization requirements for your
endpoints, etc.

* [magic.lambda](/documentation/magic.lambda/) - The Hyperlambda DSL, and its primary keywords
* [magic.lambda.math](/documentation/magic.lambda.math/) - Math operations from Hyperlambda
* [magic.lambda.http](/documentation/magic.lambda.http/) - Invoking HTTP endpoints from Hyperlambda
* [magic.lambda.csv](/documentation/magic.lambda.csv/) - Parsing and creating CSV from Hyperlambda
* [magic.lambda.json](/documentation/magic.lambda.json/) - Parsing and creating JSON and YAML from Hyperlambda
* [magic.lambda.html](/documentation/magic.lambda.html/) - Parsing and creating HTML and Markdown from Hyperlambda
* [magic.lambda.xml](/documentation/magic.lambda.xml/) - Parsing and creating XML from Hyperlambda
* [magic.lambda.mail](/documentation/magic.lambda.mail/) - Sending and retrieving emails from Hyperlambda
* [magic.lambda.mime](/documentation/magic.lambda.mime/) - Parsing MIME messages in Hyperlambda
* [magic.lambda.auth](/documentation/magic.lambda.auth/) - Authentication and authorisation in Hyperlambda
* [magic.lambda.dates](/documentation/magic.lambda.dates/) - Manipulating DateTime objects from Hyperlambda
* [magic.lambda.slots](/documentation/magic.lambda.slots/) - Creating your own dynamic slots or functions
* [magic.lambda.mysql](/documentation/magic.lambda.mysql/) - Accessing your MySQL server from Hyperlambda
* [magic.lambda.pgsql](/documentation/magic.lambda.pgsql/) - Accessing your PostgreSQL server from Hyperlambda
* [magic.lambda.mssql](/documentation/magic.lambda.mssql/) - Accessing your MS SQL Server from Hyperlambda
* [magic.lambda.sqlite](/documentation/magic.lambda.sqlite/) - Accessing your SQLite database from Hyperlambda
* [magic.lambda.odbc](/documentation/magic.lambda.odbc/) - Accessing an ODBC connection from Hyperlambda
* [magic.lambda.image](/documentation/magic.lambda.image/) - Image library, allowing you to manipulate images
* [magic.lambda.crypto](/documentation/magic.lambda.crypto/) - Cryptography helpers for Hyperlambda
* [magic.lambda.guid](/documentation/magic.lambda.guid/) - Creating a guid from Hyperlambda
* [magic.lambda.config](/documentation/magic.lambda.config/) - Accessing configuration values from Hyperlambda
* [magic.lambda.logging](/documentation/magic.lambda.logging/) - Logging from Hyperlambda
* [magic.lambda.caching](/documentation/magic.lambda.caching/) - Caching from Hyperlambda
* [magic.lambda.strings](/documentation/magic.lambda.strings/) - Manipulate strings in Hyperlambda
* [magic.lambda.scheduler](/documentation/magic.lambda.scheduler/) - Create scheduled tasks and workflows from Hyperlambda
* [magic.lambda.validators](/documentation/magic.lambda.validators/) - Validate input in Hyperlambda
* [magic.lambda.hyperlambda](/documentation/magic.lambda.hyperlambda/) - Parsing and creating Hyperlambda
* [magic.lambda.sockets](/documentation/magic.lambda.sockets/) - Web socket support for Magic using SignalR
* [magic.lambda.threading](/documentation/magic.lambda.threading/) - Thread support for Magic and Hyperlambda
* [magic.lambda.pdf](/documentation/magic.lambda.pdf/) - PDF support for Magic and Hyperlambda
* [magic.lambda.openai](/documentation/magic.lambda.openai/) - OpenAI specific slots

In addition to the above projects, Magic also contains [middleware](/documentation/magic/), which is the
dashboard components, and the Hyperlambda endpoints we provide out of the box. On Aista's YouTube channel you will also
find several playlists, that guides you through the entire platform.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/videoseries?list=PLgyI389Eb9HNlhKpF9EHXO7D1EE7_dklg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Support

If you have a support request of private nature, you can send us an email
at [info@aista.com](mailto:info@aista.com). If you want to submit a feature request or a bug report,
you can do this at [github.com/polterguy/magic/issues](https://github.com/polterguy/magic/issues).
We would also love to discuss Magic with you
at [github.com/polterguy/magic/discussions](https://github.com/polterguy/magic/discussions)

## Quality

Each projects in Aista Magic Cloud is statically analysed for code issues using SonarCloud. This ensures
high quality code, and helps us stabilise the platform as a whole. Each time we create a new release, we
verify the build status of each project in the platform, ensuring we don't accidentally implement bugs,
somehow breaking the platform. This process includes running unit tests automatically as we push code
towards Magic's GitHub repository, analysing the code to verify it's not unnecessary complex, and make sure
the code is DRY, implying it does not repeat itself and follows all best practices.

<table>
   <tr>
      <th>Source</th>
      <th>Build</th>
      <th>Quality</th>
      <th>LOC</th>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.node">magic.node</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.node/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.node&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.node&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.signals">magic.signals</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.signals/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.signals&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.signals&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.endpoint">magic.endpoint</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.endpoint/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda">magic.lambda</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.library">magic.library</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.library/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.data.common">magic.data.common</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.data.common/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.data.cql">magic.data.cql</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.data.cql/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.cql&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.mysql">magic.lambda.mysql</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.mysql/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.pgsql">magic.lambda.pgsql</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.pgsql/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pgsql&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pgsql&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.mssql">magic.lambda.mssql</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.mssql/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.odbc">magic.lambda.odbc</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.odbc/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.http">magic.lambda.http</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.http/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.hyperlambda">magic.lambda.hyperlambda</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.hyperlambda/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.io">magic.lambda.io</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.io/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.math">magic.lambda.math</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.math/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.strings">magic.lambda.strings</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.strings/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.strings&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.validators">magic.lambda.validators</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.validators/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.auth">magic.lambda.auth</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.auth/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.slots">magic.lambda.slots</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.slots/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.slots&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.sockets">magic.lambda.sockets</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.sockets/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.caching">magic.lambda.caching</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.caching/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.config">magic.lambda.config</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.config/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.crypto">magic.lambda.crypto</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.crypto/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.csv">magic.lambda.csv</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.csv/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.dates">magic.lambda.dates</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.dates/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.guid">magic.lambda.guid</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.guid/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.guid&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.guid&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.html">magic.lambda.html</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.html/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.xml">magic.lambda.xml</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.xml/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.image">magic.lambda.image</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.image/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.image&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.image&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.json">magic.lambda.json</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.json/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.logging">magic.lambda.logging</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.logging/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.logging&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.mail">magic.lambda.mail</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.mail/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.mime">magic.lambda.mime</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.mime/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.scheduler">magic.lambda.scheduler</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.scheduler/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.threading">magic.lambda.threading</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.threading/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.threading&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.system">magic.lambda.system</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.system/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=ncloc"></td>
   </tr>
   <tr>
      <td><a href="https://github.com/polterguy/magic.lambda.ad-auth">magic.lambda.ad-auth</a></td>
      <td><img alt="Build badge" src="https://github.com/polterguy/magic.lambda.ad-auth/actions/workflows/build.yaml/badge.svg"></td>
      <td><img alt="Quality gate" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=alert_status"></td>
      <td><img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=ncloc"></td>
   </tr>
</table>

If you want to dive into the QA details of each project, you can find Magic's SonarCloud page at
[sonarcloud.io/organizations/polterguy/projects?sort=-coverage](https://sonarcloud.io/organizations/polterguy/projects?sort=-coverage).

## License

Magic is 100% Open Source and free of charge to use. The main backend is licensed as MIT, the dashboard is GPL,
and the plugins are LGPL. This allows you to use Magic to create closed source applications, while also
ensuring improvements to the project itself *stays* Open Source.
