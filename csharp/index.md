# Extending Magic with C#

Obviously CRUD alone doesn't result in a complete web app, at least not for more complex
web applications. For those more complex occassions, where you need to add some custom C# code
to your application, you can easily do so by adding a new .Net Standard 2.0 library
into for instance your _"modules"_ folder in Visual Studio (Code).

After you have created your project containing your `ControllerBase` class(es), you
can simply reference this project into your _"magic.backend"_ project, and the endpoint(s)
will automatically load up as your web app is started. Have a look at the _"magic.io/magic.io.controller"_
project for an example of how to do this. Below is some example code illustrating it.

**Example C# controller**

```csharp
using Microsoft.AspNetCore.Mvc;

namespace acme
{
    [Route("api/acme")]
    public class AcmeController : ControllerBase
    {
        [HttpGet]
        public string MeaningOfLife()
        {
             return "42 spoketh Zarathustra";
        }
    }
}
```

## Automatically generated documentation

Magic uses Swagger and the Open Web API, allowing you to immediately start playing around
with your C# controller endpoints after having created them.

## Modularity and IoC/Dependency Injection

The above makes your final solution extremely modular in its design, and you can even reuse
controllers across multiple web apps if you wish. If you wish to separate the implementation
and using interfaces, dependency injection, and service implementations for your module -
You can have a look at how the _"magic.io"_ project(s) are wired together.

The important parts here is inside of _"magic.io.services/init/"_, where you will find 
a _"ConfigureServices.cs"_ file. This file adds up which services you want to use as
implementations for whichever service interfaces you have created. Basically, it 
configures your `IServiceCollection`, making the .Net IoC DI container know which
implementation class to use for whatever interface you need. At which point you can
just add an instance to your interface in your controller's constructor, and the .Net
DI IoC container will automatically inject your service for you.

**Important** - If you create your own class, that implements `IConfigureServices`
from _"magic.common.contracts"_, then the Magic core will automatically invoke your
`Configure` method when it needs to wire up your IoC container during startup. You
rarely if ever need to modify the actual backend web project to use Magic. Below
is an example of how the IO module is wiring up its services.

**Example of wiring up your IoC container**

```csharp
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using magic.io.contracts;
using magic.common.contracts;

namespace magic.io.services.init
{
    class ConfigureServices : IConfigureServices
    {
        public void Configure(IServiceCollection services, IConfiguration configuration)
        {
            services.AddTransient<IFileService, FileService>();
            services.AddTransient<IFolderService, FolderService>();
            services.AddTransient<IAuthorize, AuthorizeService>();
        }
    }
}
```

The above C# code basically associates the `IFileService`interface with your `FileService`
implementation class. Implying that every time you request an IFileService from your IoC
container, you'll be given a FileService implementation class.

If you take this approach, it's important that you also add a reference to your service
implementation project into your _"magic.backend"_ project. Magic will automatically
invoke all of your `IConfigureServices` implementations' `Configure` methods, in all
the assemblies that you are referencing from its _"magic.backend"_ project.

## Utility classes

Magic also contains a whole range of _"utility classes"_ to ease your life as a
C# software developer. For instance, if you need to invoke another Web API from
C#, this is literally as easy as creating a single line of C# code. Below is and
example.

```csharp
var result = await client.PostAsync<RequestDTO, ResponseDTO>("https://foo.com", request);
```

The above code will automatically translate your `request` into JSON, post it to
_"foo.com"_, translate the returned JSON into a `ResponseDTO` object, and return
it to your code as `result`. This allows you to integrate your code with other
HTTP REST APIs, with a single line of C#. The `client` above, is an instance
of `IHttpClient` which you can retrieve using Dependency Injection the same
way you would with any other service. The above code assumes you have a reference
in your assembly to _"magic.http.contracts"_, which contains the `IHttpClient`
interface.

[Helper endpoints](/helper-endpoints)
