# Extending Magic with C#

Obviously CRUD alone doesn't result in a complete web app, at least not for more complex
web applications. For those more complex occassions, where you need to add some custom C# code
to your application, you can easily do so by creating a new .Net Core library.

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

## Utility classes

Magic also contains a whole range of _"utility classes"_ to ease your life as a
C# software developer. For instance, if you need to invoke another Web API from
C#, this is literally as easy as creating a single line of C# code. Below is an
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

[Authentication](/authentication)
