---
title: "How to use [html2pdf]"
description: "How to use [html2pdf] - This slot converts the HTML markup given as its value into a PDF document, and returns the PDF as raw bytes in its value."
generated: true
guide: true
---

The reference page of [`html2pdf`](/reference/slots/core/html2pdf/) has its arguments, constraints and declaration.

This slot converts the HTML markup given as its value into a PDF document, and returns the PDF as raw bytes in
its value. The value can be a constant or an expression. Any images, stylesheets and fonts the HTML references
are loaded through Hyperlambda's **[io.file.load.binary]** and **[http.get]** slots, instead of directly by the
PDF library.

This slot converts HTML into a PDF document, and sets the value of its node to the bytes of the PDF. Images and stylesheets the HTML refers to are loaded through the file and HTTP slots, and so obey the whitelist. Below is an example, saving the PDF to disc.

```
html2pdf:"<h1>Hello world</h1><p>This is a PDF document.</p>"
io.file.save.binary:/misc/hello.pdf
   .:x:@html2pdf
```
