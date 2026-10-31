---
title: "How to use [xml2lambda]"
description: "How to use [xml2lambda] - .xml:@\"<CATALOG>   <PLANT>     <COMMON>Bloodroot</COMMON>     <BOTANICAL>Sanguinaria canadensis</BOTANICAL>     <ZONE>4</ZONE>     <LIGHT>Mostly Shady</LIGHT>     <PRICE>$2.44</PRICE>     <AV..."
generated: true
guide: true
---

The reference page of [`xml2lambda`](/reference/slots/core/xml2lambda/) has its arguments, constraints and declaration.

```
.xml:@"<CATALOG>
  <PLANT>
    <COMMON>Bloodroot</COMMON>
    <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
    <ZONE>4</ZONE>
    <LIGHT>Mostly Shady</LIGHT>
    <PRICE>$2.44</PRICE>
    <AVAILABILITY>031599</AVAILABILITY>
  </PLANT>
</CATALOG>
"
xml2lambda:x:@.xml
```

The above results in something resembling the following.

```
xml2lambda
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
```

Attributes starts out with the `@` character, children nodes does not - While text content inside of elements will
be named `#text`. This implies you'll need to use escaped expression iterators when traversing the resulting node
lambda object. For instance, to retrieve the above `PRICE` element's inner text, you could use something such as the
following.

```
get-value:x:@xml2lambda/**/PRICE/*/\#text
```
