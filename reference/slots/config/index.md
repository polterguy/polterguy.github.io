---
title: config.* slots
description: The 4 slots named config.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [config.get]

Reads a single setting from appsettings.json by dotted key path (e.g. 'magic:auth:secret').

* **Value** (`config-key`), required: Configuration key to retrieve
* **Returns**: Resolves to the configuration value, or the first child value when the key is missing

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | no | Default value source evaluated and returned when the configuration key does not exist. |

Guide: [How to use [config.get]](/plugins/magic.lambda.config/#how-to-use-configget)

## [config.load]

Returns the raw contents of appsettings.json; pair with [config.save] for round-trip config editing.

* **Returns**: Resolves to the raw appsettings.json content

## [config.save]

Saves JSON configuration values to appsettings.json.

* **Value** (`json`), required: Valid JSON object content to save to appsettings.json

## [config.section]

Reads an entire appsettings.json section by key, returning its keys and nested values as child nodes.

* **Value** (`config-key`), required: Configuration section to retrieve
* **Returns**: Returns one child node per key/value entry in the requested configuration section

