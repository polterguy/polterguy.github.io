
# magic.lambda.html - HTML and Markdown support in Hyperlambda

This project provides HTML helper slots for Magic. More specifically, it provides the following slots.

* __[html2lambda]__ - Creates a lambda object out of an HTML input string.
* __[lambda2html]__ - Creates an HTML string out of the specified lambda object.
* __[markdown2html]__ - Creates HTML out of the specified Markdown input string.

## How to use [html2lambda]

```
.html:@"<html>
  <head>
    <title>Howdy</title>
  </head>
  <body>
    <p class=""foo"">Howdy <strong>world</strong> - This is cool!</p>
  </body>
</html>"

html2lambda:x:-
```

The above results in something resembling the following.

```
html2lambda
   html
      head
         title
            #text:Howdy
      body
         p
            @class:foo
            #text:"Howdy "
            strong
               #text:world
            #text:" - This is cool!"
```

Attributes starts out with the `@` character, children nodes does not - While text content inside of elements will
have the name of `#text`. This implies you'll need to use escaped expression iterators when traversing the resulting node
lambda object. For instance, to retrieve the above `title` element's inner text, you could use something such as the
following.

```
get-value:x:-/**/title/*\#text
```

## How to use [lambda2html]

This is the reverse of **[html2lambda]** and returns HTML resulting from the specified lambda object. Below
is example usage.

```
.html:@"<html>
  <head>
    <title>Howdy</title>
  </head>
  <body>
    <p class=""foo"">Howdy <strong>world</strong> - This is cool!</p>
  </body>
</html>"
html2lambda:x:-
lambda2html:x:-/*
```

The above will result in the following HTML, formatted for brevity.

```html
<html>
  <head>
    <title>Howdy</title>
  </head>
  <body>
    <p class="foo">Howdy <strong>world</strong> - This is cool!</p>
  </body>
</html>
```

## How to use [markdown2html]

This library can also handle Markdown, since Markdown is arguably just another representation of HTML.
The **[markdown2html]** slot converts the specified Markdown content to HTML. Basic usage is as follows.

```
.yaml:@"
Howdy world

* Foo
* Bar
"
markdown2html:x:@.yaml
```

The above will produce the following result.

```html
markdown2html:@"<p>Howdy world</p>
<ul>
<li>Foo</li>
<li>Bar</li>
</ul>
```

### Front matter and [markdown2html]

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

## Project website for magic.lambda.html

The source code for this repository can be found at [github.com/polterguy/magic.lambda.html](https://github.com/polterguy/magic.lambda.html), and you can provide feedback, provide bug reports, etc at the same place.

- ![Build status](https://github.com/polterguy/magic.lambda.html/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
