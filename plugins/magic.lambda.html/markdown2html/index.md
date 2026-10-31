---
title: "How to use [markdown2html]"
description: "How to use [markdown2html] - This library can also handle Markdown, since Markdown is arguably just another representation of HTML."
generated: true
guide: true
---

This is the guide to [`markdown2html`](/reference/slots/core/markdown2html/), whose reference page has its arguments, constraints and declaration.

This library can also handle Markdown, since Markdown is arguably just another representation of HTML.
The **[markdown2html]** slot converts the specified Markdown content to HTML. Basic usage is as follows.

```
.yaml:@"
Howdy world

* Foo
* Bar
"
markdown2html:x:@.yaml
```

The above will produce the following result.

```html
markdown2html:@"<p>Howdy world</p>
<ul>
<li>Foo</li>
<li>Bar</li>
</ul>
```
