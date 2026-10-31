---
title: magic.lambda.io
moved_anchors: {"how-to-use-execute-file": "/reference/slots/core/execute-file/#guide", "how-to-use-iocontentzip-stream": "/reference/slots/io/io.content.zip-stream/#guide", "how-to-use-iofilecopy": "/reference/slots/io/io.file.copy/#guide", "how-to-use-iofiledelete": "/reference/slots/io/io.file.delete/#guide", "how-to-use-iofileexecute": "/reference/slots/io/io.file.execute/#guide", "how-to-use-iofileexists": "/reference/slots/io/io.file.exists/#guide", "how-to-use-iofilelist": "/reference/slots/io/io.file.list/#guide", "how-to-use-iofilelist-recursively": "/reference/slots/io/io.file.list-recursively/#guide", "how-to-use-iofileload": "/reference/slots/io/io.file.load/#guide", "how-to-use-iofileload-recursively": "/reference/slots/io/io.file.load-recursively/#guide", "how-to-use-iofilemixin": "/reference/slots/io/io.file.mixin/#guide", "how-to-use-iofilemove": "/reference/slots/io/io.file.move/#guide", "how-to-use-iofilepatch": "/reference/slots/io/io.file.patch/#guide", "how-to-use-iofilesave": "/reference/slots/io/io.file.save/#guide", "how-to-use-iofilesearch": "/reference/slots/io/io.file.search/#guide", "how-to-use-iofileunzip": "/reference/slots/io/io.file.unzip/#guide", "how-to-use-iofoldercopy": "/reference/slots/io/io.folder.copy/#guide", "how-to-use-iofoldercreate": "/reference/slots/io/io.folder.create/#guide", "how-to-use-iofolderdelete": "/reference/slots/io/io.folder.delete/#guide", "how-to-use-iofolderexists": "/reference/slots/io/io.folder.exists/#guide", "how-to-use-iofolderlist": "/reference/slots/io/io.folder.list/#guide", "how-to-use-iofolderlist-recursively": "/reference/slots/io/io.folder.list-recursively/#guide", "how-to-use-iofoldermove": "/reference/slots/io/io.folder.move/#guide", "how-to-use-iopathget-folder": "/reference/slots/io/io.path.get-folder/#guide", "how-to-use-iostreamclose": "/reference/slots/io/io.stream.close/#guide", "how-to-use-iostreamopen-file": "/reference/slots/io/io.stream.open-file/#guide", "how-to-use-iostreamread": "/reference/slots/io/io.stream.read/#guide", "how-to-use-iostreamsave-file": "/reference/slots/io/io.stream.save-file/#guide"}
---

This project provides file/folder slots for Magic. More specifically, it provides the following slots.

* __[\[io.folder.create\]](/reference/slots/io/io.folder.create/)__ - Creates a folder on disc for you on your server
* __[\[io.folder.exists\]](/reference/slots/io/io.folder.exists/)__ - Returns true if folder exists, otherwise false
* __[\[io.folder.delete\]](/reference/slots/io/io.folder.delete/)__ - Deletes a folder on disc on your server
* __[\[io.folder.list\]](/reference/slots/io/io.folder.list/)__ - Lists all folders within another source folder
* __[\[io.folder.list-recursively\]](/reference/slots/io/io.folder.list-recursively/)__ - Lists all folders within another source folder, including all nested folders
* __[\[io.folder.move\]](/reference/slots/io/io.folder.move/)__ - Moves a folder to its specified destination
* __[\[io.folder.copy\]](/reference/slots/io/io.folder.copy/)__ - Copies a folder to its specified destination
* __[\[io.file.load\]](/reference/slots/io/io.file.load/)__ - Loads a file from disc on your server
* __[\[load-file\]](/reference/slots/core/load-file/)__ - Alias for **[io.file.load]**
* __[\[io.file.load-recursively\]](/reference/slots/io/io.file.load-recursively/)__ - Loads all files in a folder, including all nested folders, returning each file's name and content
* __[\[io.file.load.binary\]](/reference/slots/io/io.file.load.binary/)__ - Loads a file from disc on your server as a byte array
* __[\[io.file.save\]](/reference/slots/io/io.file.save/)__ - Saves a file on disc on your server
* __[\[save-file\]](/reference/slots/core/save-file/)__ - Alias for **[io.file.save]**
* __[\[io.file.save.binary\]](/reference/slots/io/io.file.save.binary/)__ - Saves a file on disc on your server but contrary to the above assumes content to save is binary
* __[\[io.file.patch\]](/reference/slots/io/io.file.patch/)__ - Applies a unified diff patch to a file on disc on your server
* __[\[io.file.exists\]](/reference/slots/io/io.file.exists/)__ - Returns true if file exists, otherwise false.
* __[\[io.file.delete\]](/reference/slots/io/io.file.delete/)__ - Deletes a file on your server.
* __[\[io.file.copy\]](/reference/slots/io/io.file.copy/)__ - Copies a file on your server.
* __[\[io.file.execute\]](/reference/slots/io/io.file.execute/)__ - Executes a Hyperlambda file on your server.
* __[\[execute-file\]](/reference/slots/core/execute-file/)__ - Alias for **[io.file.execute]** except it will forward evaluate all descendant nodes using **[unwrap]**
* __[\[io.file.list\]](/reference/slots/io/io.file.list/)__ - List files in the specified folder on your server.
* __[\[io.file.list-recursively\]](/reference/slots/io/io.file.list-recursively/)__ - List files in the specified folder on your server, including all nested folders.
* __[\[io.file.move\]](/reference/slots/io/io.file.move/)__ - Moves a file on your server.
* __[\[io.file.unzip\]](/reference/slots/io/io.file.unzip/)__ - Unzips a file on your server.
* __[\[io.stream.open-file\]](/reference/slots/io/io.stream.open-file/)__ - Opens the specified filename and returns it as a stream
* __[\[io.stream.save-file\]](/reference/slots/io/io.stream.save-file/)__ - Saves a stream to the specified destination path
* __[\[io.stream.read\]](/reference/slots/io/io.stream.read/)__ - Reads all content from the specified stream as a byte array
* __[\[io.stream.close\]](/reference/slots/io/io.stream.close/)__ - Closes a previously opened stream
* __[\[io.content.zip-stream\]](/reference/slots/io/io.content.zip-stream/)__ - Creates a ZipStream for you, without touching the file system
* __[\[io.path.get-folder\]](/reference/slots/io/io.path.get-folder/)__ - Returns the folder part of the specified path
* __[.io.folder.root]__ - Returns the root folder of your system. (private C# slot)
* __[\[io.file.mixin\]](/reference/slots/io/io.file.mixin/)__ - Allows you to invoke lambda objects from a file and substitute content dynamically in your original file
* __[\[io.file.search\]](/reference/slots/io/io.file.search/)__ - Searches file content and returns filename + line numbers


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
