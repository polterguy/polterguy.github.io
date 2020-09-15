
# Magic Lambda Dates

Date manipulation library for Magic. More specifically, it gives you the following slots.

* __[date.now]__ - Returns the now date, equivalent of `DateTime.Now`.
* __[date.format]__ - Returns a string representation of some date, formatted according to the specified **[format]** argument.
* __[time]__ - Creates a time span, useful for adding and subtracting offsets to date objects. Pass in **[days]**, **[hours]**, **[minutes]**, **[seconds]** and **[milliseconds]** to declare how large your offset is. All arguments are optional, but (of course) on argument should be passed in.

**Notice** - Internally in Magic, everything is UTC us Universal timezone, implying if you want to render it in user's
timezone, you'll have to convert it explicitly. All dates and times internally in  Magic, also those stored into any database,
are treated as UTC timezone.

## quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.dates.svg?master)](https://travis-ci.com/polterguy/magic.lambda.dates)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.dates&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.dates)
