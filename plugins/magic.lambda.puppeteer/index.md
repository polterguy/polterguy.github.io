---
title: magic.lambda.puppeteer
moved_anchors: {"puppeteerclick": "/reference/slots/puppeteer/puppeteer.click/#guide", "puppeteerclose": "/reference/slots/puppeteer/puppeteer.close/#guide", "puppeteerconnect": "/reference/slots/puppeteer/puppeteer.connect/#guide", "puppeteercontent": "/reference/slots/puppeteer/puppeteer.content/#guide", "puppeteerevaluate": "/reference/slots/puppeteer/puppeteer.evaluate/#guide", "puppeteerfill": "/reference/slots/puppeteer/puppeteer.fill/#guide", "puppeteergoto": "/reference/slots/puppeteer/puppeteer.goto/#guide", "puppeteerpress": "/reference/slots/puppeteer/puppeteer.press/#guide", "puppeteerscreenshot": "/reference/slots/puppeteer/puppeteer.screenshot/#guide", "puppeteerselect": "/reference/slots/puppeteer/puppeteer.select/#guide", "puppeteertitle": "/reference/slots/puppeteer/puppeteer.title/#guide", "puppeteertype": "/reference/slots/puppeteer/puppeteer.type/#guide", "puppeteerurl": "/reference/slots/puppeteer/puppeteer.url/#guide", "puppeteerwait-for-selector": "/reference/slots/puppeteer/puppeteer.wait-for-selector/#guide", "puppeteerwait-for-url": "/reference/slots/puppeteer/puppeteer.wait-for-url/#guide"}
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
