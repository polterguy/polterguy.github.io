---
title: magic.lambda.dates
moved_anchors: {"how-to-use-dateformat": "/reference/slots/date/date.format/#guide", "how-to-use-datefrom-unix": "/reference/slots/date/date.from-unix/#guide", "how-to-use-datemax": "/reference/slots/date/date.max/#guide", "how-to-use-datemin": "/reference/slots/date/date.min/#guide", "how-to-use-datenow": "/reference/slots/date/date.now/#guide", "how-to-use-dateunix": "/reference/slots/date/date.unix/#guide", "how-to-use-time": "/reference/slots/core/time/#guide", "how-to-use-timeformat": "/reference/slots/time/time.format/#guide", "how-to-use-timetotal-milliseconds": "/reference/slots/time/time.total-milliseconds/#guide"}
---

This project contains date manipulation slots for Magic. More specifically, this project contains the following slots.

* __[\[date.now\]](/reference/slots/date/date.now/)__ - Returns the now date, equivalent of `DateTime.Now`.
* __[\[date.from-unix\]](/reference/slots/date/date.from-unix/)__ - Converts the specified Unix timestamp to a `DateTime` object.
* __[\[date.min\]](/reference/slots/date/date.min/)__ - Returns the minimum date value, equivalent of `DateTime.MinValue`.
* __[\[date.max\]](/reference/slots/date/date.max/)__ - Returns the maximum date value, equivalent of `DateTime.MaxValue`.
* __[\[date.unix\]](/reference/slots/date/date.unix/)__ - Returns the current UTC time as a Unix timestamp.
* __[\[date.format\]](/reference/slots/date/date.format/)__ - Returns a string representation of some date, formatted according to the specified **[format]** argument.
* __[\[time.total-milliseconds\]](/reference/slots/time/time.total-milliseconds/)__ - Returns the total number of milliseconds in a time span.
* __[\[time.format\]](/reference/slots/time/time.format/)__ - Formats a time span as a string, according to the specified **[format]** argument.
* __[\[time\]](/reference/slots/core/time/)__ - Creates a time span, useful for adding and subtracting offsets to date objects. Pass in **[days]**, **[hours]**, **[minutes]**, **[seconds]** or **[milliseconds]** to declare how large your offset is. All arguments are optional, but (of course) at least one argument should be passed in.

**Notice** - Internally in Magic, everything is UTC Universal timezone, implying if you want to render it in user's
timezone, you'll have to convert it explicitly in your client/frontend. All dates and times internally in  Magic,
also those stored into any database, are treated as UTC timezone. All dates transmitted _to_ the backend, is also
assumed to be UTC. This is to make things simple in regards to interacting with database systems, that may or may not
add support for timezone offsets.
Below is an example of taking the current date and time, and adding two days and one second to it, for then to
format the result as a string.

```
math.add
   date.now
   time
      days:2
      second:1

date.format:x:-
   format:"yyyy-MM-dd HH:mm:ss"
```
