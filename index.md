# Introduction

Magic allows you to create your entire Web app by simply clicking two buttons. The first button will
automatically create your backend, by wrapping your database tables into HTTP REST endpoints. The
second button will create an Angular frontend for you, wrapping your previously created backend
into an Angular Web application. Watch the following video for a demonstration of how Magic works.
Notice, the Web app in the video was created in its entirety _without writing a single line of code_!

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/7zNh4Ekd67c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
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

## License

Although most of Magic's source code is publicly available, it is not Free Software or Open Source,
and I do charge a fee for commercial usage. [Read more here](https://servergardens.com/buy/).

[Getting started with Magic](/getting-started)

[![Build status](https://travis-ci.org/polterguy/magic.svg?master)](https://travis-ci.org/polterguy/magic)
