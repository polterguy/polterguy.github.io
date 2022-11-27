
# Parsing XML from Hyperlambda

This project provides XML helper slots for Hyperlambda. More specifically, it provides the following slots.

* __[xml2lambda]__ - Creates a lambda object out of an XML input string.
* __[lambda2xml]__ - Creates an XML string from a lambda object.

## Usage

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

To convert the above lambda object back to its original XML content, you can use something such as follows.

```
lambda2xml:x:@xml2lambda/*
```

Attributes starts out with the `@` character, children nodes does not - While text content inside of elements will
be named `#text`. This implies you'll need to use escaped expression iterators when traversing the resulting node
lambda object. For instance, to retrieve the above `PRICE` element's inner text, you could use something such as the
following.

```
get-value:x:@xml2lambda/**/PRICE/*/\#text
```

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.xml](https://github.com/polterguy/magic.lambda.xml), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.xml/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.xml&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.xml)
