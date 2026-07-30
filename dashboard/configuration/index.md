---
title: Configuration
description: Manage your Magic server's settings as a root user. Changes take effect instantly and immediately alter your server's behaviour, with no restart needed.
header:
  image: /assets/images/hero/configuration.png
  og_image: /assets/images/hero/configuration-og.png
  image_description: The Configuration component
faq:
  - q: "What is the Configuration component?"
    a: "It lets you view and edit your server's configuration - the appsettings.json file used throughout the system for settings such as SMTP, OpenAI, database connection strings, and authentication."
  - q: "Is it dangerous to edit the configuration?"
    a: "You should be careful, since erroneous configuration can stop your system from working or weaken its security. The component refuses to save invalid JSON, and provides helper dialogs for the most important sections such as OpenAI, SMTP and reCAPTCHA."
  - q: "How do I restrict which frontends can call my backend?"
    a: "The magic:frontend:urls section declares CORS, as a comma separated list of URLs allowed to retrieve data from your backend. By default all URLs are allowed."
  - q: "Where do I configure my database connections?"
    a: "The magic:databases section holds connection strings for sqlite, mysql, pgsql and mssql, each as name/value pairs, plus a default database type."
  - q: "What is the auth secret?"
    a: "The magic:auth section's secret is the key used to sign your JWT tokens - it must be kept secret, and changing it invalidates all previously issued tokens."
---

The configuration component allows you to view and edit your server's configuration settings. Your server's configuration is basically your _"appsettings.json"_ file, which is being used in all parts of the system to retrieve configuration settings, such as for instance SMTP settings when email slots are sending emails, etc.

![Screenshot of configuring Magic through its Configuration component](/images/config-component.jpg)

You should be careful as you edit your server's configuration settings, since this might result in that your server becomes erroneously configured, resulting in that your system stops working - In addition to that if you edit your server's configuration erroneously, you might open up your server
such that malicious adversaries gain access to your system. The configuration component has helper UI elements to help you configure things such as OpenAI, SMTP and reCAPTCHA, giving you a graphical user interface to edit some of its most important parts.

The _"OpenAI"_ button lets you supply your OpenAI API key without touching the JSON.

![Screenshot of configuring your OpenAI API key](/assets/images/config-openai-key.jpeg)

The _"reCAPTCHA"_ button similarly asks you for your reCAPTCHA site key and secret.

![Screenshot of configuring your reCAPTCHA keys](/assets/images/config-recaptcha-keys.jpeg)

And the _"SMTP"_ button configures your email server; host, port, credentials, and the default from name and address.

![Screenshot of configuring your SMTP settings](/assets/images/config-smtp-settings.jpeg)

Notice, if you supply buggy JSON the component will not allow for saving your configuration, but instead provide you with an error message informing you that your JSON has errors. You can also create your own configuration sections as you see fit to use in your own modules.

The component also lets you download a backup of your entire configuration as a file, and restore your configuration from such a backup later - useful before making larger changes, or when moving settings between cloudlets.

Below is a list of the most important sections you can configure in your cloudlet.

## CORS

The `magic:frontend:urls` section allows you to explicitly specify CORS, implying frontend URLs that are allowed to retrieve data from your backend. Its default setting implies _all_ URLs are allowed to retrieve data from your backend, but sometimes you need to explicitly specify one or more URLs here. You can do this by adding a comma separated list of URLs in this setting.

## SMTP configuration

The `magic:smtp` section allows you to specify which SMTP server Magic should use for sending emails. Most parts of this section are self explanatory, but the `from` section is the default from name and address to use, which is only used if an email is sent _without_ explicitly declaring who it originated from.

## Database configuration

The `magic:databases` section allows you to configure your database connection strings. Magic supports 4 relational database types, these are as follows.

* `sqlite` - SQLite
* `mysql` - MySQL + MariaDB
* `pgsql` - PostgreSQL
* `mssql` - SQL Server

You can use all of the above database types in your Magic server. However, to access your database you need to provide Magic with one or more connection strings. Each of these sections contains a key/value pair where the key becomes the name of your connection string, and the value its actual
connection string. This section also has a `default` setting, which is the default database type to use if not specified by caller. This needs to be one of _"mysql"_, _"pgsql"_, _"sqlite"_, or _"mssql"_ - Implying MySQL, PostgreSQL, SQLite or SQL Server.

You would typically never edit the default setting, since Magic only supports SQLite as its primary magic database out of the box.

## Authentication and authorisation configuration

This section allows you to override the default authentication and authorisation values for Magic. Its sub-sections imply the following.

* `secret` - JWT secret used to generate a JWT signature
* `https-only` - If true this implies JWT tokens will only be verified over an SSL/TLS connection
* `valid-minutes` - Default number of minutes before JWT token generated by Magic expires. Notice, this can be overridden as your Hyperlambda code is creating a JWT token, but the authenticate endpoint respects this value by default

## Logging configuration

The `level` parts of this section imply which logging level you want to use. Magic supports 5 legal values for this setting, and these are as follows.

* `debug` - Log everything
* `info` - Log only from info level and above
* `error` - Log only from error level and above
* `fatal` - Log only fatal errors
* `off` - Never log

This works similarly to log4net, and implies _"minimum logging level"_, where any log invocations from and above your minimum level are logged, while the rest of your log invocations will be ignored. The default value of _"debug"_ implies that everything will be logged.

## Sockets configuration

The `url` setting here allows you to override which URL clients need to use to negotiate a socket channel with your server. You can also completely turn off web sockets entirely here, by changing the value to `null` or remove the section entirely.

{% include faq.html %}
