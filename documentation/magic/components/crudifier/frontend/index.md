---
title: Create a frontend web app in 1 second
description: After having automatically generated your backend Magic can also create your frontend in 1 second by reading meta information from your backend and automatically generate a frontend wrapping your backend.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crud-frontend.jpg"
---

# The frontend generator component

The frontend generator component allows you to automatically generate a frontend wrapping your previously generated backend.
The idea of the process is that it provides you with a starting place for your own frontend code, allowing
you to modify the result of this operation as you see fit, to accommodate for whatever business requirements
you might have.

![Frontend generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/crud-frontend.jpg)

The frontend generator creates 100% _"perfect"_ Angular code, implying following all Lint standards, and being
very DRY and highly structured. The end result is a responsive CRUD web application, giving you all CRUD operations
towards your database.

![A generated CRUD frontend](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sakila.jpg)

Your generated frontend will support filtering, paging, creating new database records, editing existing
records, deleting records, in addition to localisation/translation and authorisation/authentication. To test
your generated frontend locally, make sure you've got NodeJS and Angular installed, and write the following
into a terminal prompt where your frontend was unzipped.

```bash
npm i
ng serve
```

Depending upon which template you choose you can also override settings for your end result, such as colours, themes,
which modules and components to generate frontend components for, etc. What code is being generated depends upon
your specific template, and Magic allows you to create your own templates too - However, the integrated Angular
template(s) generates high quality code, following all TSLint standards, allowing you to easily understand and
modify it as you see fit.
