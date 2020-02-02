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
sorting and filtering for you. Magic also automagically takes care of
authentication and authorization for you, allowing you to restrict user access to specific tables
based upon what role(s) the user belongs to.

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

## Maturity

Magic has been featured in MSDN Magazine with several articles, and is currently the only product
not produced my Microsoft that is documented at the main website for .Net and .Net Core. You can
find some of its articles below.

* [Make C# more dynamic with Hyperlambda](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/june/csharp-make-csharp-more-dynamic-with-hyperlambda)
* [Super-DRY development for ASP.NET Core](https://docs.microsoft.com/en-us/archive/msdn-magazine/2019/june/patterns-and-practices-super-dry-development-for-asp-net-core)
* [Active Events One design pattern instead of a dozen](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/march/patterns-active-events-one-design-pattern-instead-of-a-dozen)
* ++++

The main architect of Magic has researched Magic and its underlying ideas for more than a decade, and
has been working for some of the largest frinancial trading broker firms on the planet, in addition
to being delivering software for some of the largest hospitals on the planet. Magic is _very, very, very_
secure!

## Responsive

All components generated will be highly responsive, allowing you to consume your generated apps
from your favourite phone, tablet, or computer - Regardless of your device resolution.  But don't
believe us, try it out for yourself. Magic is free to use locally, and will only cost you anything
whenever you decide to deploy it unto a server. Magic also comes with [professional support](https://servergardens.com/)
if you decide to use it commercially on your own server.

[![Download magic](https://servergardens.files.wordpress.com/2020/01/new-download-button-2.png)](https://github.com/polterguy/magic/archive/v5.7.3.zip)

[Getting started with Magic](/getting-started)

[![Build status](https://travis-ci.org/polterguy/magic.svg?master)](https://travis-ci.org/polterguy/magic)
