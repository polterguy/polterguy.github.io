---
title: "[html2lambda]"
description: "html2lambda is a core slot of Magic Cloud. Transforms HTML into a lambda hierarchy."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/html2lambda/slot.json"
---

`html2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms HTML into a lambda hierarchy.

* **Value** (`html`), required: HTML markup to transform
* **Returns**: Resolves to the parsed HTML hierarchy as child nodes

### Guide

<!-- guide -->
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
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.html](/plugins/magic.lambda.html/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `html2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "html2lambda",
  "description": "Transforms HTML into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "html",
      "description": "HTML markup to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "html-tree",
      "description": "Resolves to the parsed HTML hierarchy as child nodes"
    }
  }
}
```

</details>

---

[&larr; `html-decode`](/reference/slots/core/html-decode/) | [all core slots](/reference/slots/core/) | [`html2markdown` &rarr;](/reference/slots/core/html2markdown/)

