
# Magic Lambda Dates

Date manipulation slots for Magic. More specifically, this project contains the following slots.

* __[date.now]__ - Returns the now date, equivalent of `DateTime.Now`.
* __[date.min]__ - Returns the minimum date value, equivalent of `DateTime.MinValue`.
* __[date.format]__ - Returns a string representation of some date, formatted according to the specified **[format]** argument.
* __[time]__ - Creates a time span, useful for adding and subtracting offsets to date objects. Pass in **[days]**, **[hours]**, **[minutes]**, **[seconds]** or **[milliseconds]** to declare how large your offset is. All arguments are optional, but (of course) at least one argument should be passed in.

**Notice** - Internally in Magic, everything is UTC Universal timezone, implying if you want to render it in user's
timezone, you'll have to convert it explicitly in your client/frontend. All dates and times internally in  Magic,
also those stored into any database, are treated as UTC timezone. All dates transmitted _to_ the backend, is also
assumed to be UTC. This is to make things simple in regards to interacting with database systems, that may or may not
add support for timezone offsets.

Below is an example of taking the current date and time, and adding two days and one second to it, for then to
format the result as a string.

```
math.add
   date.now
   time
      days:2
      second:1
date.format:x:-
   format:"yyyy-MM-dd HH:mm:ss"
```

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.dates](https://github.com/polterguy/magic.lambda.dates), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

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

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.
