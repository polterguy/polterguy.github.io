---
title: magic.lambda.config
moved_anchors: {"how-to-use-configget": "/plugins/magic.lambda.config/config.get/"}
---

This project provides configuration settings slots for Magic. The project provides the following
slots, allowing you to retrieve configuration settings from your _"appsettings.json"_ configuration file,
in addition to saving and loading your configuration file.

* __[\[config.get\]](/reference/slots/config/config.get/)__ - Returns a configuration value from your configuration file with the specified key
* __[\[config.section\]](/reference/slots/config/config.section/)__ - Returns the specified configuration section from your configuration file with the specified key
* __[\[config.load\]](/reference/slots/config/config.load/)__ - Loads your _"appsettings.json"_ file and returns as a string
* __[\[config.save\]](/reference/slots/config/config.save/)__ - Saves your _"appsettings.json"_ file, sanity checking it's valid JSON before persisting your file
