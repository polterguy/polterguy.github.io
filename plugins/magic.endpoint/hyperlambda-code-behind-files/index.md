---
title: "Hyperlambda code behind files"
description: "Hyperlambda code behind files - The HttpFileExecutorAsync resolver will resolve everything not starting out with magic/ as a file, optionally applied as a mixin file having a Hyperlambda code behind file for mixing in..."
generated: true
---

This page is part of the [magic.endpoint](/plugins/magic.endpoint/) documentation.

The `HttpFileExecutorAsync` resolver will resolve everything _not_ starting out with `magic/` as a file,
optionally applied as a mixin file having a Hyperlambda code behind file for mixing in dynamic content
with _".html"_ files. This allows you to render HTML, CSS, JavaScript and _"whatever"_, with the ability
to dynamically render parts of your HTML files using Hyperlambda. This logic relies upon the **[io.file.mixin]**
slot from the _"magic.lambda.io"_ project. If you create two files such as follows, and put both of these
files in your _"/etc/www/"_ folder, you can see this logic in action.

**index.html**

{% raw %}
```
<html>
    <head>
        <title>Hello world</title>
    </head>
    <body>
        <h1>Hello world</h1>
        <p>
           Hello there Thomas Hansen,
           2+2 equals {{*/.calculate}}
        </p>
    </body>
</html>
```
{% endraw %}

**index.hl**

```
.calculate
   math.add
      .:int:2
      .:int:2
   return:x:-
```

The above will substitute your {% raw %}`{{*/.calculate}}`{% endraw %} parts with the result of invoking your **[.calculate]** lambda
object, resulting in 4. To understand how this works, you need to read about the **[io.file.mixin]** slot in
the _"magic.lambda.io"_ project, and realise that the above will actually transform to the following as the
mixin logic is executed.

```
io.file.mixin:/etc/www/index.html
   .calculate
      math.add
         .:int:2
         .:int:2
      return:x:-
```

This allows you to serve dynamically rendered HTML files, where parts of your HTML is substituted with the
result of invoking some lambda object. If you have an HTML file _without_ a Hyperlambda code behind file,
it will be served as a static file. CSS files, JavaScript files, and images will also be served as static
files.

This resolver will resolve to everything within your _"/etc/www/"_ folder. If you've got an _"index.html"_ page in some folder, this file will be assumed to be the default document of that folder.

Interceptor Hyperlambda files will be executed as normally, allowing you to apply interceptor files similarly
to how you apply these with your _"/magic/"_ endpoints.

The resolver will also rewrite and redirect automatically every URL ending with _".html"_ and remove the file extension parts, in addition to removing _"index"_ at the end afterwards, to avoid duplicated URLs.

## Dynamic URLs

If you've got a file called _"default.html"_, and the client is requesting a URL that does not have an associated physical file existing for the absolute path specified - Then your _"default.html"_ file will resolve the specified URL. Such a _"default.html"_ file can also optionally have a Hyperlambda code behind file, allowing you to serve dynamic content based upon the URL of the request. This allows you to use dynamic URLs, to for instance lookup files from your database and serve back as dynamic content.

If you want to use dynamic pages, you can retrieve the request URL by invoking the **[request.url]** slot to retrieve the request URL.

## Configuring your code behind resolver

You can also apply a **[.config]** file at the root of you _"/etc/www/"_ folder that partially changes the resolver's behavior. To illustrate how to use such a config file, consider the following.

**/etc/www/.config**

```
static_files
   headers
      *
         Cache-Control:public, max-age=31536000
      woff2
         Cache-Control:public, max-age=31536000
         Content-Type:font/woff2
         Access-Control-Allow-Origin:*
      css
         Access-Control-Allow-Origin:*
not_found:/etc/www/.sys/404.html
spa_enabled:bool:true
redirect
   .
      from:foo1
      to:bar1
   .
      from:foo2
      to:bar2
```

The first parts named **[static_files]** is for file without a mixin file, which includes _".html"_ files without a Hyperlambda code behind file, and all other files ending with any other extension. It applies the first `Cache-Control` to all files except those ending with _".woff"_ and _".css"_. Then it applies its **[woff]** HTTP headers and **[css]** parts for files ending with _".woff"_ and _".css"_ respectively.

The **[not_found]** parts declares an HTML file to serve if no file is found that resolves the URL. Its default value is _"/etc/www/.components/404.html"_, but you can override this with the above **[not_found]** configuration setting. This file will resolve as a _"mixin file"_ allowing you to have code behind Hyperlambda file somehow modifying the end result. If you don't have any 404 file at all, the resolver will simply return the static string _"Not found"_.

The last setting called **[spa_enabled]** will default resolving to your _"/etc/www/index.html"_ file, unless some other file matches any other rules, such as a _"default.html"_ file in some sub-folder triggering a match. This allows you to create SPA web applications, where resolving occurs on the frontend. This is useful for things such as Angular and ReactJS that's using frontend URL routing, where everything is still served the same _"index.html"_ file. Its default value is false.

The **[redirect]** parts allows you to declare 301 redirects if URLs are changing.

---

[&larr; Hyperlambda endpoints and meta information](/plugins/magic.endpoint/hyperlambda-endpoints-and-meta-information/) | [all of magic.endpoint](/plugins/magic.endpoint/) | [Slots related to endpoints and the HTTP context &rarr;](/plugins/magic.endpoint/slots-related-to-endpoints-and-the-http-context/)
