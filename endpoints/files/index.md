---
title: File system endpoints
description: Magic's built-in file system endpoints; uploading, downloading, listing, renaming and deleting files and folders.
header:
  image: /assets/images/hero/endpoints-top.png
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: File system endpoints
---

## File system related endpoints

These endpoints are related to the file system somehow and allow you to upload and download files,
create and delete folders, etc. These endpoints are arguably the foundation of Hyper IDE,
allowing you to edit your files on your server. Most of these endpoints can only be invoked by a root user, and
you would typically not consume these endpoints yourself directly from your own code.

### GET magic/system/file-system/download-folder

This endpoint allows the caller to download the specified folder from the backend as a ZIP file. The
endpoint can only be invoked by a root account, and requires the caller to specify **[folder]** being
an existing folder in the Magic backend. The endpoint requires the following query argument(s).

* __[folder]__ - Relative path of which folder to zip and download to the client

This endpoint is not intended for you to consume in your own code.

### DELETE magic/system/file-system/file

This endpoint deletes the specified **[file]** in the backend. The endpoint can only be invoked by a
root user. The endpoint requires the following query argument(s).

* __[file]__ - Full relative path of which file to delete

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/file

This endpoint returns the specified **[file]** to the caller. The endpoint can only be invoked by
a root user. The endpoint requires the following query argument(s).

* __[file]__ - Full relative path of file to download

This endpoint is not intended for you to consume in your own code.

### PUT magic/system/file-system/file

This endpoint creates or updates an existing file on the server. The endpoint requires its payload
as `multipart/form-data`, where **[folder]** becomes the folder of where to save the file,
and the attached **[file]** becomes the file to save, assuming the file has a name specified
as a part of its MIME entity as its Content-Disposition header's `filename`. The endpoint
can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### DELETE magic/system/file-system/folder

This endpoint deletes the specified **[folder]** in your backend. The endpoint can only be
invoked by a root user. The endpoint requires the following query argument(s).

* __[folder]__ - Full relative path of folder to delete

This endpoint is not intended for you to consume in your own code.

### PUT magic/system/file-system/folder

This endpoint creates a new folder in your backend given the specified payload.

```
{
  "folder": "/foo/bar/"
}
```

The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/list-folders-recursively

This endpoint lists all folders recursively starting from the specified **[folder]** argument.
The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[folder]__ - Root folder of where to start listing folders. Will return all folders existing within this folder to caller
* __[sys]__ - If true, folders inside system folders are included in the result

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/list-files-recursively

This endpoint returns all files recursively from within the specified **[folder]** folder.
The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[folder]__ - Root folder of where to start listing files. Will return all files existing within this folder to caller
* __[sys]__ - If true, files inside system folders are included in the result

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/list-files

This endpoint lists all files within the specified **[folder]** folder, optionally containing
the specified **[filter]** criteria. The endpoint can only be invoked by a root user. The endpoint
requires the following argument(s).

* __[folder]__ - Folder to list files within
* __[filter]__ - Optional filter criteria filenames must contain in order to be considered a match

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/list-folders

This endpoint lists all folders within the specified **[folder]** folder. The endpoint
can only be invoked by a root user. The endpoint requires the following argument(s).

* __[folder]__ - Folder to list folder within

This endpoint is not intended for you to consume in your own code.

### POST magic/system/file-system/rename

This endpoint renames a file or a folder. It requires the following payload.

```
{
  "oldName": "xxx",
  "newName": "yyy"
}
```

Notice, the endpoint can rename both files or folders, but can only be invoked by a root user.
The **[oldName]** is the _full path_ of the file's or folder's _current_ name. The **[newName]**
is its new full name or path.

This endpoint is not intended for you to consume in your own code.

### PUT magic/system/file-system/unzip

This endpoint unzips the specified **[file]** ZIP file in place. The endpoint requires the
following payload.

```
{
  "file": "/foo/bar.zip",
  "create_folder": false
}
```

The **[create_folder]** argument is optional, and if true, the ZIP file is unzipped into a new folder named after the ZIP file itself.

The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### PUT magic/system/file-system/install-module

This endpoint uploads a ZIP file assumed to be a module, and installs it in your backend. The endpoint
requires its payload as `multipart/form-data`, with the attached **[file]** being the ZIP file to install.
The module is unzipped into your modules folder, and its startup files are executed, initialising the module.

The endpoint can only be invoked by a root user, and is not intended for you to consume in your own code.
