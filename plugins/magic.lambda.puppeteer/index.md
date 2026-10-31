---
title: magic.lambda.puppeteer
moved_anchors: {"puppeteerclick": "/plugins/magic.lambda.puppeteer/puppeteer.click/", "puppeteerclose": "/plugins/magic.lambda.puppeteer/puppeteer.close/", "puppeteerconnect": "/plugins/magic.lambda.puppeteer/puppeteer.connect/", "puppeteercontent": "/plugins/magic.lambda.puppeteer/puppeteer.content/", "puppeteerevaluate": "/plugins/magic.lambda.puppeteer/puppeteer.evaluate/", "puppeteerfill": "/plugins/magic.lambda.puppeteer/puppeteer.fill/", "puppeteergoto": "/plugins/magic.lambda.puppeteer/puppeteer.goto/", "puppeteerpress": "/plugins/magic.lambda.puppeteer/puppeteer.press/", "puppeteerscreenshot": "/plugins/magic.lambda.puppeteer/puppeteer.screenshot/", "puppeteerselect": "/plugins/magic.lambda.puppeteer/puppeteer.select/", "puppeteertitle": "/plugins/magic.lambda.puppeteer/puppeteer.title/", "puppeteertype": "/plugins/magic.lambda.puppeteer/puppeteer.type/", "puppeteerurl": "/plugins/magic.lambda.puppeteer/puppeteer.url/", "puppeteerwait-for-selector": "/plugins/magic.lambda.puppeteer/puppeteer.wait-for-selector/", "puppeteerwait-for-url": "/plugins/magic.lambda.puppeteer/puppeteer.wait-for-url/"}
---

The magic.lambda.puppeteer project provides headless Chromium automation slots for Magic using PuppeteerSharp.
It uses an explicit session model: **[puppeteer.connect]** returns a `session_id`, and every other slot requires
that `session_id`. There is no scoped context or `.lambda` usage.

**Thread safety**: This library is **not thread safe**. Do not use the same `session_id` concurrently across threads.

Sessions use sliding expiration. By default they expire after 15 minutes of inactivity, and are always closed after
2 hours total lifetime. A maximum of **5** concurrent sessions is allowed globally per cloudlet.


## Combination examples

Get title and URL from a page, then close the session.

```
.session_id
set-value:x:@.session_id
   puppeteer.connect

puppeteer.goto:x:@.session_id
   url:"https://ainiro.io"

puppeteer.title:x:@.session_id
puppeteer.url:x:@.session_id

puppeteer.close:x:@.session_id
```

Fetch page HTML and save a screenshot.

```
.session_id
set-value:x:@.session_id
   puppeteer.connect

puppeteer.goto:x:@.session_id
   url:"https://ainiro.io/contact-us"

puppeteer.content:x:@.session_id
puppeteer.screenshot:x:@.session_id
   filename:"/etc/tmp/ainiro-contact.png"
   full-page:true

puppeteer.close:x:@.session_id
```
