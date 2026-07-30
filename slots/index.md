---
title: Slots
description: Documentation for the most important dynamic slots you can find in Magic's middleware
---

Magic creates the following dynamic slots during startup. Notice, most of these slots are there exclusively
to make sure the middleware of Magic works correctly, and are _not_ intended to be used directly by you
in your own [Hyperlambda](/hyperlambda/) code, unless explicitly stated otherwise, and/or you're extending
Magic, or replacing parts of its core with your own custom logic.

* __[magic.auth.authenticate]__ - Authenticates a user and returns a JWT token
* __[magic.auth.change-password]__ - Allows a user to reset his or her password
* __[magic.auth.create-user]__ - Creates a new user in Magic
* __[magic.auth.ensure-role]__ - Ensures the specified role exists, and if not, creates it
* __[magic.db.mysql.databases]__ - Returns all databases for a specified connection string
* __[magic.db.mysql.tables]__ - Returns all tables for the specified connection-string/database combination
* __[magic.db.mysql.columns]__ - Returns all columns for a specified connection-string/database/table combination
* __[magic.db.mysql.foreign_keys]__ - Returns all foreign keys for a specified connection-string/database/table combination
* __[magic.db.mysql.indexes]__ - Returns all indexes for the specified connection-string/database/table combination
* __[magic.db.mssql.*]__ - SQL Server versions of the five slots above
* __[magic.db.pgsql.*]__ - PostgreSQL versions of the five slots above
* __[magic.db.sqlite.*]__ - SQLite versions of the five slots above
* __[magic.io.file.load-recursively]__ - Loads all files from within some folder recursively
* __[magic.modules.ensure-database]__ - Ensures some database exists by executing its create database SQL file
* __[magic.modules.install-module]__ - Installs a module in your system
* __[transformers.hash-password]__ - Hashes a specified password in place

## Slot reference

The reference documentation is organised by concept. Each page below documents every slot within its
category; its arguments, example usage, and what the slot returns.

* [Authentication and authorisation slots](/slots/auth/) - Authenticating users, changing passwords, creating users, and ensuring roles exist
* [Database meta traversal slots](/slots/database-meta/) - Listing databases, tables, columns, foreign keys and indexes across all four database types
* [Misc slots](/slots/misc/) - Loading files recursively, ensuring module databases, installing modules, and hashing passwords
