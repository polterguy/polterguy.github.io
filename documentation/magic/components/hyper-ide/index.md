---
title: Hyper IDE, a web based IDE
description: Hyper IDE is a fully fledged integrated development environment, giving you most important features from other IDEs. Hyper IDE works perfectly on your phone, tablet, computer, or any other device you might have access to with a browser.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg"
---

# The Hyper IDE component

Hyper IDE is your _"goto component"_ when you want to create your own modules using Magic and Hyperlambda.
It's a fully fledged web based IDE or Integrated Development Environment, allowing you to edit your code,
create new modules, and contains most things you're used to from a traditional IDE.

![Editing a file in Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-hyper-ide-2.jpg)

Hyper IDE also provides integrated autocomplete if your editor has focus and you click CTRL+SPACE
in Windows or FN+CONTROL+SPACE on your Mac. This allows you to very rapidly create Hyperlambda code,
while having Hyper IDE ensure your code is using existing slots. Click the _"Shortkeys"_ button to see
a list of all keyboard shortcuts Hyper IDE provides. Notice, these keyboard shortcuts are only available
when your code editor has focus. You can also create files and folders, and upload files to your server
through the action buttons drop down menu.

![Hyper IDE autocomplete](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-actions.jpg)

## Invoking endpoints from Hyper IDE

Hyper IDE allows you to invoke your HTTP endpoints without ever leaving your IDE. This makes it easy for
you to test your code as you are creating it. If you are editing an HTTP endpoint Hyperlambda file, you can click F5,
resulting in something resembling the following.

![Invoking HTTP endpoints from Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-blog.jpg)

For more details about invoking your HTTP endpoints refer to the [endpoints component](/documentation/magic/components/endpoints/).
This component also allows you to automatically generate health check tests, sanity checking your system as you're editing its code.

## Hyper IDE macros

Hyper IDE supports _"macros"_. A macro is an automated
process that somehow creates code, and/or modifies your existing code, 100% automatically. There exists
several macros in Hyper IDE solving everything from automatically documenting your module, to creating file
upload endpoints for you. To execute a macro, first select which module you want to run it for, then click
the macro action button, and parametrise your macro.

![Hyper IDE macros](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/execute-macro.jpg)

