# Helper endpoints

Some tasks are simply so common that I have solved these generically for you, and
added controller endpoints for these tasks into the core of Magic. One example
of such a task is the ability to upload and download files from your server.
In fact, most of the common functions you'd normally use `System.IO` for,
have some sort of pre-existing controller solving this task for you, exposed
over the HTTP REST API. This allows you to create files and folders,
rename/move files and folders, upload files, download files, etc.

If you'd like to see these controller endpoints, you can use the Swagger Open Web
API documentation, which you can reach at `https://yourserver:port/swagger`.
If you're in Visual Studio on Window you can simply start your debugger,
and make sure you append _"swagger"_ after its launch URL after your browser
has been launched.

**Notice** - All of these endpoints requires you to be authorized as _"root"_
to access them by default. Modifying this is easy though, by diving into
the C# source of Magic, and injecting your own authorization service,
and remove the existing authorization service.

[Hyperlambda 101](/hyperlambda)
