# DB + Magic == Angular and .Net Core Web app

Magic allows you to create your entire Web app by simply clicking two buttons. The first button will
automatically create your backend, by wrapping your database tables into CRUD HTTP REST endpoints. The
second button will create an Angular frontend for you, wrapping your previously created backend
into an Angular Web application. Watch the following video for a demonstration of how Magic works.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/8xO9H-2Fejc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## How it works

Magic will read metadata from your database, and use this metadata to generate an HTTP REST Web
API for you, wrapping all CRUD operations inside of REST endpoints. Then it will use metadata from
the REST API to automatically generate Angular components, router links, menu items, datagrids, etc.
The end result becomes that before you've even had to create as much as a single line of code 
yourself, 50% of your job is already done.

The resulting frontend gives you a datagrid for all your database tables, allowing you
to create, read, update and delete records in your database. It also automatically creates paging,
sorting, and filtering for you - In addition to providing you with a _very, very, very_ secure
authentication and authorisation system.

Magic is built in .Net Core, and allows you to expand upon it with your own C# controllers easily.
It's a highly modular and extendible architecture, allowing you to intercept its core, using adapters
and triggers. The Angular code also perfectly follows TSLint rules, making it highly readable and
easily modified. The process of creating your CRUD apps is also highly configurable, allowing you
to modify any aspect of the end result, before you start coding.

## Screenshots

An example Magic CRUD app, with its nav bar expanded.

![An example Magic CRUD app](https://servergardens.files.wordpress.com/2020/01/magic-crud-1.png)

How the datagrid looks like when viewing your records.

![Viewing your database records in a datagrid](https://servergardens.files.wordpress.com/2020/01/magic-datagrid.png)

Editing a database record. Notice how it creates the correct components for your columns, based upon
what the underlying data type of your table is. In this particular example for instance, we have a
datetime-picker, because one of the table's columns is a datetime.

![Editing database records](https://servergardens.files.wordpress.com/2020/01/editing.png)

Below you can see how the integrated authentication and authorisation components will look like.
Notice, all passwords are securely stored using individual salting and hashed based upon the BlowFish
hashing algorithm - Making the auth system extremely secure.

![The integrated auth system](https://servergardens.files.wordpress.com/2020/01/auth.png)

Magic also allows you to automatically create charts, based upon statistics endpoints, that returns
some sort of aggregate function grouped by some column from your database. Below you can see an example
from the Sakila database.

![Automatically generate statistical charts](https://servergardens.files.wordpress.com/2020/02/statistics-magic-sample.png)

## Productivity

If you run Magic towards a database with ~100 tables, Magic will generate roughly 5.000 lines of backend
code for you, in addition to 80.000 lines of frontend code. According to neutral research in
the topic, an average software developer can produce ~750 lines of code per month. This implies that
5 seconds with Magic _equals the productivity of a single developer for more than 9 years_.

Of course, these types of comparisons aren't fully fair some may argue, but there is no doubt that
Magic will soar your productivity to unimaginable heights compared to having to manually create
the equivalent project.

## Maturity and security

Magic has been featured in MSDN Magazine with several articles, and is currently the only product
not produced by Microsoft that is documented at the main website for .Net and .Net Core. You can
find some of its articles below.

* [Make C# more dynamic with Hyperlambda](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/june/csharp-make-csharp-more-dynamic-with-hyperlambda)
* [Super-DRY development for ASP.NET Core](https://docs.microsoft.com/en-us/archive/msdn-magazine/2019/june/patterns-and-practices-super-dry-development-for-asp-net-core)
* [Active Events One design pattern instead of a dozen](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/march/patterns-active-events-one-design-pattern-instead-of-a-dozen)
* ++++

The main architect of Magic has researched Magic and its underlying ideas for more than a decade, and
has been working and consulting for some of the largest financial trading broker firms on the planet - Some of whom
are operating in markets moving 5.1 trillion dollars on a daily basis. Needles to say, but Magic is
_very, very, very_ secure. For some of these firms, Magic has saved millions of dollars
in development costs, while at the same time tightened security significantly.

Magic was also built using a TDD approach, and there are hundreds of unit tests in the project, that
verifies the integrity of every possible course of code flow, whenever we apply change to its underlying
code. Magic's source code, has also been scrutinised by thousands of (human) developers, without being able
to find any security holes in it.

## Code quality and performance

A Magic application will outperform the equivalent Entity Framework solution with at least 5x in speed
and throughput, making it scale at least 5 times as well as an Entity Framework solution. In addition,
its generated code has an extremely high quality, and will for the most parts, perfectly obey by all
coding standards, and/or automated tools that are measuring code quality - Such as for instance TSlint,
SonarCube, etc. In neutral tests, Magic has shown to outperform the average (human) software developer by 10x
on code quality, using neutral and objective metrics measuring quality. This results in that your
resulting Magic application is extremely easy to maintain and modify if the need should arise.

* [Check out the Sonar Cloud quality gates for the project and its sub modules](https://sonarcloud.io/organizations/polterguy/projects?sort=-name)

The project also complies 100% perfectly towards SOLID coding standards, and every aspect of the framework
is extendible, allowing you to inject custom logic, and/or change its existing logic, without knowing
anything abouts its internals in any ways. There are probably very few .Net Core projects in this world,
if any, with the same [Quality Gate results](https://sonarcloud.io/organizations/polterguy/projects?sort=-name)
as Magic. Each sub module in Magic has on average between 85-100% Unit Test coverage, ignoring some of the
modules where unit testing cannot be performed.

## License Terms

Although 95% of Magic's source code is Open Source, and licensed as MIT, Magic will
[cost you a fee](https://servergardens.com/buy/) of €49 for a single developer license. This allows you to
create and publish as many Magic applications as you please (no royalties).

## Quid Pro Quo initiative

Magic is 95% Open Source, but you do need a license key to run it in your production server, otherwise
Magic will stop working after 7 days. However, we believe strongly in the value of Open Source and
sharing knowledge. Hence, if you are an author writing technical articles for [DZone](https://dzone.com),
or similar websites, and/or you need a license for your Open Source Magic project, or to evaluate Magic -
You can send an email to us at license@servergardens.com, and we _might_ give you a free license, if you
explain your project, and or your intentions to use Magic, and you _do not_ share your license key with
anybody else.

## Reference documentation

Below you can find the reference documentation for Magic's sub modules.

* [Magic Node](/magic.node) - Explains nodes, Hyperlambda and Expressions
* [Magic Lambda](/magic.lambda) - Explains all _"keywords"_ in Hyperlambda
* [Magic Endpoint](/magic.endpoint) - Endpoint resolving in Magic
* [Magic Data Common](/magic.data.common) - Commonalities for data adapters in Magic
* [Magic Lambda MySQL](/magic.lambda.mysql) - Accessing your MySQL server from Hyperlambda
* [Magic Lambda MS SQL](/magic.lambda.mssql) - Accessing your MS SQL Server from Hyperlambda
* [Magic Lambda Logging](/magic.lambda.logging) - Logging from Hyperlambda
* [Magic Lambda Caching](/magic.lambda.caching) - Caching from Hyperlambda
* [Magic Lambda IO](/magic.lambda.io) - File manipulation using Hyperlambda
* [Magic Lambda Hyperlambda](/magic.lambda.hyperlambda) - Parse Hyperlambda from text, and vice versa
* [Magic Lambda HTTP](/magic.lambda.http) - Invoking HTTP REST endpoints from Hyperlambda
* [Magic Lambda Crypto](/magic.lambda.crypto) - Cryptography helpers for Hyperlambda
* [Magic Lambda Config](/magic.lambda.config) - Accessing configuration values from Hyperlambda
* [Magic Lambda Scheduler](/magic.lambda.scheduler) - Create scheduled tasks and workflows from Hyperlambda
* [Magic Lambda JSON](/magic.lambda.json) - Manipulating JSON from Hyperlambda
* [Magic Lambda Mail](/magic.lambda.mail) - Sending and retrieving emails from Hyperlambda
* [Magic Lambda MIME](/magic.lambda.mime) - Parsing email messages in Hyperlambda
* [Magic Lambda Slots](/magic.lambda.slots) - Dynamically create your own slots/functions
* [Magic Lambda Strings](/magic.lambda.strings) - Manipulate strings in Hyperlambda
* [Magic Lambda Math](/magic.lambda.math) - Math operations from Hyperlambda
* [Magic Lambda Dates](/magic.lambda.dates) - Allows you to manipulate DateTime objects from Hyperlambda
* [Magic Lambda Auth](/magic.lambda.auth) - Authentication and authorisation from Hyperlambda
* [Magic Lambda Validators](/magic.lambda.validators) - Validate input in Hyperlambda
* [Magic IO](/magic.io) - IO operations in Magic
* [Magic HTTP](/magic.http) - HTTP rest invocations in Magic
* [Magic Library](/magic.library) - A single NuGet package helper tying everything easily together
