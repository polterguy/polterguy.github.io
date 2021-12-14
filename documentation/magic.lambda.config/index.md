
# Magic Lambda Config

This project provides configuration settings slots for Magic. The project provides one
single slot, allowing you to retrieve configuration settings from your configuration file as follows.

* __[config.get]__ - Returns a configuration value from your configuration file with the specified key
* __[config.section]__ - Returns the specified configuration section from your configuration file with the specified key

You can supply a _"path"_ such as _"foo:bar"_, which will traverse into your _"foo"_ config setting, find its _"bar"_ key,
and return the value of your _"bar"_ key. Below is an example of usage.

```
config.get:"foo:bar"
```

Assuming your configuration file looks like the following.

```json
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

**Notice** - As of this writing, I am still trying to figure out how to return values as the correct types, and
also how to have the **[config.section]** return a hierarchy of the _entire_ section. In a future version, I might
figure this out, at which point the APIs for these methods will slightly change. They are currently both to be
considered as BETA versions.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.config](https://github.com/polterguy/magic.lambda.config), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

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

## License

This project is the copyright(c) 2020-2021 of Aista, Ltd thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)
