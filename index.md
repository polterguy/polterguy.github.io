# The programming language that does your job

Magic allows you to create your entire Web app by simply clicking two buttons. The first button will
automatically create your backend, by wrapping your database tables into CRUD HTTP REST endpoints. The
second button will create an Angular frontend for you, wrapping your previously created backend
into an Angular Web application.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/r91tIBy1QbA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## How it works

Magic will read metadata from your database, and use this metadata to generate a Hyperlambda
HTTP REST Web API for you, wrapping all CRUD operations inside of REST endpoints. Then it will use
metadata from the REST API to automatically generate Angular components, router links, menu items,
datagrids, etc. The end result becomes that before you've even had to create as much as a single
line of code yourself, 50% of your job is already done.

The resulting frontend gives you a datagrid for all your database tables, allowing you
to create, read, update and delete records in your database. It also automatically creates paging,
sorting, and filtering for you - In addition to providing you with a _very, very, very_ secure
authentication and authorization system.

## Screenshots of example CRUD app

An example Magic CRUD app, with its nav bar expanded.

![An example Magic CRUD app](https://servergardens.files.wordpress.com/2020/01/magic-crud-1.png)

How the datagrid looks like when viewing your records.

![Viewing your database records in a datagrid](https://servergardens.files.wordpress.com/2020/01/magic-datagrid.png)

Editing a database record. Notice how it creates the correct components for your columns, based upon
what the underlying data type of your table is. In this particular example for instance, we have a
datetime-picker, because one of the table's columns is a datetime.

![Editing database records](https://servergardens.files.wordpress.com/2020/01/editing.png)

Below you can see how the integrated authentication and authorization components will look like.
Notice, all passwords are securely stored using individual salting and hashed based upon the BlowFish
hashing algorithm - Making the auth system extremely secure.

![The integrated auth system](https://servergardens.files.wordpress.com/2020/01/auth.png)

Magic also allows you to automatically create charts, based upon statistics endpoints, that returns
some sort of aggregate function grouped by some column from your database. Below you can see an example
from the Sakila database.

![Automatically generate statistical charts](https://servergardens.files.wordpress.com/2020/02/statistics-magic-sample.png)

## Hyperlambda

In addition to the CRUD backend and Angular frontend generator, Magic is also a complete DSL
engine, or Domain Specific programming Language engine - Giving you workflow support, task
scheduling, the ability to create your own DSL, dynamic HTTP endpoints, etc. Even if you
don't care about its CRUD generator, Magic would still be highly valuable, due to Hyperlambda.
Hyperlambda just so happens to easily lend itself towards generating backend and frontend
code, in addition to all the other things it helps you with.

## Task scheduler and workflows

Magic also includes a task scheduler and a workflow engine, allowing you to create, persist,
and execute serialized method invocations - Either periodically, or at a single point in the
future, triggered by some action, or at a specific date and time. This gives you the most
important features from Microsoft Workflow Foundation, without the weird and difficult to
understand XML syntax. Magic workflows also perfectly integrates with .Net Core, contrary to
MWF that only works for .Net Framework. Below is a screenshot of how you can manage your
tasks using the Magic Dashboard.

![Managing and scheduling your persisted tasks](https://servergardens.files.wordpress.com/2020/09/task-scheduler.png)

Below is an example of how it looks like as you're editing your tasks. Notice how the
Hyperlambda editor in Magic's dashboard gives you perfect autocompletion.

![Editing a persisted tasks](https://servergardens.files.wordpress.com/2020/09/task-schedule-editing.png)

## Productivity

If you run Magic towards a database with ~100 tables, Magic will generate roughly 5.000 lines of backend
code for you, in addition to 80.000 lines of frontend code. According to neutral research in
the topic, an average software developer can produce ~750 lines of code per month. This implies that
5 seconds with Magic _equals the productivity of a single developer for more than 9 years_.

The above comparisons isn't completely fair, but there is no doubt that
Magic will increase your productivity compared to having to manually create the
equivalent project(s).

In addition, you can often accomplish the same with 5 lines of Hyperlambda code, as you'll
need hundreds and sometimes thousands of lines of C# code to accomplish. This is due to that
Hyperlambda is an extremely high level programming language. Below is an example of sending
an email for instance. Compare this code to its C# equivalent.

```
mail.smtp.send
   message
      to
         John Doe:john@doe.com
      from
         Jane Doe:jane@doe.com
      subject:Subject line
      entity:text/plain
         content:Body content
```

## Maturity and security

Magic has been featured in MSDN Magazine with several articles, and is currently the only product
not produced by Microsoft that is documented at the main website for .Net and .Net Core. You can
find some of its articles below.

* [Make C# more dynamic with Hyperlambda](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/june/csharp-make-csharp-more-dynamic-with-hyperlambda) - The 5th most read article published by Microsoft _ever_
* [Active Events One design pattern instead of a dozen](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/march/patterns-active-events-one-design-pattern-instead-of-a-dozen) - The 20th most read article published by Microsoft
* [Super-DRY development for ASP.NET Core](https://docs.microsoft.com/en-us/archive/msdn-magazine/2019/june/patterns-and-practices-super-dry-development-for-asp-net-core) - Describes the idea of _"super DRY code"_, which is at the heart of Magic
* ++++

## Code quality and performance

A Magic application will outperform the equivalent Entity Framework solution with at least 5x in speed
and throughput, making it scale at least 5 times as well as an Entity Framework solution. In addition,
its generated code has an extremely high quality, and will for the most parts, perfectly obey by all
coding standards, and/or automated tools that are measuring code quality - Such as for instance TSlint,
SonarQube, etc. In neutral tests, Magic has shown to outperform the average (human) software developer by 10x
on code quality, using neutral and objective metrics measuring quality. This results in that your
Magic applications becomes extremely easy to maintain and modify if the need should arise.

* [Check out the Sonar Cloud quality gates for the project and its sub modules](https://sonarcloud.io/organizations/polterguy/projects?sort=-coverage)

## License Terms

Although 95% of Magic's source code is Open Source, and licensed as MIT, Magic will
[cost you a fee](https://servergardens.com/buy/) of €49 for a single developer license. One such license
allows a single developer to create and publish as many Magic applications as needed (no royalties).
The license is valid for the entirety of the current release cycle, which is the 8.x version, giving
you free updates.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic)

