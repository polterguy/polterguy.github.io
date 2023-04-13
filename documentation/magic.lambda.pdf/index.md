
# magic.lambda.pdf - PDF support for Magic and Hyperlambda

This project provides PDF slots for Magic. The project provides the following
slots, allowing you to convert a PDF file, stream or raw bytes to its text representation.

* __[pdf2text]__ - Converts the specified PDF file or stream to text

## How to use [pdf2text]

This slot allows you to retrieve only the text parts of a PDF document.

```
pdf2text:/foo/bar.pdf
```

Notice, the slot can also accept a stream, such as for instance supplied as an uploaded
document, and react directly on the stream, avoid having to save the streamto a file first.
It can also accept a string as its input, at which point it assumes the string is the
relative path to a file. Finally, the slot can accept raw bytes, which it then assumes
is the raw content from a PDF document.

## Project website for magic.lambda.pdf

The source code for this repository can be found at [github.com/polterguy/magic.lambda.pdf](https://github.com/polterguy/magic.lambda.pdf), and you can provide feedback, provide bug reports, etc at the same place.

- ![Build status](https://github.com/polterguy/magic.lambda.pdf/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.pdf&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.pdf)
