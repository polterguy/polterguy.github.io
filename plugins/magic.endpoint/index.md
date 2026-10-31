---
title: magic.endpoint
moved_anchors: {"accepted-content-type-values-for-hyperlambda-endpoints": "/plugins/magic.endpoint/accepted-content-type-values-for-hyperlambda-endpoints/", "api-urls": "/plugins/magic.endpoint/api-urls/", "changing-your-hyperlambda-endpoints-response-type": "/plugins/magic.endpoint/hyperlambda-endpoints-and-meta-information/#changing-your-hyperlambda-endpoints-response-type", "configuring-your-code-behind-resolver": "/plugins/magic.endpoint/hyperlambda-code-behind-files/#configuring-your-code-behind-resolver", "dynamic-urls": "/plugins/magic.endpoint/hyperlambda-code-behind-files/#dynamic-urls", "extending-the-hyperlambda-content-type-request-and-response-resolver": "/plugins/magic.endpoint/accepted-content-type-values-for-hyperlambda-endpoints/#extending-the-hyperlambda-content-type-request-and-response-resolver", "extending-the-meta-data-retrieval-process": "/plugins/magic.endpoint/hyperlambda-endpoints-and-meta-information/#extending-the-meta-data-retrieval-process", "how-to-use-mimeadd": "/reference/slots/mime/mime.add/#guide", "how-to-use-mimelist": "/reference/slots/mime/mime.list/#guide", "how-to-use-requestverb": "/reference/slots/request/request.verb/#guide", "hyperlambda-and-cookies": "/plugins/magic.endpoint/slots-related-to-endpoints-and-the-http-context/#hyperlambda-and-cookies", "hyperlambda-code-behind-files": "/plugins/magic.endpoint/hyperlambda-code-behind-files/", "hyperlambda-endpoints-and-arguments": "/plugins/magic.endpoint/hyperlambda-endpoints-and-arguments/", "hyperlambda-endpoints-and-meta-information": "/plugins/magic.endpoint/hyperlambda-endpoints-and-meta-information/", "slots-related-to-endpoints-and-the-http-context": "/plugins/magic.endpoint/slots-related-to-endpoints-and-the-http-context/"}
---

magic.endpoint is your dynamic endpoint URL controller responsible for handling all HTTP requests.
It has two implementations. Which implementation is being used depends upon the URL you specify.

* `HttpApiExecutorAsync` - Resolves everything starting out with _"magic/"_ and is your primary API URL resolver
* `HttpFileExecutorAsync` - Resolving everything else and is your document and HTML resolver


## Interceptors

Interceptors are a common feature for both the `HttpApiExecutorAsync` resolver and the `HttpFileExecutorAsync` resolver. An interceptor is a Hyperlambda file named _"interceptor.hl"_. It will intercept all requests going to the folder it's located, or a sub-folder, and create a combined lambda object consisting of both the interceptor.hl file, and the file responsible for resolving the URL.

To understand interceptors, imagining the following two Hyperlambda files.

**/modules/foo/interceptor.hl**

```
data.connect:magic
   .interceptor
```

**/modules/foo/bar.get.hl**

```
data.read
   table:roles
   columns
      name
```

When an HTTP GET request enters your backend with the URL of _"magic/modules/foo/bar"_ , the Hyperlambda that actually executes becomes the following.

```
data.connect:magic
   data.read
      table:roles
      columns
         name
```

The above **[.interceptor]** node in your interceptor will be replaced by the content of your resolved Hyperlambda file. This allows you to create more DRY code, by having commonalities inside a common Hyperlambda file, one common file for each folder, and/or its sub-folders. You _can_ have as many **[.interceptor]** nodes as you wish in your interceptors, but for obvious reasons we recommend only having _one_.

Interceptors such as the above are recursively applied, allowing you to create as many levels of interceptors as you wish.


## Exception handlers

If you've got a file named _"exceptions.hl"_ inside one of your folders, it will be invoked if an unhandled exception occurs. Your exception handler will be invoked only for unhandled exceptions for requests inside the folder where it exists physically, allowing you to have different exceptions handlers for different parts of your app.

Notice, contrary to interceptors exception handlers will _not_ be recursively applied, and only the inner most exception handler will be invoked. Below is a simple exception handler that simply creates a log entry, returning a static message to the client, with the message propagating to the client, and its status code being 456.

```
log.error:x:@.arguments/*/message
   url:x:@.arguments/*/path
return
   message:Jo dude! Erred!
   public:bool:true
   status:int:456
```


## Topics

* [API URLs](/plugins/magic.endpoint/api-urls/) - The HttpApiExecutorAsync resolver will be invoked for all relative URLs starting with "magic/", for the following verbs.
* [Hyperlambda endpoints and arguments](/plugins/magic.endpoint/hyperlambda-endpoints-and-arguments/) - The default IHttpExecutorAsync implementation can explicitly declare what arguments the file can legally accept, and if an argument is given during invocation that the file doesn't allow for, an excep
* [Accepted Content-Type values for Hyperlambda endpoints](/plugins/magic.endpoint/accepted-content-type-values-for-hyperlambda-endpoints/) - The POST, PUT and PATCH endpoints can intelligently handle any of the following Content-Types.
* [Hyperlambda endpoints and meta information](/plugins/magic.endpoint/hyperlambda-endpoints-and-meta-information/) - Due to the semantic structure of Hyperlambda, retrieving meta information from your HTTP endpoints using this module is very easy.
* [Hyperlambda code behind files](/plugins/magic.endpoint/hyperlambda-code-behind-files/) - The HttpFileExecutorAsync resolver will resolve everything not starting out with magic/ as a file, optionally applied as a mixin file having a Hyperlambda code behind file for mixing in dynamic conten
* [Slots related to endpoints and the HTTP context](/plugins/magic.endpoint/slots-related-to-endpoints-and-the-http-context/) - In addition to the meta retrieval endpoint described above, the module contains the following slots.
