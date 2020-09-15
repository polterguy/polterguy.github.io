
# Magic Lambda Config

This project provides configuration settings slots for Magic. The project provides one
single slot, allowing you to retrieve configuration settings from your configuration file as follows.

* __[config]__ - Returns the configuration value from your configuration file with the specified key.

You can supply a _"path"_ such as _"foo:bar"_, which will traverse into your _"foo"_ config setting, find its _"bar"_ key,
and return the value of your _"bar"_ key. Below is an example of usage.

```
config:"foo:bar"
```

Assuming your configuration file looks like the following.

```json
{
   "foo": {
      "bar": 42
   }
}
```

... afterwards the value of your __[config]__ node will be the following.

```
foo:int:42
```

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.config.svg?master)](https://travis-ci.com/polterguy/magic.lambda.config)
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
