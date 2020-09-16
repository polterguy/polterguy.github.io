# Hyperlambda Hello World

The word _"Hyperlambda"_ originates from _"hyper"_ and _"lambda"_, implying _"web functions"_.
In order to understand Hyperlambda's usefulness, it is therefor valuable to use Hyperlambda to create
an HTTP REST endpoint, or a _"web function"_.

To create an HTTP REST endpoint, we will need to create a Hyperlambda file. Use for instance
the _"Files"_ menu item in the Magic Dashboard, and open up the folder called _"modules"_.
Create a new folder inside of this folder, and name your new folder _"tutorials"_.

**Notice** - By default Magic will protect files inside of the modules folder, so you'll
have to explicitly click the _"Safe mode"_ slider to be allowed to create folders here.
See the screenshot below for details.

![Creating a new tutorials folder](https://servergardens.files.wordpress.com/2020/09/create-folder.png)

Then open this folder, and create a new Hyperlambda file and name it _exactly_ as follows.
Its name _is_ important.

```
hello-world.get.hl
```

Then click the file to edit it, and replace its default content with the following Hyperlambda.

```
return
   result:Hello World from Hyperlambda
```

Save the file, and open up the _"Endpoints"_ dashboard link, in for instance a different tab
in your browser. Click the _"Show endpoints"_ slider, and filter for _"hello-world"_ if this
gives you a lot of files. Click the endpoint, at which point you'll see something such
as the following.

![How your Hello World endpoint will look like](https://servergardens.files.wordpress.com/2020/09/invoke-endpoint.png)

The click the _"get"_ button. This will give you the following result.

```json
{
   "result": "Hello World from Hyperlambda"
}
```

## Gory details

Remember the filename we used for our endpoint, which was _"hello-world.get.hl"_. The first
parts of the filename, before the _".get.hl"_ parts becomes it relative URL. Since we placed
the file inside of our _"modules/tutorials/"_ folder, its complete URL becomes
_"magic/modules/tutorials/hello-world"_.

The first parts of its extension, the _"get"_ parts, declares that our file is an HTTP GET
endpoint, which we can invoke using the GET verb.

The last parts, the _".hl"_ parts, simply declares that this is a Hyperlambda file,
making the Hyperlambda parser kick in and transform it to a lambda object, which then
is evaluated, and whatever the file returns, is afterwards transformed to JSON, which
again is returned to the client as its HTTP response object.



