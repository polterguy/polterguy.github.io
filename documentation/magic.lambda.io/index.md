
# Magic Lambda IO

This project provides file/folder slots for Magic. More specifically, it provides the following slots.

* __[io.folder.create]__ - Creates a folder on disc for you on your server.
* __[io.folder.exists]__ - Returns true if folder exists, otherwise false.
* __[io.folder.delete]__ - Deletes a folder on disc on your server.
* __[io.folder.list]__ - Lists all folders within another source folder.
* __[io.file.load]__ - Loads a file from disc on your server.
* __[io.file.save]__ - Saves a file on disc on your server.
* __[io.file.exists]__ - Returns true if file exists, otherwise false.
* __[io.file.delete]__ - Deletes a file on your server.
* __[io.file.copy]__ - Copies a file on your server.
* __[io.file.execute]__ - Executes a Hyperlambda file on your server.
* __[io.file.list]__ - List files in the specified folder on your server.
* __[io.file.move]__ - Moves a file on your server.
* __[io.content.zip-stream]__ - Creates a ZipStream for you, without touching the file system.
* __[.io.folder.root]__ - Returns the root folder of your system. (private C# slot)

## Fundamentals

All of these slots can _only_ manipulate files and folders inside of your _"files"_ folder in your web server.
This are normally files inside of the folder you have configured in your _"appsettings.json"_ file, with the
key _"magic.io.root-folder"_. This implies that all paths are _relative_ to this path, and no files or folders
from outside of this folder can in any ways be manipulated using these slots.

Notice, if you wish to change this configuration value, then the character tilde "~" means root
folder where your application is running from within. There is nothing preventing you from using an
absolute path, but if you do, you must make sure your web server process have full rights to modify
files within this folder.

### io.folder.create

Creates a new folder on disc. The example below will create a folder named _"foo"_ inside of the _"misc"_ folder.
Notice, will throw an exception if the folder already exists.

```
io.folder.create:/misc/foo/
```

### io.folder.exists

Returns true if specified folder exists on disc.

```
io.folder.exists:/misc/foo/
```

### io.folder.delete

Deletes the specified folder on disc. Notice, will throw an exception if the folder doesn't exists.

```
io.folder.delete:/misc/foo/
```

### io.folder.list

Lists all folders inside of the specified folder. By default hidden folders will not be shown, unless
you pass in **[display-hidden]** and set its value to boolean _"true"_.

```
io.folder.list:/misc/
```

### io.file.load

Loads the specified text file from disc. This slot can _only load text files_. Or to be specific,
there are no ways you can change binary files, hence loading a binary file is for the most parts
not something you should do. Although there _might_ exist exceptions to this.

```
io.file.load:/misc/README.md
```

### io.file.save

Saves the specified content to the specified file on disc, overwriting any previous content if the
file exists from before, creating a new file if no such file already exists. The value of the first
argument will be considered the content of the file.

Notice, the node itself will be evaluated, allowing you to have other slots evaluated before slot saves
the file, to return dynamically the content of your file.

```
io.file.save:/misc/README2.md
   .:This is new content for file
```

### io.file.exists

Returns true if specified file exists from before.

```
io.file.exists:/misc/README.md
```

### io.file.delete

Deletes the specified file. Will throw an exception if the file doesn't exist.

```
io.file.load:/misc/DOES-NOT-EXIST.md
```

### io.file.copy

Copies the specified file to the specified destination folder and file.
Notice, requires the destination folder to exist from before, and the source
file to exist from before. This slot will delete any previously existing destination
file, before starting the copying process. Just like the save slot, this will evaluate
the lambda children before it executes the copying of your file, allowing you to use
the results of slots as the destination path for your file.

```
io.file.copy:/misc/README.md
   .:/misc/backup/README-backup.md
```

Notice, the folder parts of thye destination folder is _optional_, and if you don't supply a folder
as a part of the path, the source folder will be used by default.

### io.file.execute

Executes the specified Hyperlambda file. Just like when evaluating a dynamic slot, you can
pass in an **[.arguments]** node to the file, which will be considered arguments to your file.
Hence, this slot allows you to invoke a file, as if it was a dynamically created slot, and there
is no semantic difference really between this slot and **[signal]** from the _magic.lambda.slots_
project.

```
io.file.execute:/misc/some-hyperlambda-file.hl
```

### io.file.list

Lists all files inside of the specified folder. By default hidden files will not be shown, unless
you pass in **[display-hidden]** and set its value to boolean _"true"_.

```
io.file.list:/misc/
```

### io.file.move

Similar to **[io.file.copy]** but deletes the source file after evaluating.

```
io.file.move:/misc/README.md
   .:/misc/backup/README-backup.md
```

### io.content.zip-stream

Creates a memory based ZIP stream you can return over the response socket connection. Notice,
this doesn't create a zip file, but rather a zip stream, which you can manipulate using other
slots. This slot is useful if you need to return zipped content as your HTTP response for instance.

Notice, both the root arguments (lambda children) of this slot will be evaluated, in addition to
its content nodes, evaluated once for each file declaration node.

```
io.content.zip-stream
   .:/foo/x.txt
      .:content of file
```

### .io.folder.root

Returns the root folder of the system. Cannot be invoked from Hyperlambda, but only from C#. Intended as
a support function for other C# slots.

```csharp
var node = new Node();
signaler.Signal(".io.folder.root", node);

// Retrieving root folder after evaluating slot.
var rootFolder = node.Get<string>();
```

## C# extensions

If you want to, you can easily completely exchange the underlaying file system, with your own _"virtual file system"_,
since all interaction with the physical file system is done through the `IFileService` and `IFolderService` interfaces.
This allows you to circumvent the default dependency injected service, and binding towards some other implementation,
at least in theory allowing you to (for instance) use a database based file system, etc. If you want to do this, you'll
need to supply your own bindings to the following two interfaces, using your IoC container.

* `magic.lambda.io.contracts.IFileService`
* `magic.lambda.io.contracts.IFolderService`

If you want to do this, you would probably want to manually declare your own implementation for these classes, by tapping
into _"magic.library"_ somehow, or not invoking its default method that binds towards the default implementation classes
somehow.

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/documentation/magic.lambda.io.svg?master)](https://travis-ci.com/polterguy/documentation/magic.lambda.io)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.io&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.io)
