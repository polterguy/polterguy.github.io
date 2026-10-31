---
title: magic.lambda.pdf slot reference
description: Every slot in magic.lambda.pdf with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.pdf](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.pdf). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.pdf](/plugins/magic.lambda.pdf/)._

## [html2pdf]

Converts HTML into a PDF document.

* **Value** (`html`), required: HTML markup to convert
* **Returns**: Resolves to the generated PDF bytes

Guide: [How to use [html2pdf]](/plugins/magic.lambda.pdf/#how-to-use-html2pdf)

## [pdf2text]

Extracts text from a PDF file or stream.

* **Value** (`pdf-file,pdf-content,binary-content`), required: PDF file path, bytes, or stream to extract text from
* **Returns**: Returns extracted text in value or, when preserving pages, one child node per page

| Argument | Type | Required | Description |
|---|---|---|---|
| `[preserve-pages]` | bool | no | Whether to return one child node per page instead of one combined value |

Guide: [How to use [pdf2text]](/plugins/magic.lambda.pdf/#how-to-use-pdf2text)

