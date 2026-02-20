---
title: magic.lambda.puppeteer
---

The magic.lambda.puppeteer project provides headless Chromium automation slots for Magic using PuppeteerSharp.
It uses an explicit session model: **[puppeteer.connect]** returns a `session_id`, and every other slot requires
that `session_id`. There is no scoped context or `.lambda` usage.

**Thread safety**: This library is **not thread safe**. Do not use the same `session_id` concurrently across threads.

Sessions use sliding expiration. By default they expire after 15 minutes of inactivity, and are always closed after
2 hours total lifetime. A maximum of **5** concurrent sessions is allowed globally per cloudlet.

## [puppeteer.connect]

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

## [puppeteer.close]

Closes the browser and page associated with a session.

Arguments:

* Slot value - Session identifier returned by **[puppeteer.connect]**.

Examples:

```
puppeteer.close:SESSION_ID
```

## [puppeteer.goto]

Navigates to a URL.

Arguments:

* Slot value - Session identifier.
* `url` - URL to navigate to.
* `timeout` - Navigation timeout in milliseconds.
* `wait-until` - One of `load`, `domcontentloaded`, `networkidle0`, `networkidle2`.

Examples:

```
puppeteer.goto:SESSION_ID
   url:"https://ainiro.io"
```

```
puppeteer.goto:SESSION_ID
   url:"https://ainiro.io"
   timeout:30000
   wait-until:networkidle2
```

## [puppeteer.wait-for-url]

Waits until the page URL matches.

Arguments:

* Slot value - Session identifier.
* `url` - URL string to wait for.
* `timeout` - Timeout in milliseconds.

Examples:

```
puppeteer.wait-for-url:SESSION_ID
   url:"https://ainiro.io/contact-us"
```

## [puppeteer.wait-for-selector]

Waits until a selector appears in the DOM.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to wait for.
* `timeout` - Timeout in milliseconds.
* `visible` - Boolean. Require element to be visible.
* `hidden` - Boolean. Require element to be hidden.

Examples:

```
puppeteer.wait-for-selector:SESSION_ID
   selector:"#name"
   visible:true
```

## [puppeteer.click]

Clicks a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to click.
* `button` - Mouse button: `left`, `middle`, or `right`.
* `click-count` - Number of clicks.
* `delay` - Delay between down and up in milliseconds.

Examples:

```
puppeteer.click:SESSION_ID
   selector:"#submit_contact_form_button"
```

```
puppeteer.click:SESSION_ID
   selector:"#submit_contact_form_button"
   click-count:2
```

## [puppeteer.type]

Types text into a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to type into.
* `text` - Text to type.
* `delay` - Delay between key presses in milliseconds.

Examples:

```
puppeteer.type:SESSION_ID
   selector:"#name"
   text:"Thomas Hansen"
```

```
puppeteer.type:SESSION_ID
   selector:"#info"
   text:"Hello from AI agent"
   delay:25
```

## [puppeteer.fill]

Clears and types text into a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to fill.
* `text` - Text to type after clearing.
* `delay` - Delay between key presses in milliseconds.

Examples:

```
puppeteer.fill:SESSION_ID
   selector:"#email"
   text:"thomas@gaiasoul.com"
```

## [puppeteer.press]

Presses a key on a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to focus.
* `key` - Key name (for example `Enter`).
* `delay` - Delay in milliseconds.

Examples:

```
puppeteer.press:SESSION_ID
   selector:"#submit_contact_form_button"
   key:Enter
```

## [puppeteer.select]

Selects option values from a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector for a `<select>` element.
* `values` - Values to select. Provide as children or a comma-separated string.

Examples:

```
puppeteer.select:SESSION_ID
   selector:"#plan"
   values
      .:basic
      .:pro
```

## [puppeteer.content]

Returns page HTML.

Arguments:

* Slot value - Session identifier.

Examples:

```
puppeteer.content:SESSION_ID
```

## [puppeteer.title]

Returns page title.

Arguments:

* Slot value - Session identifier.

Examples:

```
puppeteer.title:SESSION_ID
```

## [puppeteer.url]

Returns current URL.

Arguments:

* Slot value - Session identifier.

Examples:

```
puppeteer.url:SESSION_ID
```

## [puppeteer.screenshot]

Saves a screenshot to disk.

Arguments:

* Slot value - Session identifier.
* `filename` - Output file path.
* `full-page` - Boolean. Capture full scrollable page.
* `type` - `png` or `jpeg`.
* `quality` - JPEG quality 0-100 (only for `jpeg`).

Examples:

```
puppeteer.screenshot:SESSION_ID
   filename:"/etc/tmp/example.png"
   full-page:true
```

```
puppeteer.screenshot:SESSION_ID
   filename:"/etc/tmp/example.jpg"
   type:jpeg
   quality:85
```

## [puppeteer.evaluate]

Evaluates a JavaScript expression in the page.

Arguments:

* Slot value - Session identifier.
* `expression` - JavaScript expression string.
* `args` - Optional arguments for JS function invocation. Each child value is one argument.

Examples:

```
puppeteer.evaluate:SESSION_ID
   expression:"document.title"
```

```
puppeteer.evaluate:SESSION_ID
   expression:"typeof window.mcaptcha"
```

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
