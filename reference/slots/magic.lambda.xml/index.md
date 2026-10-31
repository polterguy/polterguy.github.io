---
title: magic.lambda.xml slot reference
description: Every slot in magic.lambda.xml with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.xml](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.xml). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.xml](/plugins/magic.lambda.xml/)._

## [lambda2xml]

Converts a lambda object to an XML fragment or document.

* **Value** (`xml-tree`), required: Expression selecting a SINGLE lambda root to transform (XML has exactly one document root)
* **Returns**: Resolves to the generated XML string

Guide: [How to use [lambda2xml]](/plugins/magic.lambda.xml/#how-to-use-lambda2xml)

## [xml2lambda]

Transforms XML into a lambda hierarchy.

* **Value** (`xml`), required: XML text to transform
* **Returns**: Resolves to the parsed XML hierarchy as child nodes; attributes are emitted as @name child nodes, text as #text child nodes, and comments/whitespace-only text nodes are omitted

Guide: [How to use [xml2lambda]](/plugins/magic.lambda.xml/#how-to-use-xml2lambda)

