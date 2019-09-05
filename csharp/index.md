# Extending Magic with C#

Obviously CRUD alone doesn't result in a complete web app, at least not for more complex
web applications. For those more complex occassions, where you need to add some custom C# code
to your application, you can easily do so by adding a new .Net Standard 2.0 library
into for instance your _"modules"_ folder in Visual Studio (Code).

After you have created your project containing your `ControllerBase` class(es), you
can simply reference this project into your _"magic.backend"_ project, and the endpoint(s)
will automatically load up as your web app is started. Have a look at the _"magic.io/magic.io.controller"_
project for an example of how to do this. Below is some example code illustrating it.

```csharp
using Microsoft.AspNetCore.Mvc;

namespace acme
{
    [Route("api/acme")]
    public class FilesController : ControllerBase
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

This makes your final solution extremely modular in its design, and you can even reuse
controllers across multiple web apps if you wish. If you wish to separate the implementation
and using interfaces, dependency injection, and service implementations for your module -
You can have a look at how the _"magic.io"_ project(s) are wired together. The important
parts here is inside of _"magic.io.services/init/"_, where you will find a _"ConfigureServices.cs"_
file. This file adds up which services you want to use as implementations for whichever
service interfaces you have created. Basically, it configures your `IServiceCollection`,
making the .Net IoC DI container know which implementation class to use for whatever
interface you need. At which point you can just add an instance to your interface
in your controller's constructor, and the .Net DI IoC container will automatically
inject your service for you.

**Important** - If you create your own class, that implements `IConfigureServices`
from _"magic.common.contracts"_, then the Magic core will automatically invoke your
`Configure` method when it needs to wire up your IoC container during startup.

If you take this approach, it's important that you also add a reference to your service
implementation project into your _"magic.backend"_ project.

[Home](/)
