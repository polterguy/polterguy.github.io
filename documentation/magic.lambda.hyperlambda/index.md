
# Parsing Hyperlambda using Magic

This is the Hyperlambda parser and generator in Magic. More specifically, this project provides you
with the following two slots.

* __[hyper2lambda]__ - Transforms a piece of Hyperlambda (text) to a lambda hierarchy
* __[lambda2hyper]__ - Transforms a lambda hierarchy to Hyperlambda (text)

Using these slots, you can both easily create, serialize, and parse Hyperlambda to lambda, and vice versa.
Below is an example of parsing a piece of text as Hyperlambda, for then to dynamically execute it afterwards.

```
.hl:@"log.info:""This was logged from a piece of text"""

hyper2lambda:x:-

eval:x:-
```

You can also reverse the process, such as the following illustrates.

```
.hl
   log.info:This is some example logging invocation

lambda2hyper:x:-/*
```

The above two slots, allows you to dynamically generate plain text from a lambda structure, and vice versa,
allowing you to for instance persist execution objects and structured data into files, your database, or for
that matter transmit it over the network to another machine. Below is an example of dynamically
loading a Hyperlambda file from disc, for then to execute it. Notice, in order to have the following
snippet work, you'll need an actual file called _"foo.hl"_ inside of your backend's _"files/"_ folder.

```
io.file.load:/foo.hl

hyper2lambda:x:-

eval:x:-
```

**Notice** - Both of these slots can optionally be given a **[comments]** arguments with a value of `true`,
at which point both **[lambda2hyper]** and **[hyper2lambda]** will preserve comments, and persist these as
**[..]** nodes into your lambda, and reverse the process for the other direction. This allows you to keep the
comments of your Hyperlambda parts as semantic nodes, as you handle your Hyperlambda and node hierarchy.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.hyperlambda](https://github.com/polterguy/magic.lambda.hyperlambda), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.hyperlambda/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.hyperlambda&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.hyperlambda)
