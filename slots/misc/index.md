---
title: Misc slots
description: Magic's miscellaneous dynamic slots; loading files recursively, ensuring module databases, installing modules, and hashing passwords.
moved_anchors: {"magiciofileload-recursively": "/slots/misc/magic.io.file.load-recursively/", "magicmodulesensure-database": "/slots/misc/magic.modules.ensure-database/", "magicmodulesinstall-module": "/slots/misc/magic.modules.install-module/", "transformershash-password": "/slots/misc/transformers.hash-password/"}
---

## Misc slots

These are slots that don't belong to a specific category solving some problem related to your applications.

* [`magic.io.file.load-recursively`](/slots/misc/magic.io.file.load-recursively/) - This slot loads all files recursively within the specified folder, and returns their filenames and their content.
* [`magic.modules.ensure-database`](/slots/misc/magic.modules.ensure-database/) - This slot ensures that a module's database exists by invoking its associated create database SQL file.
* [`magic.modules.install-module`](/slots/misc/magic.modules.install-module/) - This slot installs a module that has been previously unzipped into your modules folder by making sure all startup files are executed.
* [`transformers.hash-password`](/slots/misc/transformers.hash-password/) - This slot is a "transformer" and typically used for input payloads originating from HTTP invocations, such as when creating a new user, etc.
