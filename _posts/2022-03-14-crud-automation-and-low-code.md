---
layout: post
author: thomas
title: CRUD automation and Low-Code
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg"
description: With Aista Magic Cloud you can create CRUD HTTP endpoints wrapping your database in seconds.
---

CRUD is probably one of the most boring tasks you can possibly do as a software developer, especially if you have a large database with hundreds of tables, and you need to create CRUD endpoints wrapping your entire database. With Magic you can [automatically create CRUD API endpoints in seconds](https://docs.aista.com/) by simply clicking a button. Below is a screenshot. The process is extremely simply; Choose your database, configure your endpoints, click a button - And two seconds later Magic has produced thousands of lines of code for you 100% automatically, wrapping every single table inside CRUD HTTP endpoints for you without you having to write a single line of code yourself.

![CRUD automation](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

You can of course configure the process and provide custom authorisation requirements for each endpoint, publish socket messages as endpoints are invoked, create log entries if you wish, etc, etc, etc. Magic also automatically generates join SQL statements for you for referenced tables, and you can select which CRUD verbs you want to have Magic create for you on a per table basis. Basically, you've got more or less 100% control over the process through checkboxes and a simple to use UI.

## Customising your endpoints with Hyper IDE

After you're done generating your CRUD HTTP web API you can easily customise your endpoints. Magic's output is Hyperlambda which is an easily understood DSL you can edit with Magic's integrated IDE. Below is a screenshot of Hyper IDE allowing you to edit your endpoints after the _"Crudifier"_ is done doing its magic. Hyper IDE again is a lightweight web based integrated development environment allowing you to easily edit your code, save it, for then to immediately see the result. Hyper IDE provides syntax highlighting, autocomplete, and even works perfectly from your phone.

![Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

Although Hyper IDE is best suited for Hyperlambda, you can still use it to edit CSS, HTML, JavaScript, TypeScript, and most other popular programming languages. You can also invoke your endpoints directly from Hyper IDE, such as illustrated below. Hyper IDE has its own integrated _"Postman"_ component allowing you to immediately invoke your endpoints as you're editing your code. This allows you to immediately see the result of changes to your code providing you with _"instant feedback"_, reducing the amount of time it takes for you to discover bugs in your code.

![Invoking your endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-blog.jpg)

## Creating HTTP endpoints with SQL

Every now and then you need some sort of KPI, and/or statistical component in your frontend, at which point typically the bulk of your code is SQL. With Magic you can easily create HTTP endpoints using nothing but good old fashion SQL. Below is a screenshot of the integrated SQL editor where we're creating a fairly complex join SQL statement, for then to wrap our SQL inside an HTTP endpoint. The following screenshot also illustrates how to allow for your endpoint to take arguments, which again becomes parts of your SQL statement to for instance filter your results, etc.

![SQL HTTP endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

## Automatically generate an Angular frontend

When you're done with generating your backend, you can also just as easily create an Angular frontend by simply clicking another button. Below is a screenshot of how your end result might end up looking like. However, you can also test the [following automatically generated CRUD app](https://sakila.servergardens.com/) with the username/password combination of __admin__/__admin__. Please realise that we started out with nothing but an existing database, and we created a CRUD web API in 1 second, for then to create the following Angular app in 1 second. All in all we're talking about 2 seconds of _"coding"_ here, and some few minutes to build and deploy our result to a VPS.

![CRUD Angular frontend](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sakila.jpg)

## Magic is Open Source

As a final touch, everything we did above is 100% open source and free of charge to use, also in your own closed source projects. If you're interested in trying it out for yourself, you can download Magic below. Magic also contains many more components helping you out with your software development efforts, ranging from an integrated SQL editor replacing MySQL Workbench, integrated audit logging components, a Micro Service _"AppStore"_, etc, etc, etc. What we showed you here was only 3/4 of the components you find in Magic. Magic has 16 components in total. I would appreciate it if you gave our project a star on [Magic's GitHub project page](https://github.com/polterguy/magic). And of course if you try out Magic we would love to hear what you think about it.

* [Download Aista Magic Cloud](https://docs.aista.com/)
