
# Magic Lambda CSV

[![Build status](https://travis-ci.com/polterguy/magic.lambda.csv.svg?master)](https://travis-ci.com/polterguy/magic.lambda.csv)

This project provides CSV helper slots for Magic. More specifically, it provides the following slots.

* __[lambda2csv]__ - Creates CSV string from a lambda object.
* __[csv2lambda]__ - Creates a lambda object from a CSV string.

## Usage

```
.data
   .
      name:Thomas Hansen
      age:int:47
   .
      name:John Doe
      age:int:67
lambda2csv:x:-/*
add:x:+
   get-nodes:x:@lambda2csv/*
csv2lambda:x:@lambda2csv
```

Notice, the **[lambda2csv]** slot will return type information, and the **[csv2lambda]** slot can optionally be
given type information, allowing you to convert correctly back to the correct type(s) as you convert a CSV
string to its lambda objects. The **[lambda2csv]** slot will also create headers for your object.

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.csv.svg?master)](https://travis-ci.com/polterguy/magic.lambda.csv)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.csv&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.csv)
