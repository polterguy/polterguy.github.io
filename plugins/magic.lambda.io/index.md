---
title: magic.lambda.io
moved_anchors: {"how-to-use-execute-file": "/plugins/magic.lambda.io/execute-file/", "how-to-use-iocontentzip-stream": "/plugins/magic.lambda.io/io.content.zip-stream/", "how-to-use-iofilecopy": "/plugins/magic.lambda.io/io.file.copy/", "how-to-use-iofiledelete": "/plugins/magic.lambda.io/io.file.delete/", "how-to-use-iofileexecute": "/plugins/magic.lambda.io/io.file.execute/", "how-to-use-iofileexists": "/plugins/magic.lambda.io/io.file.exists/", "how-to-use-iofilelist": "/plugins/magic.lambda.io/io.file.list/", "how-to-use-iofilelist-recursively": "/plugins/magic.lambda.io/io.file.list-recursively/", "how-to-use-iofileload": "/plugins/magic.lambda.io/io.file.load/", "how-to-use-iofileload-recursively": "/plugins/magic.lambda.io/io.file.load-recursively/", "how-to-use-iofileloadbinary": "/plugins/magic.lambda.io/io.file.load.binary/", "how-to-use-iofilemixin": "/plugins/magic.lambda.io/io.file.mixin/", "how-to-use-iofilemove": "/plugins/magic.lambda.io/io.file.move/", "how-to-use-iofilepatch": "/plugins/magic.lambda.io/io.file.patch/", "how-to-use-iofilesave": "/plugins/magic.lambda.io/io.file.save/", "how-to-use-iofilesavebinary": "/plugins/magic.lambda.io/io.file.save.binary/", "how-to-use-iofilesearch": "/plugins/magic.lambda.io/io.file.search/", "how-to-use-iofileunzip": "/plugins/magic.lambda.io/io.file.unzip/", "how-to-use-iofoldercopy": "/plugins/magic.lambda.io/io.folder.copy/", "how-to-use-iofoldercreate": "/plugins/magic.lambda.io/io.folder.create/", "how-to-use-iofolderdelete": "/plugins/magic.lambda.io/io.folder.delete/", "how-to-use-iofolderexists": "/plugins/magic.lambda.io/io.folder.exists/", "how-to-use-iofolderlist": "/plugins/magic.lambda.io/io.folder.list/", "how-to-use-iofolderlist-recursively": "/plugins/magic.lambda.io/io.folder.list-recursively/", "how-to-use-iofoldermove": "/plugins/magic.lambda.io/io.folder.move/", "how-to-use-iopathget-folder": "/plugins/magic.lambda.io/io.path.get-folder/", "how-to-use-iostreamclose": "/plugins/magic.lambda.io/io.stream.close/", "how-to-use-iostreamopen-file": "/plugins/magic.lambda.io/io.stream.open-file/", "how-to-use-iostreamread": "/plugins/magic.lambda.io/io.stream.read/", "how-to-use-iostreamsave-file": "/plugins/magic.lambda.io/io.stream.save-file/"}
---

This project provides file/folder slots for Magic. More specifically, it provides the following slots.

* __[\[io.folder.create\]](/plugins/magic.lambda.io/io.folder.create/)__ - Creates a folder on disc for you on your server
* __[\[io.folder.exists\]](/plugins/magic.lambda.io/io.folder.exists/)__ - Returns true if folder exists, otherwise false
* __[\[io.folder.delete\]](/plugins/magic.lambda.io/io.folder.delete/)__ - Deletes a folder on disc on your server
* __[\[io.folder.list\]](/plugins/magic.lambda.io/io.folder.list/)__ - Lists all folders within another source folder
* __[\[io.folder.list-recursively\]](/plugins/magic.lambda.io/io.folder.list-recursively/)__ - Lists all folders within another source folder, including all nested folders
* __[\[io.folder.move\]](/plugins/magic.lambda.io/io.folder.move/)__ - Moves a folder to its specified destination
* __[\[io.folder.copy\]](/plugins/magic.lambda.io/io.folder.copy/)__ - Copies a folder to its specified destination
* __[\[io.file.load\]](/plugins/magic.lambda.io/io.file.load/)__ - Loads a file from disc on your server
* __[\[load-file\]](/plugins/magic.lambda.io/load-file/)__ - Alias for **[io.file.load]**
* __[\[io.file.load-recursively\]](/plugins/magic.lambda.io/io.file.load-recursively/)__ - Loads all files in a folder, including all nested folders, returning each file's name and content
* __[\[io.file.load.binary\]](/plugins/magic.lambda.io/io.file.load.binary/)__ - Loads a file from disc on your server as a byte array
* __[\[io.file.save\]](/plugins/magic.lambda.io/io.file.save/)__ - Saves a file on disc on your server
* __[\[save-file\]](/plugins/magic.lambda.io/save-file/)__ - Alias for **[io.file.save]**
* __[\[io.file.save.binary\]](/plugins/magic.lambda.io/io.file.save.binary/)__ - Saves a file on disc on your server but contrary to the above assumes content to save is binary
* __[\[io.file.patch\]](/plugins/magic.lambda.io/io.file.patch/)__ - Applies a unified diff patch to a file on disc on your server
* __[\[io.file.exists\]](/plugins/magic.lambda.io/io.file.exists/)__ - Returns true if file exists, otherwise false.
* __[\[io.file.delete\]](/plugins/magic.lambda.io/io.file.delete/)__ - Deletes a file on your server.
* __[\[io.file.copy\]](/plugins/magic.lambda.io/io.file.copy/)__ - Copies a file on your server.
* __[\[io.file.execute\]](/plugins/magic.lambda.io/io.file.execute/)__ - Executes a Hyperlambda file on your server.
* __[\[execute-file\]](/plugins/magic.lambda.io/execute-file/)__ - Alias for **[io.file.execute]** except it will forward evaluate all descendant nodes using **[unwrap]**
* __[\[io.file.list\]](/plugins/magic.lambda.io/io.file.list/)__ - List files in the specified folder on your server.
* __[\[io.file.list-recursively\]](/plugins/magic.lambda.io/io.file.list-recursively/)__ - List files in the specified folder on your server, including all nested folders.
* __[\[io.file.move\]](/plugins/magic.lambda.io/io.file.move/)__ - Moves a file on your server.
* __[\[io.file.unzip\]](/plugins/magic.lambda.io/io.file.unzip/)__ - Unzips a file on your server.
* __[\[io.stream.open-file\]](/plugins/magic.lambda.io/io.stream.open-file/)__ - Opens the specified filename and returns it as a stream
* __[\[io.stream.save-file\]](/plugins/magic.lambda.io/io.stream.save-file/)__ - Saves a stream to the specified destination path
* __[\[io.stream.read\]](/plugins/magic.lambda.io/io.stream.read/)__ - Reads all content from the specified stream as a byte array
* __[\[io.stream.close\]](/plugins/magic.lambda.io/io.stream.close/)__ - Closes a previously opened stream
* __[\[io.content.zip-stream\]](/plugins/magic.lambda.io/io.content.zip-stream/)__ - Creates a ZipStream for you, without touching the file system
* __[\[io.path.get-folder\]](/plugins/magic.lambda.io/io.path.get-folder/)__ - Returns the folder part of the specified path
* __[.io.folder.root]__ - Returns the root folder of your system. (private C# slot)
* __[\[io.file.mixin\]](/plugins/magic.lambda.io/io.file.mixin/)__ - Allows you to invoke lambda objects from a file and substitute content dynamically in your original file
* __[\[io.file.search\]](/plugins/magic.lambda.io/io.file.search/)__ - Searches file content and returns filename + line numbers


## magic.lambda.io fundamentals

magic.lambda.io can _only_ manipulate files and folders inside of your _"files"_ folder in your web server.
These are normally files inside of the folder you have configured in your _"appsettings.json"_ file, with the
key _"magic.io.root-folder"_. This implies that all paths are _relative_ to this path, and no files or folders
from outside of this folder can in any ways be manipulated using these slots. These are the files you
can see when you open Hyper IDE.

Notice, if you wish to change this configuration value, then the character tilde "~" means root
folder where your application is running from within. There is nothing preventing you from using an
absolute path, but if you do, you must make sure your web server process have full rights to modify
files within this folder. We do not recommend changing this configuration setting.

### How to use [.io.folder.root]

Returns the root folder of the system. Cannot be invoked from Hyperlambda, but only from C#. Intended as
a support function for other C# slots.

```
var node = new Node();
signaler.Signal(".io.folder.root", node);

// Retrieving root folder after evaluating slot.
var rootFolder = node.Get<string>();
```


## Restricting file access with [whitelist]

Every slot in this project verifies its path against the **[whitelist]** vocabulary in scope, if any,
comparing it segment by segment such that a wildcard is confined to the segment it occurs in.

```
whitelist
   vocabulary
      io.file.load:/etc/*.md
      io.folder.create:/etc/*/
   .lambda
      io.file.load:/etc/readme.md
```

* __/etc/*__ - Every file directly in the folder, but _not_ in its sub folders
* __/etc/*.md__ - Every markdown file directly in the folder
* __/etc/\*/config.json__ - That filename, one folder level below

A folder is pinned with its trailing slash, since a folder ends with a slash by convention in Magic,
and a folder has no extension - so a pattern such as `/etc/*.md/` throws for a folder slot even though
the same wildcard is legal as a filename. An asterisk must be either an entire segment or the start of
the filename, and anything else throws rather than silently matching something unintended.

Notice, the paths a slot touches _besides_ its own value are verified too. **[io.file.copy]** and
**[io.file.move]** verify their destination, which the vocabulary never sees otherwise. **[io.file.unzip]**
verifies its destination folder once, and then confines every entry the archive writes to that folder,
which is what stops an archive escaping it with a `../` in an entry's name.

Read more about **[whitelist]** in the magic.lambda project.
