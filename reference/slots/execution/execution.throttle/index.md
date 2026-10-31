---
title: "[execution.throttle]"
description: "execution.throttle is a slot in the execution namespace of Magic Cloud. Enforces a named throttle previously declared with [execution.throttle.create], throwing a 429 exception once the limit is exceeded."
generated: true
llms: "guide"
slot_json: "/reference/slots/execution/execution.throttle/slot.json"
---

`execution.throttle` is a slot in the `execution` namespace, in Hyperlambda, the language of Magic Cloud. Enforces a named throttle previously declared with [execution.throttle.create], throwing a 429 exception once the limit is exceeded.

* **Value** (`throttle-name`), required: Name of the throttle to enforce, as previously declared with [execution.throttle.create]

### Guide

<!-- guide -->
Rate limiting is split into two slots; **[execution.throttle.create]** _declares_ a named throttle,
being the single source of truth for its configuration, while **[execution.throttle]** _enforces_ it,
throwing an exception with a 429 status code once the limit is exceeded. Declaring a throttle whose
configuration is unchanged is a no-op that keeps the existing counters, implying you can safely
declare a throttle directly at the top of your endpoint file, immediately before enforcing it.

```
// At the top of your endpoint file, allowing 10 invocations per user per minute.
execution.throttle.create:my-endpoint
   limit:10
execution.throttle:my-endpoint
```

For a throttle shared between multiple endpoints you typically declare it once in a file inside
your module's _"magic.startup"_ folder instead, ensuring it exists when your module loads, and
enforce it with a single line of code in each endpoint sharing the budget.

```
// In your module's magic.startup folder.
execution.throttle.create:openai-budget
   limit:100
   window:3600
   per:global
```

```
// At the top of every endpoint sharing the above budget.
execution.throttle:openai-budget
```

The name is the identity of your throttle, and works the same way as the name of a **[semaphore]** -
all **[execution.throttle]** invocations using the same name share _one_ rate limit, allowing you to
enforce the same throttle in multiple endpoints to give a group of endpoints a shared budget, or use
a unique name per endpoint to rate limit each endpoint individually.

Psst, to create a unique name you can copy the endpoint filename and use it as name.

**[execution.throttle.create]** takes the following arguments.

* __[limit]__ - Maximum number of invocations allowed per window, mandatory when creating
* __[window]__ - Window length in seconds, defaults to 60
* __[per]__ - How to partition the limit, being one of _'user'_, _'ip'_ or _'global'_

**[per]** being _'user'_ counts invocations per authenticated username, and throws a 401 exception
for anonymous callers. _'ip'_ counts per client IP address, and _'global'_ shares one single limit
between all callers. If you omit **[per]** entirely, the limit is counted per username when the
caller is authenticated, and per IP address otherwise, which is typically what you want. When
resolving the client IP address, the slot prefers CloudFlare's `CF-Connecting-IP` request header
when it exists, since behind CloudFlare the raw connection IP resolves to the proxy and not to the
client, and only falls back to the connection IP when the header is absent.

The limit is a _fixed window_, implying `limit:50` with `window:60` allows exactly 50 invocations
per minute, with the counter resetting when the window expires. Rejected invocations are told how
many seconds remain before the window resets as part of the exception message.

Invoking **[execution.throttle.create]** with the name of an already existing throttle but a
_different_ configuration _replaces_ the throttle, the same way **[slots.create]** replaces an
already existing dynamic slot, also resetting its counters - while an _identical_ configuration
leaves the existing throttle untouched. Invoking it _without_ any arguments _deletes_ the throttle
instead, the same way **[cache.set]** without a value deletes the cached item.

```
// Deletes the throttle entirely.
execution.throttle.create:openai-budget
```

**[execution.throttle]** accepts _only_ a name - passing it any arguments throws an exception,
since configuration belongs exclusively to **[execution.throttle.create]**. Enforcing a throttle
that has not been declared also throws an exception, since this implies your endpoint expects a
rate limit that does not exist.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.threading](/plugins/magic.lambda.threading/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `execution.throttle`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execution.throttle",
  "description": "Enforces a named throttle previously declared with [execution.throttle.create], throwing a 429 exception once the limit is exceeded",
  "signature": {
    "input": {
      "kind": "throttle-name",
      "description": "Name of the throttle to enforce, as previously declared with [execution.throttle.create]",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `execution.kill`](/reference/slots/execution/execution.kill/) | [all `execution.*` slots](/reference/slots/execution/) | [`execution.throttle.create` &rarr;](/reference/slots/execution/execution.throttle.create/)

