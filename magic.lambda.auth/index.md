
# Magic Lambda Auth

Authentication and authorization helpers for [Magic](https://github.com/polterguy/magic). This project allows you to create and consume
JWT tokens, to secure your magic installation. The project contains 3 slots.

* __[auth.ticket.create]__ - Creates a new JWT token, that you can return to your client, any ways you see fit.
* __[auth.ticket.refresh]__ - Refreshes a JWT token. Useful for refreshing a token before it expires, which would require the user to login again.
* __[auth.ticket.verify]__ - Verifies a JWT token, and that the user is logged in, in addition to (optionally) that he belongs to one roles supplied as a comma separated list of roles.

Notice, you will have to modify your `auth:secret` configuration setting, to provide a unique salt for your installation. If you don't do
this, some adversary can easily reproduce your tokens, and impersonate your users. Example of appSettings.config settings you could
apply (don't use the exact same salt, the idea is to provide a _random_ salt, unique for _your_ installation)

```json
{
  "auth": {
    "secret":"some-rubbish-random23545456-characters-goes-here!!!!!"
  }
}
```

The idea is that your `SymmetricSecretKey` is based upon the above configuration setting, implying you should safe keep it the
same way you'd safe keep the pin code to your ATM card.

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.auth.svg?master)](https://travis-ci.com/polterguy/magic.lambda.auth)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.auth&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.auth)
