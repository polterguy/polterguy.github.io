---
title: "How to use [puppeteer.connect]"
description: "How to use [puppeteer.connect] - Launches Chromium, opens a page, and returns a sessionid."
generated: true
guide: true
---

The reference page of [`puppeteer.connect`](/reference/slots/puppeteer/puppeteer.connect/) has its arguments, constraints and declaration.

Launches Chromium, opens a page, and returns a `session_id`.

Arguments:

* `headless` - Boolean. Launch Chromium in headless mode. Defaults to true.
* `executable` - Full path to Chromium/Chrome binary.
* `executable-path` - Alias for `executable`.
* `timeout` - Launch timeout in milliseconds.
* `user-data-dir` - Directory for Chromium user data.
* `args` - Additional Chromium arguments. Each child value is one argument string.
* `timeout-minutes` - Sliding inactivity timeout in minutes. Defaults to 15.
* `max-lifetime-minutes` - Maximum session lifetime in minutes. Defaults to 120.

Examples:

```
puppeteer.connect
```

```
puppeteer.connect
   headless:true
   executable:"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
   timeout:30000
   args
      .:--no-sandbox
      .:--disable-dev-shm-usage
   timeout-minutes:30
   max-lifetime-minutes:120
```
