---
title: puppeteer.* slots
description: The 15 slots named puppeteer.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [puppeteer.click]

Clicks an element on the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[button]` | string | no | Mouse button to click. Default: `left`. |
| `[click-count]` | int | no | Number of clicks. |
| `[delay]` | int | no | Delay in milliseconds between mouse down and up. |

Guide: [How to use [puppeteer.click]](/plugins/magic.lambda.puppeteer/#puppeteerclick)

## [puppeteer.close]

Closes a Puppeteer session.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

Guide: [How to use [puppeteer.close]](/plugins/magic.lambda.puppeteer/#puppeteerclose)

## [puppeteer.connect]

Creates or reuses a Puppeteer browser session.

* **Returns**: Resolves to the created Puppeteer session ID
* **Scope**: provides `puppeteer-session` - Creates an open Puppeteer browser session scope for puppeteer.* slots

| Argument | Type | Required | Description |
|---|---|---|---|
| `[timeout-minutes]` | int | no | Idle timeout in minutes. |
| `[max-lifetime-minutes]` | int | no | Maximum session lifetime in minutes. |
| `[headless]` | bool | no | Whether the browser should run headless. Default: `true`. |
| `[timeout]` | int | no | Browser launch timeout in milliseconds. |
| `[args]` | string\|lambda | no | Browser launch arguments. |
| `[args]` / _unnamed child node_ | string | no | Argument value. Can be repeated. |
| `[user-data-dir]` | string | no | Browser user data directory. |
| `[executable]` | string | no | Browser executable path. |
| `[executable-path]` | string | no | Browser executable path. |

* **Constraint** (AtMostOneOf): [executable] and [executable-path] are aliases; supply at most one (`[executable]`, `[executable-path]`)

Guide: [How to use [puppeteer.connect]](/plugins/magic.lambda.puppeteer/#puppeteerconnect)

## [puppeteer.content]

Returns the current page HTML content.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page HTML content
* **Scope**: requires `puppeteer-session`

Guide: [How to use [puppeteer.content]](/plugins/magic.lambda.puppeteer/#puppeteercontent)

## [puppeteer.evaluate]

Evaluates JavaScript in the page context.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the result of the evaluated JavaScript expression
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expression]` | string | yes | JavaScript expression or function. |
| `[args]` | string\|lambda | no | Arguments passed to the JavaScript function. |
| `[args]` / _unnamed child node_ | string | no | Argument value. Can be repeated. |

Guide: [How to use [puppeteer.evaluate]](/plugins/magic.lambda.puppeteer/#puppeteerevaluate)

## [puppeteer.fill]

Fills an input element with text.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[text]` | string | no | Text to send. |
| `[config-key]` | string | no | Configuration key resolving the text to send. |
| `[delay]` | int | no | Delay in milliseconds between key presses. |

* **Constraint** (ExactlyOneOf): Provide either [text] or [config-key] (`[text]`, `[config-key]`)

Guide: [How to use [puppeteer.fill]](/plugins/magic.lambda.puppeteer/#puppeteerfill)

## [puppeteer.goto]

Navigates the current page to a URL.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the resolved page URL after navigation
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | yes | URL to navigate to. |
| `[timeout]` | int | no | Navigation timeout in milliseconds. |
| `[wait-until]` | string | no | Navigation completion condition: load, domcontentloaded, networkidle0, or networkidle2. |

Guide: [How to use [puppeteer.goto]](/plugins/magic.lambda.puppeteer/#puppeteergoto)

## [puppeteer.press]

Sends a key press to the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[key]` | string | no | Key to press. |
| `[delay]` | int | no | Delay in milliseconds between key down and up. |

Guide: [How to use [puppeteer.press]](/plugins/magic.lambda.puppeteer/#puppeteerpress)

## [puppeteer.screenshot]

Captures a screenshot of the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the screenshot image bytes
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | yes | Destination filename. |
| `[full-page]` | bool | no | Whether to capture the full page. Default: `false`. |
| `[type]` | string | no | Image type. |
| `[quality]` | int | no | JPEG/WebP image quality. |

Guide: [How to use [puppeteer.screenshot]](/plugins/magic.lambda.puppeteer/#puppeteerscreenshot)

## [puppeteer.select]

Selects an option in a select element.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[values]` | string\|lambda | no | Option values to select. |
| `[values]` / _unnamed child node_ | string | no | Argument value. Can be repeated. |

Guide: [How to use [puppeteer.select]](/plugins/magic.lambda.puppeteer/#puppeteerselect)

## [puppeteer.title]

Returns the current page title.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page title
* **Scope**: requires `puppeteer-session`

Guide: [How to use [puppeteer.title]](/plugins/magic.lambda.puppeteer/#puppeteertitle)

## [puppeteer.type]

Types text into an element.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[text]` | string | no | Text to send. |
| `[config-key]` | string | no | Configuration key resolving the text to send. |
| `[delay]` | int | no | Delay in milliseconds between key presses. |

* **Constraint** (ExactlyOneOf): Provide either [text] or [config-key] (`[text]`, `[config-key]`)

Guide: [How to use [puppeteer.type]](/plugins/magic.lambda.puppeteer/#puppeteertype)

## [puppeteer.url]

Returns the current page URL.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page URL
* **Scope**: requires `puppeteer-session`

Guide: [How to use [puppeteer.url]](/plugins/magic.lambda.puppeteer/#puppeteerurl)

## [puppeteer.wait-for-selector]

Waits for a selector to appear.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[timeout]` | int | no | Wait timeout in milliseconds. |
| `[visible]` | bool | no | Wait until selector is visible. |
| `[hidden]` | bool | no | Wait until selector is hidden. |

Guide: [How to use [puppeteer.wait-for-selector]](/plugins/magic.lambda.puppeteer/#puppeteerwait-for-selector)

## [puppeteer.wait-for-url]

Waits for the page URL to match a condition.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | yes | URL pattern to wait for. |
| `[timeout]` | int | no | Wait timeout in milliseconds. |

Guide: [How to use [puppeteer.wait-for-url]](/plugins/magic.lambda.puppeteer/#puppeteerwait-for-url)

