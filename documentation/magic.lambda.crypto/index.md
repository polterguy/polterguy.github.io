
# Magic Lambda Crypto

Provides cryptographic services to Magic. More specifically, this project provides the following slots, that
among other things helps you with storing passwords securely in your database, in addition to other services,
such as generating random strings of text, etc.

* __[crypto.hash]__ - Creates a hash of the specified string value/expression's value, using the specified **[algorithm]**, that defaults to SHA256
* __[crypto.password.hash]__ - Creates a cryptographically secure hash from the specified password, expected to be found in its value node
* __[crypto.password.verify]__ - Verifies a **[hash]** argument matches towards the password specified in its value
* __[crypto.random]__ - Creates a cryptographically secured random string for you, with the characters [a-zA-Z], '_' and '-'

The above password slots will use BlowFish algorithm, through BCrypt, while the supported algorithms for the **[crypto.hash]**
are as follows.

* SHA1
* SHA256
* SHA384
* SHA512
* MD5

The **[crypto.random]** can optionally take a **[min]** and **[max]** argument, which defines the min/max length of the
string returned. If not supplied, the default values for these arguments are respectively 10 and 20. This slot is useful
for creating random secrets, and similar types of random strings, where you need cryptographically secured random strings.
An example of generating a cryptographically secure random string of text, between 50 and 100 characters in lenght,
can be found below.

```
crypto.random
   min:50
   max:100
```

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.crypto.svg?master)](https://travis-ci.com/polterguy/magic.lambda.crypto)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.crypto&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.crypto)
