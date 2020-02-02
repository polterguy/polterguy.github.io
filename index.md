# Database + Magic == Angular Web app

Magic allows you to create your entire Web app by simply clicking two buttons. The first button will
automatically create your backend, by wrapping your database tables into HTTP REST endpoints. The
second button will create an Angular frontend for you, wrapping your previously created backend
into an Angular Web application. Watch the following video for a demonstration of how Magic works.
Notice, the Web app in the video was created in its entirety _without writing a single line of code_!

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/8xO9H-2Fejc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## How it works

Magic will read metadata from your database. It will use this metadata to generate an HTTP REST Web
API for you, wrapping all CRUD operations inside of REST endpoints. Then it will use metadata from
the REST API to automatically generate Angular components, router links, menu items, datagrids, etc.
The end result becomes that before you've even had to create as much as a single line of code 
yourself, 90% of your job is already done.

The resulting frontend gives you a datagrid for all your database tables, allowing you
to create, read, update and delete records in your database. It also automatically creates paging,
sorting, and filtering for you - In addition to providing you with a _very, very, very_ secure
authentication and authorisation system.

Magic is built in .Net Core, and allows you to add C# controllers to it easily. It's a highly modular
architecture, allowing you to intercept its core, using adapters and triggers. The Angular code also
perfectly follows all TSLint rules, making it highly readable and easily modified.

## Screenshots

An example Magic CRUD app, with its nav bar expanded.

![An example Magic CRUD app](https://servergardens.files.wordpress.com/2020/01/magic-crud-1.png)

How the datagrid looks like when viewing your records.

![Viewing your database records in a datagrid](https://servergardens.files.wordpress.com/2020/01/magic-datagrid.png)

Editing a database record. Notice how it creates the correct components for your columns, based upon
what the underlying data type of your table is. In this particular example for instance, we have a
date and time picker, because one of the table's columns is of datetime type.

![Editing database records](https://servergardens.files.wordpress.com/2020/01/editing.png)

Below you can see how the integrated authentication and authorisation components will look like.
Notice, all passwords are securely stored using individual salting and hashed based upon the BlowFish
hashing algorithm - Making the auth system extremely secure.

![The integrated auth system](https://servergardens.files.wordpress.com/2020/01/auth.png)

## Productivity

If you run Magic towards a database with ~100 tables, Magic will generate roughly 5.000 lines of backend
code for you, in addition to 80.000 lines of frontend code. According to neutral research in
the topic, an average software developer can produce ~750 lines of code per month. This implies that
5 seconds with Magic _equals the productivity of a single developer for more than 9 years_.

Of course, these types of comparisons aren't fully fair some may argue, but there is no doubt that
Magic will soar your productivity to unimaginable heights compared to having to manually create
the equivalent product.

> I guarantee you that with Magic, you can get away with 50% of your developers, still while being 10x as productive

Thomas Hansen, CEO at Server Gardens

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
in recruitment costs, and tightened existing security by at least 10x on all parameters.

Magic was also built using a TDD approach, and there are hundreds of unit tests in the project, that
verifies the integrity of every possible course of code flow, whenever we apply change to its underlying
code. Magic's source code, has also been scrutinised by thousands of (human) developers, without being able
to find any security holes in it.

> I guarantee you that Magic, if setup correctly, will pass any penetration test on this planet

Thomas Hansen, CEO at Server Gardens

## Code quality and performance

A Magic application will outperform the equivalent Entity Framework solution with at least 5x in speed
and throughput, making it scale at least 5 times as well as an Entity Framework solution. In addition,
its generated code has an extremely high quality, and will for the most parts, perfectly obey by all
coding standards, and/or automated tools that are measuring code quality - Such as for instance TSlint,
etc. In neutral tests, Magic has shown to outperform the average (human) software developer by 3-4 times
on code quality, using neutral and objective metrics measuring such things. This results in that your
resulting Magic application is extremely easy to maintain and modify if the need should arise.

> I guarantee you that Magic will be able to create better code than every single human developer you have in your team

Thomas Hansen, CEO at Server Gardens

## Responsive

All components generated will be highly responsive, allowing you to consume your generated apps
from your favourite phone, tablet, or computer - Regardless of your device resolution.  But don't
believe us, try it out for yourself. Magic is free to use locally, and will only cost you anything
whenever you decide to deploy it unto a server. Magic also comes with [professional support](https://servergardens.com/)
if you decide to use it commercially on your own server, and Server Gardens also has a team of extremely
brilliant developers, in all areas related to the operation of Magic, if you need help to deploy it into
production.

> I guarantee you that your Magic app, will perfectly work, on every single modern device in your enterprise

Thomas Hansen, CEO at Server Gardens

> We realised there was a need for higher code quality, tightened security measures, and more automation
in the enterprise software development space - So we released Magic to the public, allowing others
to take advantage of the same quality improvements we could internally see within our own enterprise.

Thomas Hansen, CEO at Server Gardens

[![Download magic](https://servergardens.files.wordpress.com/2020/01/new-download-button-2.png)](https://github.com/polterguy/magic/archive/v5.7.3.zip)

[![Build status](https://travis-ci.org/polterguy/magic.svg?master)](https://travis-ci.org/polterguy/magic)
