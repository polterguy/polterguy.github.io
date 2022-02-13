---
title: Hyper IDE, a web based IDE
description: Hyper IDE is a fully fledged integrated development environment, giving you most important features from other IDEs. Hyper IDE works perfectly on your phone, tablet, computer, or any other device you might have access to with a browser.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg"
---

# Hyper IDE, a web based IDE

This is your _"goto component"_ when you want to create your own modules using Magic. It's a fully
fledged web based IDE or Integrated Development Environment, allowing you to edit your code,
create new modules, and everything you're used to from a traditional IDE. Below is a screenshot of
Hyper IDE.

![Editing a file in Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg)

Hyper IDE also provides integrated autocomplete if your editor has focus and you click CTRL+SPACE
in Windows or FN+CONTROL+SPACE on your Mac. This allows you to very rapidly create Hyperlambda code,
while having Hyper IDE ensure your code is using existing slots. Click the _"Shortkeys"_ button to see
a list of all keyboard shortcuts Hyper IDE provides. Notice, these keyboard shortcuts are only available
when your code editor has focus. You can also create files and folders, and upload files to your server
through the action buttons drop down menu. Below is a screenshot of Hyper IDE in dark mode while toggling
the action buttons drop down menu.

![Hyper IDE action menu](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

If you don't like dark mode, and/or are sitting outside in the sun while coding, feel free to toggle
the mode and switch to light mode, which will resemble the following.

![Hyper IDE light mode](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-light.jpg)

## Crudifier

Hyper IDE has one unique feature your traditional IDE probably does not have, which is that
it _automatically creates code_ for you. If you click the _"Crudifier"_ action button, Hyper IDE
allows you to select an existing database, click a button, and have Magic automatically create
HTTP CRUD endpoints wrapping every table in your database. Below is a screenshot of this process.

![Hyper IDE crudify](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-crudify.jpg)

This feature can at least in theory save you from months of manual development, and allows you to provide
authorisation requirements, publish socket messages upon invocations, log invocations, apply caching for
your endpoints, etc.

### Create your Angular code in seconds

If you click the crudify action button, you can also create an Angular frontend 100% automatically.
Typically this implies Hyper IDE will produce tens of thousands of lines of code for you automatically,
and provide you with a ZIP file, and/or put your Angular code on your server somewhere. Below is a
screenshot of this process.

![Automatically generate an Angular frontend with Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/generate-frontend.jpg)

### Create HTTP endpoints with SQL

Yup, you heard us correct. With Hyper IDE you can create HTTP web API endpoints entirely using nothing
but SQL. The process implies providing some SQL statement to Hyper IDE's crudifier, choose authorisation
requirements, URL, and other dynamic settings, and have Magic automatically generate an HTTP endpoint
wrapping your SQL. Below is a screenshot of the process.

![Create HTTP endpoints using SQL](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/generate-sql.jpg)

The integrated SQL editor also provides you with autocomplete on your tables and columns the same
way the code editor in Hyper IDE itself does. To access autocomplete click CTRL+SPACE or FN+CONTROL+SPACE
on your Mac. The process also allows you to dynamically parametrise your SQL with HTTP query parameters, and/or
JSON payloads supplied by the client.

## Macros

In addition to the above crudifier feature, Hyper IDE also supports _"macros"_. A macro is an automated
process that somehow creates code, and/or modifies your existing code, 100% automatically. There exists
many macros in Hyper IDE solving everything from automatically documenting your module, to creating file
upload endpoints for you. To run a macro, first select which module you want to run it for, then click
the macro action button, and parametrise your macro. Below is a screenshot of the process of creating
a file upload HTTP endpoint using the integrated macro system.

![Hyper IDE create upload endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/execute-macro.jpg)

After executing the above macro, your module will have an _"upload file"_ HTTP endpoint, automatically
taking care of deleting old files, and/or creating its data folder for you, allowing your client/frontend
code to invoke this endpoint using `multipart/form-data` HTTP requests to automatically upload files to
your server.

## Use your IDE from your tablet, and/or phone

Yup, Hyper IDE is 100% responsive, and although we don't recommend it, it *is* possible to use Hyper IDE
from your phone, assuming your phone has a modern browser. Maybe your phone isn't the best device to create
software from, but actually being able to use your IDE from a tablet, and/or your phone for emergencies is
something we take great pride in delivering.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
