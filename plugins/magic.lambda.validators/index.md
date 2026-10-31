---
title: magic.lambda.validators
moved_anchors: {"how-to-use-validatorsdate": "/plugins/magic.lambda.validators/validators.date/", "how-to-use-validatorsdefault": "/plugins/magic.lambda.validators/validators.default/", "how-to-use-validatorsemail": "/plugins/magic.lambda.validators/validators.email/", "how-to-use-validatorsenum": "/plugins/magic.lambda.validators/validators.enum/", "how-to-use-validatorsinteger": "/plugins/magic.lambda.validators/validators.integer/", "how-to-use-validatorsmandatory": "/plugins/magic.lambda.validators/validators.mandatory/", "how-to-use-validatorsrecaptcha": "/plugins/magic.lambda.validators/validators.recaptcha/", "how-to-use-validatorsregex": "/plugins/magic.lambda.validators/validators.regex/", "how-to-use-validatorsstring": "/plugins/magic.lambda.validators/validators.string/", "how-to-use-validatorsurl": "/plugins/magic.lambda.validators/validators.url/"}
---

This project contains argument validators for Hyperlambda. More specifically it contains the following slots.

* __[\[validators.date\]](/plugins/magic.lambda.validators/validators.date/)__ - Verifies that some date input is a date, and optionally between __[min]__ and __[max]__ value
* __[\[validators.email\]](/plugins/magic.lambda.validators/validators.email/)__ - Verifies that some input is a legal email address
* __[\[validators.enum\]](/plugins/magic.lambda.validators/validators.enum/)__ - Verifies that some input is one of a set of predefined legal values, found as values of children
* __[\[validators.integer\]](/plugins/magic.lambda.validators/validators.integer/)__ - Verifies that some integer input (long, int, etc) is between some specified __[min]__ and __[max]__ range
* __[\[validators.mandatory\]](/plugins/magic.lambda.validators/validators.mandatory/)__ - Verifies that some input valus is given (_at all_)
* __[\[validators.regex\]](/plugins/magic.lambda.validators/validators.regex/)__ - Verifies that some input is matching some given __[regex]__ pattern
* __[\[validators.string\]](/plugins/magic.lambda.validators/validators.string/)__ - Verifies that some string input is between __[min]__ and __[max]__ in length
* __[\[validators.url\]](/plugins/magic.lambda.validators/validators.url/)__ - Verifies that some string input is a legal URL, either HTTP or HTTPS type of scheme
* __[\[validators.recaptcha\]](/plugins/magic.lambda.validators/validators.recaptcha/)__ - reCAPTCHA validator, to avoid bots from invoking your APIs
* __[\[validators.default\]](/plugins/magic.lambda.validators/validators.default/)__ - Default validator, adding default argument if not specified

All of the above slots takes an expression, or values, as its main input, and will throw exceptions if their input expression's
value(s), or its value, does not follow the rules specified by the validator. Some of the above slots takes additional arguments.
This makes them perfect fits for _"intercepting"_ the input specified to an HTTP REST endpoint, to verify the input data conforms
to some sort of predefined validation scheme.


## Commonalities between validators

```
.foo
   email:foo@bar.com
validators.email:x:@.foo/*/email
```

Most Hyperlambda validators requires some sort of argument(s) - However, some of
these validators does not require arguments, such as the email validator, that simply verifies the input is a valid email address.
To use the **[validators.regex]** validator, you should probably [learn regular expression](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285). However, this is beyond the scope of this article.

**Notice** - No attempt to invoke the type validator logic will be done unless the value is a _non null_ value. If you want
to enforce such logic, you'll have to combine the specific type validators with the **[validators.mandatory]** validator,
that enforces that a value must be specified and not have a null value.


## Validator internals

You can use one invocation to any of the validators to validate multiple nodes, such as the following illustrates.

```
.arguments
   .
      no:5
   .
      no:10
   .
      // Throws if you remove the "."
      .no:11

validators.integer:x:@.arguments/*/*/no
   min:5
   max:10
```

First the above expression will be evaluated, then *every* resulting value will be validated, and if *any* of them are
not validated according to the validator's arguments - Which for the above example is number between 5 and 10 - The
validater will throw an exception, providing the invalid value, and the name of the last iterator (effectively being the argument name)
to the caller. This allows you to use *one single validator* to validate multiple arguments, such as the above illustrates.
This might be useful if you for instance have an endpoint accepting multiple address fields, and zip code is a mandatory
argument, and it needs to be an integer with a **[max]** and **[min]** value.
