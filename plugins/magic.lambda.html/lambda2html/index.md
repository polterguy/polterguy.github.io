---
title: "How to use [lambda2html]"
description: "How to use [lambda2html] - This is the reverse of [html2lambda] and returns HTML resulting from the specified lambda object."
generated: true
guide: true
---

This is the guide to [`lambda2html`](/reference/slots/core/lambda2html/), whose reference page has its arguments, constraints and declaration.

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
