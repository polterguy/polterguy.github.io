
# Magic Lambda Validators

This project contains input validators for Magic. More specifically it contains the following slots.

* __[validators.date]__ - Verifies that some date input is a date, and optionally between __[min]__ and __[max]__ value
* __[validators.email]__ - Verifies that some input is a legal email address
* __[validators.enum]__ - Verifies that some input is one of a set of predefined legal values, found as values of children
* __[validators.integer]__ - Verifies that some integer input (long, int, etc) is between some specified __[min]__ and __[max]__ range
* __[validators.mandatory]__ - Verifies that some input valus is given (_at all_)
* __[validators.regex]__ - Verifies that some input is matching some given __[regex]__ pattern
* __[validators.string]__ - Verifies that some string input is between __[min]__ and __[max]__ in length
* __[validators.url]__ - Verifies that some string input is a legal URL, either HTTP or HTTPS type of scheme

All of the above slots takes an expression, or values, as its main input, and will throw exceptions if their input expression's
value(s), or its value, does not follow the rules specified by the validator. This makes them perfect fits for _"intercepting"_ the
input specified to an HTTP REST endpoint, to verify the input data conforms to some sort of predefined validator.

## Usage

```
.foo
   number:int:11

validators.integer:x:@.foo/*/number
   min:int:5
   max:int:10
```

Most validators requires some sort of argument(s), such as you can see above in the integer validator - However, some of
these validators are without arguments, such as the email validator, that simply verifies the input is a valid email address.
To use the **[validators.regex]** validator, you should probably [learn regular expression](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285).
However, this is beyond the scope of this article.

**Notice** - No attempt to invoke the type validator logic will be done unless the value is a _non null_ value. If you want
to enforce such logic, you'll have to combine the specific type validators with the **[validators.mandatory]** validator,
which enforces that a value must be specified and be non null.

## Internals

You can use one invocation to any of the validators to validate multiple nodes, such as the following illustrates.

```
.arguments
   .
      no:5
   .
      no:10
   .
      // Throws
      .no:11
validators.integer:x:@.arguments/*/*/no
   min:5
   max:10
```

First the above expression will be evaluated, then *every* resulting value will be validated, and if *any* of them are
not validated according to the validtor's arguments - Which for the above example is number between 5 and 10 - The
validater will throw an exception, providing the invalid value, and the name of the last iterator (effectively being the argument name)
to the caller. This allows you to use *one single validator* to validate multiple arguments, such as the above illustrates.
This might be useful if you for instance have an endpoint accepting multiple address fields, and zip code is a mandatory
argument, and it needs to be an integer.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.validators](https://github.com/polterguy/magic.lambda.validators), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.validators&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.validators)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)
