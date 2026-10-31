---
title: "How to use [html2lambda]"
description: "How to use [html2lambda] - The above results in something resembling the following."
generated: true
guide: true
---

The reference page of [`html2lambda`](/reference/slots/core/html2lambda/) has its arguments, constraints and declaration.

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
