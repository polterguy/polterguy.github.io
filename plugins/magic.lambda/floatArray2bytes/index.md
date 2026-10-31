---
title: "How to use [floatArray2bytes]"
description: "How to use [floatArray2bytes] - This slot serializes a sequence of float values into raw bytes, which is useful when you need to feed vectors, such as embeddings, into binary APIs."
guide: true
slots: ["floatArray2bytes"]
---

The reference page of [`floatArray2bytes`](/reference/slots/core/floatArray2bytes/) has its arguments, constraints and declaration.

This slot serializes a sequence of float values into raw bytes, which is useful when you need to feed vectors, such as
embeddings, into binary APIs. Its value is an expression selecting the nodes containing the float values, each of which
must be convertible to a float. After invocation, the value of the node is a `byte[]` containing 4 bytes for each float
value.
