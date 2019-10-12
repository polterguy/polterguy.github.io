# Introduction

Magic allows you to wrap your database into HTTP REST endpoints for each CRUD operation towards your tables
at the click of a button. It works by extracting meta information from your database, for then to generate
a code file for POST, GET, PUT and DELETE, representing the **C**reate, **R**ead, **U**pdate and **D**elete
operations. This allows you to create an HTTP REST backend wrapping your database, literally in seconds.

<div style="margin-left: auto; margin-right: auto; width: 560px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/4TyT4lBEOg8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## How it works

Magic is built upon a YAML inspired syntax called _"Hyperlambda"_, that declares the code your endpoint
will evaluate when accessed. This makes it fairly easy to have your computer generate code from the metadata
extracted from your database. Think about these files as automatically generated XML files, except instead
of using XML, it is using Hyperlambda.

Magic is built in .Net Core, and allows you to add C# controllers to it easily. It's a highly modular
architecture, allowing you to intercept its core, using adapters and triggers.

[Getting started with Magic](/getting-started)

[![Build status](https://travis-ci.org/polterguy/magic.svg?master)](https://travis-ci.org/polterguy/magic)
