
# Magic Lambda HTTP

Provides HTTP REST capabilities for [Magic](https://github.com/polterguy/magic). More specifically it provides 4 slots.

* __[http.get]__ - Returns some resource using the HTTP GET verb towards the specified URL.
* __[http.delete]__ - Deletes some resource using the HTTP DELETE verb.
* __[http.post]__ - Posts some resources to some URL using the HTTP POST verb.
* __[http.put]__ - Puts some resources to some URL using the HTTP PUT verb.

The __[http.put]__ and the __[http.post]__ slots requires you to provide a __[payload]__, which will be pass to the
endpoint as a string. All 4 endpoints can (optionally) take a __[token]__ arguments, which will be transferred as
a `Bearer Authorization` token to the endpoint, in the HTTP Authorization header of your request.

Notice, if you want to have more control over your HTTP request, you can also explicitly add your own
**[header]** collection, which will become the HTTP request's headers, where the header name is the name
of the node, and its value is the value of the node. Below is a simple example of retrieving the document
found at the specified URL, using a simple GET HTTP request, without neither a **[token]** nor **[header]**
collection.

```
http.get:"https://google.com"
```

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.http.svg?master)](https://travis-ci.com/polterguy/magic.lambda.http)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
