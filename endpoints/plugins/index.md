---
title: Plugins endpoints
description: Magic's built-in plugin endpoints, listing installed plugins and installing new ones from the App Store.
header:
  image: /assets/images/hero/endpoints-top.png
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: Plugins endpoints
---

## Plugins endpoints

These are endpoints related to the [Plugins](/dashboard/plugins/) component somehow, allowing you to install
new plugins. The Plugins component is a micro service _"App Store"_ for your
Magic cloudlet, allowing your Magic server to install backend modules on the fly, resulting
in having some backend micro service installed into your backend, without interrupting normal
usage. None of these endpoints are really intended to be consumed by your own code, but only
for internal usage by Magic itself.

### GET magic/system/bazar/app-manifests

This endpoint returns a list of plugin apps that have been installed in your backend. Each item will
contain a date of installation, the username of the user who installed the app, the name and version
of the app, etc. Below is an example of what the endpoint might
return if you only have one plugin item installed. The endpoint can only be invoked by a root user and
it requires no arguments.

```
[
  {
    "version": "v1.0.0",
    "module_name": "babelfish"
  }
]
```

This endpoint is not intended for you to consume in your own code.

### POST magic/system/bazar/install-plugin

This endpoint downloads a plugin item as a zip file from the specified URL, and unzips the file into the backend,
for then to install the plugin by executing its startup files. The endpoint can only be invoked by a root user
and requires the following payload.

```
{
  "url": "https://some-bazar.com/download?app=some-app.zip",
  "name": "some-module",
  "type": "module"
}
```

* __[url]__ - URL to download the plugin's ZIP file from
* __[name]__ - Name of the module, becoming its folder name inside your modules folder
* __[type]__ - Type of plugin being installed

The plugin will be downloaded from the specified URL and assumed to be a zip file. The zip file
will then be unzipped into your _"modules"_ folder as the specified _"name"_. Notice, any
previously installed plugins with the same name will be automatically deleted and uninstalled.
