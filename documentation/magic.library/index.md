
# Wiring all parts of Magic together automagically

This project helps you to wire up everything related to Magic. Normally you'd use it simply like the following from
your startup class in your .Net 6 Web API project.

```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using magic.library;

namespace magic.backend
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        IConfiguration Configuration { get; }

        public void ConfigureServices(IServiceCollection services)
        {
            // Initializing Magic.
            services.AddMagic(Configuration);
        }

        public void Configure(IApplicationBuilder app)
        {
            // Initializing Magic.
            app.UseMagic(Configuration);
        }
    }
}
```

However, you can also take more control over how things are actually wired up, by instead of using the
_"do all methods"_ called `AddMagic` and `UseMagic`, invoke some of the specialized initialization methods,
you can find below.

* `IServiceCollection.AddCaching`
* `IServiceCollection.AddMagicHttp`
* `IServiceCollection.AddMagicLogging`
* `IServiceCollection.AddMagicSignals`
* `IServiceCollection.AddMagicEndpoints`
* `IServiceCollection.AddMagicFileServices`
* `IServiceCollection.AddMagicAuthorization`
* `IServiceCollection.AddMagicScheduler`
* `IServiceCollection.AddMagicMail`
* `IServiceCollection.AddLambda`

The above methods is basically what the `AddMagic` method actually does, and they're extension methods of
`IServiceCollection`, that can be found in the `magic.library` namespace. Similar alternatives to `UseMagic` can
be found below.

* `IApplicationBuilder.UseMagicExceptions`
* `IApplicationBuilder.UseMagicStartupFiles`
* `IApplicationBuilder.UseScheduler`

If you use these methods instead of the _"do all methods"_, probably a large portion of your motivation would
be to _replace_ one of these methods with your own implementation, to exchange the default wiring up, by (for instance)
using a _"virtual database based file system"_ by creating your own service implementation of for instance `IFileService`
from _"magic.lambda.io"_, or use a different logging provider than the default, etc. If you wish
to do this, you'd probably benefit from looking at what the default implementation of your method does, to understand the
requirements from your method.

Doing this is very powerful, and allows you to change the way the system behaves by default - But is also definitely
considered an _"advanced exercise"_.

## Exceptions handlers

As of version 9.7.1 Magic support providing custom exceptions handler on a per folder level, that overrides the
default exception logic with a custom exception handler expected to be named _"exceptions.hl"_ and found within
the folder hierarchy where an HTTP invocation is resolved. For instance, if you wish to create your own exception
handler for a specific module called _"foo"_, you can create an exception handler file
called _"/files/modules/foo/exceptions.hl"_, and expect this file to be invoked every time an unhandled exception
occurs.

This allows you to transform an unhandled exception, such as for instance localising it or customising it
in any ways. Your custom exception handler will be invoked with the following arguments.

* __[message]__ - The exception error message
* __[path]__ - The URL that triggered the exception
* __[field]__ - If the exception that was thrown declared a field, this argument will contain the same value
* __[status]__ - If the exception that was thrown declared a status code, this argument will contain the same value
* __[public]__ - If the exception that was thrown declared a public exception, this argument will contain the same value

You can return a _"transformer"_ exception from your exception handler, returning the following arguments.

* __[message]__ - Message to return as JSON to client
* __[field]__ - Field to return as JSON to client
* __[status]__ - Status code to decorate your HTTP response with

The default exception handler can be found in _"/files/exceptions.hl"_, which will be invoked if no custom exception
handler is declared further down in your folder hierarchy.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.library](https://github.com/polterguy/magic.library), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.library/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.library&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.library)
