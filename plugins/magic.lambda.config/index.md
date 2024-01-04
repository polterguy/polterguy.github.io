---
title: magic.lambda.config
---

This project provides configuration settings slots for Magic. The project provides the following
slots, allowing you to retrieve configuration settings from your _"appsettings.json"_ configuration file,
in addition to saving and loading your configuration file.

* __[config.get]__ - Returns a configuration value from your configuration file with the specified key
* __[config.section]__ - Returns the specified configuration section from your configuration file with the specified key
* __[config.load]__ - Loads your _"appsettings.json"_ file and returns as a string
* __[config.save]__ - Saves your _"appsettings.json"_ file, sanity checking it's valid JSON before persisting your file

## How to use [config.get]

This slot allows you to retrieve configuration settings. To retrieve settings you can supply a
_"path"_ such as _"foo:bar"_ to for instance an invocation to **[config.get]**. This will traverse into
your _"foo"_ config setting, find its _"bar"_ key, and return the value of your _"bar"_ key. Below is
an example of usage.

```
config.get:"foo:bar"
```

Assuming your configuration file looks like the following.

```
{
   "foo": {
      "bar": 42
   }
}
```

... afterwards the value of your __[config.get]__ node will be the following.

```
config.get:42
```

**Notice** - Due to implementation details of .Net and its `IConfiguration` specifically, values
returned will _always_ be strings, and you'll have to manually convert these to other types, using for
instance the **[convert]** slot from magic.lambda. This _might_ change in a future release though.
You can also provide a default value that will be returned if no configuration value is found, such
as the following illustrates.

```
.foo:foo
config.get:"magic:foo:non-existing-key"
   get-value:x:@.foo
```

Since the above _"non-existing-key"_ doesn't exist in your configuration file, the above Hyperlambda will
return the value _"foo"_ being the result of the invocation to the **[get-value]** slot. This allows you
to create default values your code resorts to if the specified configuration setting doesn't exist.

## Project website for magic.lambda.config

The source code for this repository can be found at [github.com/polterguy/magic.lambda.config](https://github.com/polterguy/magic.lambda.config), and you can provide feedback, provide bug reports, etc at the same place.

- ![Build status](https://github.com/polterguy/magic.lambda.config/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.config&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.config)

## Copyright and maintenance

The projects is copyright of Aista, Ltd 2021 - 2023, and professionally maintained by [AINIRO your friendly ChatGPT website chatbot vendor](https://ainiro.io).
