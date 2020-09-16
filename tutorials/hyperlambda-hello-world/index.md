# Hyperlambda Hello World

The word _"Hyperlambda"_ originates from _"hyper"_ and _"lambda"_, implying _"web functions"_.
In order to understand Hyperlambda's usefulness, it is therefor valuable to use Hyperlambda to create
an HTTP REST endpoint.

To create an HTTP REST endpoint, we will need to create a Hyperlambda file. Use for instance
the _"Files"_ menu item in the Magic Dashboard, and open up the folder called _"modules"_.
Create a new folder inside of this folder, and name your new folder _"tutorials"_. Notice,
by default Magic will protect files inside of the modules folder, so you'll have to
explicitly click the _"Safe mode"_ slider to be allowed to create folders here. See
the screenshot below for details.

![Creating a new tutorials folder](https://servergardens.files.wordpress.com/2020/09/create-folder.png)

Then open this folder, and create a new Hyperlambda file and name it _exactly_ as follows.

```
hello-world.get.hl
```

Then click the file to edit it, and replace its default content with the following Hyperlambda.

```
.arguments
   name:string
strings.concat
   .:"Hello "
   get-value:x:@.arguments/*/name
unwrap:x:+/*
return
   result:x:@strings.concat
```

Save the file, and open up the _"Endpoints"_ dashboard link, in for instance a different tab
in your browser. Click the _"Show endpoints"_ slider, and filter for _"hello-world"_ if this
gives you a lot of results. Click the endpoint, at which point you'll see something such
as the following.

![How your Hello World endpoint will look like](https://servergardens.files.wordpress.com/2020/09/invoke-endpoint.png)

Type in the following into the _"Query parameters"_ input textbox.

```
name=Your Name
```

The click the _"get"_ button.
