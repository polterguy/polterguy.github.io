# Introduction

Magic allows you to create your entire Web app by simply clicking two buttons. The first button will
automatically create your backend, by wrapping your database tables into HTTP REST endpoints. The
second button will create an Angular frontend for you, wrapping your previously created backend
into an entire Web application. See the screenshot below for an example.

[![An example Magic CRUD app](https://servergardens.files.wordpress.com/2020/01/magic-crud-1.png)]

Of watch the following video for a demonstration of the above system, and how it was created.

<div style="margin-left: auto; margin-right: auto; width: 560px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/7zNh4Ekd67c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## How it works

Magic is built upon a YAML inspired syntax called _"Hyperlambda"_, that declares the code your endpoint
will evaluate when accessed. This makes it fairly easy to have your computer generate code from the metadata
extracted from your database. Think about these files as automatically generated XML files, except instead
of using XML, it is using Hyperlambda.

Magic is built in .Net Core, and allows you to add C# controllers to it easily. It's a highly modular
architecture, allowing you to intercept its core, using adapters and triggers.

## Scheduling code execution

In addition to the above, Magic also features a task scheduler, allowing you to dynamically create
tasks, that might repeat according to some sort of pattern, that executes code at some specified
point in time.

## License

Although most of Magic's source code is publicly available, it is not Free Software or Open Source,
and I do charge a fee for commercial usage. [Read more here](https://servergardens.com/buy/).

[Getting started with Magic](/getting-started)

[![Build status](https://travis-ci.org/polterguy/magic.svg?master)](https://travis-ci.org/polterguy/magic)
