---
title: magic.lambda.puppeteer slot reference
description: Every slot in magic.lambda.puppeteer with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.puppeteer](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.puppeteer). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.puppeteer](/plugins/magic.lambda.puppeteer/)._

## [puppeteer.click]

Clicks an element on the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector |
| `[button]` | string | no | Mouse button to click |
| `[click-count]` | int | no | Number of clicks |
| `[delay]` | int | no | Delay in milliseconds between mouse down and up |

Guide: [How to use [puppeteer.click]](/plugins/magic.lambda.puppeteer/#puppeteerclick)

## [puppeteer.close]

Closes a Puppeteer session.

* **Value** (`puppeteer-session`), required: Puppeteer session ID

Guide: [How to use [puppeteer.close]](/plugins/magic.lambda.puppeteer/#puppeteerclose)

## [puppeteer.connect]

Creates or reuses a Puppeteer browser session.

* **Returns**: Resolves to the created Puppeteer session ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[timeout-minutes]` | int | no | Idle timeout in minutes |
| `[max-lifetime-minutes]` | int | no | Maximum session lifetime in minutes |
| `[headless]` | bool | no | Whether the browser should run headless |
| `[timeout]` | int | no | Browser launch timeout in milliseconds |
| `[user-data-dir]` | string | no | Browser user data directory |
| `[executable]` | string | no | Browser executable path |

Guide: [How to use [puppeteer.connect]](/plugins/magic.lambda.puppeteer/#puppeteerconnect)

## [puppeteer.content]

Returns the current page HTML content.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page HTML content

Guide: [How to use [puppeteer.content]](/plugins/magic.lambda.puppeteer/#puppeteercontent)

## [puppeteer.evaluate]

Evaluates JavaScript in the page context.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the result of the evaluated JavaScript expression

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expression]` | string | yes | JavaScript expression or function |

Guide: [How to use [puppeteer.evaluate]](/plugins/magic.lambda.puppeteer/#puppeteerevaluate)

## [puppeteer.fill]

Fills an input element with text.

* **Value** (`puppeteer-session`), required: Puppeteer session ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector |
| `[text]` | string | no | Text to send |
| `[config-key]` | string | no | Configuration key resolving the text to send |
| `[delay]` | int | no | Delay in milliseconds between key presses |

Guide: [How to use [puppeteer.fill]](/plugins/magic.lambda.puppeteer/#puppeteerfill)

## [puppeteer.goto]

Navigates the current page to a URL.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the resolved page URL after navigation

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | yes | URL to navigate to |
| `[timeout]` | int | no | Navigation timeout in milliseconds |
| `[wait-until]` | string | no | Navigation completion condition: load, domcontentloaded, networkidle0, or networkidle2 |

Guide: [How to use [puppeteer.goto]](/plugins/magic.lambda.puppeteer/#puppeteergoto)

## [puppeteer.press]

Sends a key press to the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector |
| `[key]` | string | no | Key to press |
| `[delay]` | int | no | Delay in milliseconds between key down and up |

Guide: [How to use [puppeteer.press]](/plugins/magic.lambda.puppeteer/#puppeteerpress)

## [puppeteer.screenshot]

Captures a screenshot of the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the screenshot image bytes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | yes | Destination filename |
| `[full-page]` | bool | no | Whether to capture the full page |
| `[type]` | string | no | Image type |
| `[quality]` | int | no | JPEG/WebP image quality |

Guide: [How to use [puppeteer.screenshot]](/plugins/magic.lambda.puppeteer/#puppeteerscreenshot)

## [puppeteer.select]

Selects an option in a select element.

* **Value** (`puppeteer-session`), required: Puppeteer session ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector |

Guide: [How to use [puppeteer.select]](/plugins/magic.lambda.puppeteer/#puppeteerselect)

## [puppeteer.title]

Returns the current page title.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page title

Guide: [How to use [puppeteer.title]](/plugins/magic.lambda.puppeteer/#puppeteertitle)

## [puppeteer.type]

Types text into an element.

* **Value** (`puppeteer-session`), required: Puppeteer session ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector |
| `[text]` | string | no | Text to send |
| `[config-key]` | string | no | Configuration key resolving the text to send |
| `[delay]` | int | no | Delay in milliseconds between key presses |

Guide: [How to use [puppeteer.type]](/plugins/magic.lambda.puppeteer/#puppeteertype)

## [puppeteer.url]

Returns the current page URL.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page URL

Guide: [How to use [puppeteer.url]](/plugins/magic.lambda.puppeteer/#puppeteerurl)

## [puppeteer.wait-for-selector]

Waits for a selector to appear.

* **Value** (`puppeteer-session`), required: Puppeteer session ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector |
| `[timeout]` | int | no | Wait timeout in milliseconds |
| `[visible]` | bool | no | Wait until selector is visible |
| `[hidden]` | bool | no | Wait until selector is hidden |

Guide: [How to use [puppeteer.wait-for-selector]](/plugins/magic.lambda.puppeteer/#puppeteerwait-for-selector)

## [puppeteer.wait-for-url]

Waits for the page URL to match a condition.

* **Value** (`puppeteer-session`), required: Puppeteer session ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | yes | URL pattern to wait for |
| `[timeout]` | int | no | Wait timeout in milliseconds |

Guide: [How to use [puppeteer.wait-for-url]](/plugins/magic.lambda.puppeteer/#puppeteerwait-for-url)

