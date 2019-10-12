# Helper endpoints

Some tasks are simply so common that I have solved these generically for you, and
added controller endpoints for these tasks into the core of Magic. One example
of such a task is the ability to upload and download files from your server.

**Notice** - Uploading and downloading files requires you to be authorized
as _"root"_ to access them by default. Modifying this is easy though, by
diving into the C# source of Magic, and injecting your own authorization
service, and remove the existing authorization service. If you wish to do this,
feel free to look at the code in the project called _"magic.library"_.

In addition to the above endpoints, several other endpoints exists in
your _"system"_ folder. The easiest way to see which endpoints you
can use, is to open your _"Endpoints"_ menu item in Magic's dashboard,
for then to make the system endpoints visible by checking the
_"Show system endpoints"_ checkbox. This will only show you Hyperlambda
endpoints though.

[Hyperlambda 101](/hyperlambda)
