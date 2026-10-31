---
title: "How to use [lambda2xml]"
description: "How to use [lambda2xml] - To convert from a lambda object to an XML object you can use something such as follows."
generated: true
guide: true
---

This is the guide to [`lambda2xml`](/reference/slots/core/lambda2xml/), whose reference page has its arguments, constraints and declaration.

To convert from a lambda object to an XML object you can use something such as follows.

```
.xml
   CATALOG
      PLANT
         COMMON
            #text:Bloodroot
         BOTANICAL
            #text:Sanguinaria canadensis
         ZONE
            #text:4
         LIGHT
            #text:Mostly Shady
         PRICE
            #text:$2.44
         AVAILABILITY
            #text:031599
lambda2xml:x:@.xml/*
```
