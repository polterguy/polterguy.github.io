---
title: "How to use [html2pdf]"
description: "How to use [html2pdf] - This slot converts the HTML markup given as its value into a PDF document, and returns the PDF as raw bytes in its value."
generated: true
guide: true
---

This is the guide to [`html2pdf`](/reference/slots/core/html2pdf/), whose reference page has its arguments, constraints and declaration.

This slot converts the HTML markup given as its value into a PDF document, and returns the PDF as raw bytes in
its value. The value can be a constant or an expression. Any images, stylesheets and fonts the HTML references
are loaded through Hyperlambda's **[io.file.load.binary]** and **[http.get]** slots, instead of directly by the
PDF library.
