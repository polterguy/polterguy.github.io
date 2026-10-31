---
title: "config.* slots"
description: "The 4 slots named config.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

4 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`config.get`](/reference/slots/config/config.get/) | Reads a single setting from appsettings.json by dotted key path (e.g. 'magic:auth:secret'). |
| [`config.load`](/reference/slots/config/config.load/) | Returns the raw contents of appsettings.json; pair with [config.save] for round-trip config editing. |
| [`config.save`](/reference/slots/config/config.save/) | Saves JSON configuration values to appsettings.json. |
| [`config.section`](/reference/slots/config/config.section/) | Reads an entire appsettings.json section by key, returning its keys and nested values as child nodes. |

