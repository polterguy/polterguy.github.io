
# Magic Lambda AD auth

This project gives your Magic installation the capability of authenticating over LDAP and Active Directory.
The basic idea of the project is that it instead of verifying your password using the default
Magic database, it allows you to verify your password by providing your username and password to a slot
that verifies it according to your AD username/password. Below is an example of how to perform
AD authentication.

```
ad-auth.authenticate
   username:foo@acme.com
   password:SomePa$$wordHere
```

If the authentication is successful, the above slot will return boolean true to caller. If the credentials
are incorrect the slot will return false to caller.

**Notice** - Your AD domain controller must be accessible from your Magic app in order for this to work. I have
only tested it with Kestrel, but I suspect it will work on any installation type on your AD controller's
domain somehow. I am not sure if it will work on Linux or OS X though, and I suspect you'll have to deploy your
Magic app to a Windows box somehow to make this work.

## Usage

Magic supports externalised authentication through configuration, so you can easily apply this
without any changes to your existing code by simply changing the default authentication scheme using
the following configuration.

```json
{
  "magic": {
    "auth": {
      "authentication": "ad-auth.authenticate",
      "ldap": "LDAP://foo.acme.somewhere"
```

The important parts above is the `authentication`, that declares which slot to invoke to verify the user's
password, and will exchange the default invocation to **[crypto.password.verify]**, without requiring code changes
of any sort - In addition to that you'll have to provide your LDAP path with the above `ldap` key.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.ad-auth](https://github.com/polterguy/magic.lambda.ad-auth), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.
