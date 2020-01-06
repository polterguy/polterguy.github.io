# Introduction

Magic allows you to create your entire Web app by simply clicking two buttons. The first button will
automatically create your backend, by wrapping your database tables into HTTP REST endpoints. The
second button will create an Angular frontend for you, wrapping your previously created backend
into an entire Web application. See the screenshot below for an example.

![An example Magic CRUD app](https://servergardens.files.wordpress.com/2020/01/magic-crud-1.png)

Or watch the following video for a demonstration of the above system, and how it was created.
Notice, the above Web app was created in its entirety _without writing a single line of code_!

<div style="margin-left: auto; margin-right: auto; width: 560px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/7zNh4Ekd67c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## How it works

Magic will read metadata from your database. It will use this metadata to generate an HTTP REST Web
API for you, wrapping all CRUD operations inside of REST endpoints. Then it will use metadata from
the REST API to automatically generate Angular components, router links, menu items, datagrids, etc.
The end result becomes that before you've even had to create as much as a single line of code 
yourself, 90% of your job is already done.

The resulting frontend, gives you datagrids and tables for all your database tables, allowing you
to create, read, update and delete from all of your database tables. It also features paging,
sorting, filtering, etc automatically created for you.

Magic is built in .Net Core, and allows you to add C# controllers to it easily. It's a highly modular
architecture, allowing you to intercept its core, using adapters and triggers. And the resulting 
Angular code is also very clean, and easy to modify.

## License

Although most of Magic's source code is publicly available, it is not Free Software or Open Source,
and I do charge a fee for commercial usage. [Read more here](https://servergardens.com/buy/).

[Getting started with Magic](/getting-started)

[![Build status](https://travis-ci.org/polterguy/magic.svg?master)](https://travis-ci.org/polterguy/magic)
