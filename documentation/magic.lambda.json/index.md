
# Magic Lambda Json

[![Build status](https://travis-ci.com/polterguy/magic.lambda.json.svg?master)](https://travis-ci.com/polterguy/magic.lambda.json)

This project provides JSON helper slots for Magic. More specifically, it provides the following slots.

* __[json2lambda]__ - Creates a lambda object out of a JSON input string.
* __[lambda2json]__ - Creates JSON out of a lambda object.

## Usage

```
.json:@"{""property"": ""value""}"
json2lambda:x:-
lambda2json:x:-/*
```

The **[lambda2json]** slot can optionally take a **[format]** argument, with a boolean _"true"_ value, which implies the
resulting JSON will be indeneted and nicely formated, making it more readable.

**Notice** - Although all JSON can be transformed into lambda, the opposite is not necessarily true. This is because
lambda allows for having multiple nodes with the same name for instance, which would result in a JSON object with
multiple properties having the same key. Hence, have this in mind as you persist your lambda objects into JSON.

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.json.svg?master)](https://travis-ci.com/polterguy/magic.lambda.json)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.json&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.json)
