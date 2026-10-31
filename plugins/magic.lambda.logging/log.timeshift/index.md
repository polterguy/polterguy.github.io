---
title: "How to use [log.timeshift]"
description: "How to use [log.timeshift] - This slot counts the log items matching a search string per day, for the last two weeks, and is useful for creating a time series of how often something is logged."
generated: true
guide: true
---

This is the guide to [`log.timeshift`](/reference/slots/log/log.timeshift/), whose reference page has its arguments, constraints and declaration.

This slot counts the log items matching a search string per day, for the last two weeks, and is useful for
creating a time series of how often something is logged. The value of the slot is mandatory, and must be a
string a log item's content is matched against, or a log entry type. As with filtering, you should invoke
**[log.capabilities]** to verify that your log implementation has `can-timeshift` set to true before relying upon it.

```
log.timeshift:tick
```

The slot returns one unnamed child node per day, starting with today (UTC) and moving backwards in time, and
each child has the following two arguments.

* __[when]__ - The date of the bucket, formatted as `yyyy-MM-dd`
* __[count]__ - Number of matching log items for that day, which is 0 for days without matches

If `tick` was logged twice today, the first returned node would have today's date as its **[when]** and 2 as its
**[count]**, while the second node, representing yesterday, would have a **[count]** of 0.
