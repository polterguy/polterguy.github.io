
# Magic Lambda MIME

Magic Lambda MIME gives you the ability to parse and create MIME messages from Hyperlambda.
The project contains the following slots.

* __[mime.parse]__ - Parses a MIME message, and returns it as a lambda object
* __[.mime.parse]__ - Parses a native MimeEntity for you, and returns it as a lambda object (not for usage directly from Hyperlambda code)
* __[mime.create]__ - Creates a MIME message for you, and returns the entire message as text, being the MIME entity
* __[.mime.create]__ - Creates a MIME message for you, and returns it as a native MimeEntity object (not for usage directly from Hyperlambda code)

## Parsing MIME messages

Below is an example of how parsing a MIME message might look like.

```
// Actual message
.msg:"Content-Type: multipart/mixed; boundary=\"=-3O9TzEjuVDwt7d5uGDkV/Q==\"\n\n--=-3O9TzEjuVDwt7d5uGDkV/Q==\nContent-Type: text/plain\nContent-Disposition: attachment; filename=README.md\n\n# Your dynamic files folder\n\nSome README.md file\n\n--=-3O9TzEjuVDwt7d5uGDkV/Q==\nContent-Type: text/plain\n\nBar\n--=-3O9TzEjuVDwt7d5uGDkV/Q==--\n"

// Parsing the above message
mime.parse:x:@.msg
```

After evaluating the above, you'll end up with something resembling the following.

```
mime.parse:multipart/mixed
   entity:text/plain
      headers
         Content-Disposition:attachment; filename=README.md
      content:"# Your dynamic files folder\n\nSome README.md file\n"
   entity:text/plain
      content:Bar
```

Notice how the slot creates a tree structure, perfectly resembling your original MIME message. It will also take care of
MIME headers for you, adding these into a **[headers]** collection, on a per MIME entity basis, depending upon whether or not
your message actually contains headers or not.

The **[.mime.parse]** semantically works identically, except it requires as its input a raw `MimeEntity` object from MimeKit.
The **[.mime.parse]** slot can _only be invoked from C#_, since it starts with a _"."_.

## Creating a mime message

This slot is logically the exact opposite of the **[mime.parse]** slot, and can take (almost) the exact same input as
its sibling produces as output. Below is an example.

```
mime.create:multipart/mixed
   structured:false
   entity:text/plain
      content:this is the body text
   entity:text/plain
      content:this is another body text
```

Which of course wil result in something resembling the following after evaluation.

```
mime.create:"Content-Type: multipart/mixed; boundary=\"=-7+NI+p6PuOyQUzW5ihnXvw==\"\n\n--=-7+NI+p6PuOyQUzW5ihnXvw==\nContent-Type: text/plain\n\nthis is the body text\n--=-7+NI+p6PuOyQUzW5ihnXvw==\nContent-Type: text/plain\n\nthis is another body text\n--=-7+NI+p6PuOyQUzW5ihnXvw==--\n"
```

**Notice** - If you set its **[structured]** argument to boolean `true`, the slot will return the MIME envelope headers
for the outermost MIME entity _"detached"_ from the rest of the message. This is useful when you for some reasons don't want
the headers for the outermost entity to be a part of the actual message, such as for instance when creating `multipart/form-data`
types of messages you need to transmit to some HTTP endpoint. If you do this, the return after executing the slot will
resemble the following.

```
mime.create
   Content-Type:"multipart/mixed; boundary=\"=-EbMBZ3eHrSrMqtB2KHSv+A==\""
   content:"--=-EbMBZ3eHrSrMqtB2KHSv+A==\nContent-Type: text/plain\n\nthis is the body text\n--=-EbMBZ3eHrSrMqtB2KHSv+A==\nContent-Type: text/plain\n\nthis is another body text\n--=-EbMBZ3eHrSrMqtB2KHSv+A==--\n"
```

The **[.mime.create]** slot, will semantically do the exact same thing, but instead of returning a piece of text,
being the MIME message, it will produce a raw `MimeEntity` that it returns to caller. This slot is used internally
when the _"magic.lambda.mail"_ project constructs emails to send over an SMTP connection for instance, and when
the _"magic.lambda.http"_ project transmits `multipart/form-data` types of requests. This slot can _only_ be
invoked from C# since it starts with a period (.) as its name.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.mime](https://github.com/polterguy/magic.lambda.mime), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.mime/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mime&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mime)

## License

This project is the copyright(c) 2020-2021 of Aista, Ltd thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)
