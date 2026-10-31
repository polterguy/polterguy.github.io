---
title: "[html2markdown]"
description: "html2markdown is a core slot of Magic Cloud. Transforms HTML into Markdown."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/html2markdown/slot.json"
---

`html2markdown` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms HTML into Markdown.

* **Value** (`html`), required: HTML markup to transform
* **Returns**: Resolves to the generated Markdown

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | no | Base URL used when resolving links. |
| `[images]` | bool | no | Whether images should be emitted. Default: `true`. |
| `[code]` | bool | no | Whether code blocks should be emitted. Default: `true`. |
| `[lists]` | bool | no | Whether lists should be emitted. Default: `true`. |

### Guide

<!-- guide -->
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

#### Front matter and [markdown2html]

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
<!-- /guide -->

### JSON declaration

This is the complete declaration of `html2markdown`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "html2markdown",
  "description": "Transforms HTML into Markdown",
  "signature": {
    "input": {
      "kind": "html",
      "description": "HTML markup to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "url": {
        "type": "string",
        "kind": "url",
        "description": "Base URL used when resolving links",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "images": {
        "type": "bool",
        "description": "Whether images should be emitted",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true",
        "role": "Option",
        "projection": "Value"
      },
      "code": {
        "type": "bool",
        "description": "Whether code blocks should be emitted",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true",
        "role": "Option",
        "projection": "Value"
      },
      "lists": {
        "type": "bool",
        "description": "Whether lists should be emitted",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "markdown,text",
      "description": "Resolves to the generated Markdown"
    }
  }
}
```

</details>

---

[&larr; `html2lambda`](/reference/slots/core/html2lambda/) | [all core slots](/reference/slots/core/) | [`html2pdf` &rarr;](/reference/slots/core/html2pdf/)

