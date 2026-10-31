---
title: "How to use [magic.modules.ensure-database]"
description: "How to use [magic.modules.ensure-database] - This slot ensures that a module's database exists by invoking its associated create database SQL file."
guide: true
slots: ["magic.modules.ensure-database"]
---

This slot ensures that a module's database exists by invoking its associated create database SQL file. The
slot requires the following arguments.

* __[module]__ - Name of module
* __[database]__ - Name of database to check for
* __[database-type]__ - Optional type of database. If not specified defaults to the default database type

The slot basically checks to see if the specified **[database]** database exists, and if not, attempts
to find its associated _"xxx.yyy.sql"_ script within its folder, where _"xxx"_ is the module name and
_"yyy"_ is the default database type. The slot will also automatically execute any migration scripts
associated with the module. Notice, the _"Ensure database"_ macro in _"Hyper IDE"_ automatically takes
care of wiring up invocations to this slot, creating the required structure in the process.
