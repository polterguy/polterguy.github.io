---
title: "How to use [html2markdown]"
description: "How to use [html2markdown] - .html:@\"<html>   <head>     <title>Howdy</title>   </head>   <body>     <h1>Header here</h1>     <p class=\"\"foo\"\">Howdy <strong>world</strong> - This is cool!</p>   </body> html2markdown:x..."
generated: true
guide: true
---

This is the guide to [`html2markdown`](/reference/slots/core/html2markdown/), whose reference page has its arguments, constraints and declaration.

```
.html:@"<html>
  <head>
    <title>Howdy</title>
  </head>
  <body>
    <h1>Header here</h1>
    <p class=""foo"">Howdy <strong>world</strong> - This is cool!</p>
  </body>
</html>"

html2markdown:x:-
```

The above results in something resembling the following.

```
# Header here

Howdy **world** - This is cool!
```

This slot will do its best to convert the specified HTML to Markdown. The process isn't perfect, since it is
impossible to consistently turn HTML into Markdown, but it is very strong in comparison to other similar libraries
out there.

You can optionally supply a **[url]** argument, which will be used to resolve relative URLs in your HTML.
The process will also return meta information, such as title, description, etc, in addition to all URLs it finds
in the document as a list of URLs in **[urls]**.

You can also optionally supply the following arguments, which all defaults to boolean true.

* **[images]** - If true imports images
* **[code]** - If true imports code
* **[lists]** - If true imports lists

## Front matter and [markdown2html]

The **[markdown2html]** slot can also handle _"front matter"_, which allows you to inject YAML at the front
of your Markdown. Front matter again is just a YAML declaration injected at the front of your Markdown,
separated by `---` to separate your YAML from your Markdown. This allows you to add structured data to
associate with your Markdown content.

```
.yaml:@"---
foo: bar
---
Howdy world

* Foo
* Bar
"
markdown2html:x:@.yaml
```

Internally, the library will invoke **[yaml2lambda]** for any front matter declarations to actually parse
the specified YAML front matter parts, implying for details about how this part works, please refer to
the _"magic.lambda.json"_ project.
