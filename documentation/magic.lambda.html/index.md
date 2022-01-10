
# Parsing HTML from Hyperlambda

This project provides HTML helper slots for Magic. More specifically, it provides the following slots.

* __[html2lambda]__ - Creates a lambda object out of an HTML input string.

## Usage

```
.html:@"<html>
  <head>
    <title>Howdy</title>
  </head>
  <body>
    <p class=""foo""></p>
  </body>
</html>"

html2lambda:x:-
```

The above results in something resembling the following.

```
html2lambda
   html
      head
         title
            #text:Howdy
      body
         p
            @class:foo
```

Attributes starts out with the `@` character, children nodes does not - While text content inside of elements will
start out with `#`. This implies you'll need to use escaped expression iterators when traversing the resulting node
lambda object. For instance, to retrieve the above `p` element's inner text, you could use something such as the
following.

```
get-value:x:-/**/\#text
```

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.html](https://github.com/polterguy/magic.lambda.html), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.html/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.html&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.html)
