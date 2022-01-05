
# Parsing CSV files from Hyperlambda

This project provides CSV helper slots for Magic. More specifically, it provides the following slots.

* __[lambda2csv]__ - Creates a CSV string from a lambda object
* __[csv2lambda]__ - Creates a lambda object from a CSV string

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
add:x:+/*/types
   get-nodes:x:@lambda2csv/*
csv2lambda:x:@lambda2csv
   types
```

Notice, the **[lambda2csv]** slot will return type information, and the **[csv2lambda]** slot can optionally be
given type information in its **[types]** argument, allowing you to convert correctly back to the correct type(s)
as you convert a CSV string to its lambda objects. The **[lambda2csv]** slot will also create headers for your
object, and the **[csv2lambda]** slot will use the first line to retrieve these headers, to rebuild the lambda
object correctly.

This allows you to roundtrip from a lambda object, to CSV format, and back to lambda again, without loosing
type information or names of your nodes. This is necessary since CSV doesn't preserve types in any ways. By
default the **[lambda2csv]** will also treat null values correctly, by adding these into the CSV file as _"[NULL]"_.
This allows you to preserve null values, which isn't really possible with CSV normally - However, for some edge
cases you might want to use  _different_ null value, at which point you can supply this is **[null-value]** argument
to both slots. If you supply a **[null-value]** argument, but set its value to _null_ - Null values will be ignored,
and no null values will be persisted in any direction.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.csv](https://github.com/polterguy/magic.lambda.csv), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.csv/actions/workflows/build.yaml/badge.svg)
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
