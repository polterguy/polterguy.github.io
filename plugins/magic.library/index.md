---
title: magic.library
moved_anchors: {"exceptions-handlers": "/plugins/magic.library/exceptions-handlers/"}
---

This project helps you to wire up everything related to Magic. Normally you'd use it simply like the following from
your startup class in your .Net 8 Web API project.

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

* `IServiceCollection.AddMagicCaching`
* `IServiceCollection.AddMagicHttp`
* `IServiceCollection.AddMagicLogging`
* `IServiceCollection.AddMagicSignals`
* `IServiceCollection.AddMagicExceptions`
* `IServiceCollection.AddMagicEndpoints`
* `IServiceCollection.AddMagicAuthorization`
* `IServiceCollection.AddMagicFileServices`
* `IServiceCollection.AddMagicFileServices`
* `IServiceCollection.AddMagicConfiguration`
* `IServiceCollection.AddMagicScheduler`
* `IServiceCollection.AddMagicMail`
* `IServiceCollection.AddMagicLambda`
* `IServiceCollection.AddMagicSockets`

The above methods is basically what the `AddMagic` method actually does, and they're extension methods of
`IServiceCollection`, that can be found in the `magic.library` namespace. Similar alternatives to `UseMagic` can
be found below.

* `IApplicationBuilder.UseMagicExceptions`
* `IApplicationBuilder.UseMagicStartupFiles`
* `IApplicationBuilder.UseMagicScheduler`
* `IApplicationBuilder.UseMagicCors`

If you use these methods instead of the _"do all methods"_, your motivation would probably
be to _replace_ one of these methods with your own implementation, to exchange the default wiring, by (for instance)
using a _"virtual database based file system"_ by creating your own service implementation of for instance `IFileService`
from _"magic.lambda.io"_, or use a different logging provider than the default, etc. If you wish
to do this, you'd probably benefit from looking at what the default implementation of your method does, to understand the
requirements from your method. Doing this is very powerful, and allows you to change the way the system behaves by default -
But is also definitely considered an _"advanced exercise"_.


## Topics

* [Exceptions handlers](/plugins/magic.library/exceptions-handlers/) - Magic allows you to provide a custom exceptions handler on a per folder level.
