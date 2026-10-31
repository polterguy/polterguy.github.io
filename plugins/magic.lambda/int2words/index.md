---
title: "How to use [int2words]"
description: "How to use [int2words] - This slot takes a signed 64 bit integer and converts it to its word representation, such as for instance 1200050 becoming \"one million two hundred thousand and fifty\"."
generated: true
guide: true
---

The reference page of [`int2words`](/reference/slots/core/int2words/) has its arguments, constraints and declaration.

This slot takes a signed 64 bit integer and converts it to its word representation, such as for instance 1200050 becoming _"one million two hundred thousand and fifty"_. Below is an example of using the slot.

```
int2words:1200050
```

The slot works with signed 64 bit integer values, implying it can work with numbers in the trillions if required. The result of executing the above should resemble the following.

```
int2words:one million two hundred thousand and fifty
```

The slot is particularly useful for RAG and VSS databases, where embedding models such as _"text-embedding-ada-002"_ tends to do a much better job at matching numbers if you spell these out instead of simply providing them as numbers.
