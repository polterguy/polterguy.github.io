---
title: Types and conversion
description: The [types], [type], [convert], [format] and [int2words] slots for working with Hyperlambda types, plus [vocabulary] returning every slot in your cloudlet.
moved_anchors: {"how-to-use-apply": "/plugins/magic.lambda/apply/", "how-to-use-context": "/plugins/magic.lambda/context/", "how-to-use-convert": "/plugins/magic.lambda/convert/", "how-to-use-floatarray2bytes": "/plugins/magic.lambda/floatArray2bytes/", "how-to-use-format": "/plugins/magic.lambda/format/", "how-to-use-int2words": "/plugins/magic.lambda/int2words/", "how-to-use-slotdescription": "/plugins/magic.lambda/slot.description/", "how-to-use-slotsignature": "/plugins/magic.lambda/slot.signature/", "how-to-use-sort": "/plugins/magic.lambda/sort/", "how-to-use-type": "/plugins/magic.lambda/type/", "how-to-use-types": "/plugins/magic.lambda/types-slot/", "how-to-use-vocabulary": "/plugins/magic.lambda/vocabulary/", "how-to-use-whitelist": "/plugins/magic.lambda/whitelist/"}
---

## Types and conversion

These slots allow you to inspect and convert between Hyperlambda types, in addition to
returning the vocabulary of slots your cloudlet understands, and the signature and description of each slot.

* [`types`](/plugins/magic.lambda/types-slot/) - This slot returns all Hyperlambda types your current installation supports.
* [`type`](/plugins/magic.lambda/type/) - This slot returns the Hyperlambda type name of some value.
* [`convert`](/plugins/magic.lambda/convert/) - This slot converts the value of an expression from its original type, to whatever [type] declaration you supply as its argument.
* [`floatArray2bytes`](/plugins/magic.lambda/floatArray2bytes/) - This slot serializes a sequence of float values into raw bytes, which is useful when you need to feed vectors, such as embeddings, into binary APIs.
* [`format`](/plugins/magic.lambda/format/) - This slot converts some expression or value according to some specified String.Format pattern.
* [`int2words`](/plugins/magic.lambda/int2words/) - This slot takes a signed 64 bit integer and converts it to its word representation, such as for instance 1200050 becoming "one million two hundred thousand and fifty".
* [`vocabulary`](/plugins/magic.lambda/vocabulary/) - Returns the name of every static slot in your system, optionally passing in a string, or an expression leading to a string, which is a filtering condition, where the slot must start with the filter sp
* [`slot.signature`](/plugins/magic.lambda/slot.signature/) - Returns the documented input and output contract of a single compiled slot, given its name as the value of the slot, or an expression leading to its name.
* [`slot.description`](/plugins/magic.lambda/slot.description/) - Returns the description of a single compiled slot, given its name as the value of the slot, or an expression leading to its name.
* [`whitelist`](/plugins/magic.lambda/whitelist/) - This slot temporarily within the given scope changes the available slots, allowing you to declare a block of lambda, where only a sub-set of your vocabulary is available for some piece of code to invo

### Pinning arguments in your [vocabulary]

A **[vocabulary]** entry can optionally declare a _value_, which pins the slot to that exact argument.
An entry without a value allows the slot with any argument, exactly as above, while an entry with a
value only allows the slot when its argument matches.

```
.result
whitelist

   vocabulary
      data.connect:chinook
      data.read
      return-nodes

   .lambda

      // Legal, since the vocabulary pins [data.connect] to exactly this database.
      data.connect:chinook
         data.read
            table:Artist
            limit:5
         return-nodes:x:@data.read/*
```

With the above vocabulary, `data.connect:northwind` throws, because the argument does not match the
pin. Repeat the same slot name with different values to allow more than one argument. This is how you
confine a piece of untrusted Hyperlambda to one specific database, one specific URL, or one specific
dynamic slot, instead of merely to the _name_ of a slot.

Notice, dynamic slots are pinned the same way, through the slot that invokes them.

```
vocabulary
   signal:accounting.report
   signal:hr.hire
```

The above allows the caller to invoke those two dynamic slots, and no others.

Files are pinned the same way, through **[execute-file]** and **[io.file.execute]**, which lets you admit
a specific Hyperlambda file instead of the slots it uses.

```
vocabulary
   execute-file:/modules/reports/top-customers.hl
   io.file.execute:/modules/reports/top-customers.hl
   io.file.load:/modules/reports/top-customers.hl
```

The statements inside an admitted file, or inside an admitted dynamic slot, are not restricted by the
whitelist, so the file can invoke slots that the caller itself cannot. This lets you expose complex business
logic to untrusted code without exposing the raw resources it works on, as long as you trust the file, and the
file validates the arguments it is given. The **[io.file.load]** line is optional, and allows the caller to
read the file's source. Read more in the
[Sandbox API generator](/dashboard/endpoint-generator/#business-logic-without-raw-access).

### Wildcards in pinned arguments

A pin ending with an asterisk matches any argument _starting_ with the rest of the pin. Anything
without an asterisk is an exact comparison, such that existing vocabularies keep behaving as before.

```
vocabulary
   data.connect:test-*
   http.post:"https://api.example.com/v3/*"
```

File and folder slots interpret their argument as a _path_, and compare it segment by segment, which
confines a wildcard to the segment it occurs in, the same way a wildcard is confined in a shell.

* __/etc/*__ - Every file directly in the folder, but _not_ in its sub folders
* __/etc/*.md__ - Every markdown file directly in the folder
* __/etc/*.tar.gz__ - Multi part extensions work the same way
* __/etc/\*/config.json__ - That filename, one folder level below

A folder ends with a slash by convention in Magic, hence a folder is pinned with its trailing slash.

```
vocabulary
   io.file.load:/etc/*.md
   io.folder.create:/etc/*/
```

An asterisk must be either an entire segment, or the start of the _filename_. Anything else throws,
rather than silently matching something its author did not intend - such as `/etc/f*o.md`, or an
extension on a folder segment such as `/etc/foo.*/howdy/*`. A folder has no extension, so `/etc/*.md/`
throws for a folder slot even though the same wildcard is legal as a filename.

Notice, a slot that reads a file on your behalf does so _through_ the file slot, and is therefore
subject to the same pins. Attaching a file to an email with **[mail.smtp.send]**, hashing a file with
**[crypto.hash]**, uploading one with **[http.post]**, or resizing an image, all require the relevant
**[io.stream.open-file]** or **[io.stream.save-file]** pin in addition to the slot itself.

* [`context`](/plugins/magic.lambda/context/) - This slot allows you to add an object unto the stack, such that it can later be retrieved with the [get-context] slot.
* [`apply`](/plugins/magic.lambda/apply/) - This slot takes an expression in addition to a list of arguments, and "applies" the arguments unto the expression's result node set, allowing you to perform dynamic substitutions on lambda hierarchies
* [`sort`](/plugins/magic.lambda/sort/) - Sort takes an expression leading to a list of nodes, in addition to a lambda object.
