---
title: Persisted and scheduled Hyperlambda tasks
description: Magic allows you to persist Hyperlambda snippets into your database, for then to schedule these snippets to execute whenever you want them to execute.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-tasks.jpg"
---

# Persisted and scheduled Hyperlambda tasks

The tasks component allows you to create and administrate persisted Hyperlambda tasks, and/or schedule
tasks for executing, either in a repeating pattern somehow, or at an exact date and time in the future.
To understand how the task scheduler works you can refer to [this document](/tutorials/task-scheduler/).
Below is a screenshot of the component.

![Hyperlambda task scheduler](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-task.jpg)

The idea of the task scheduler is first of all to allow for creating dynamically persisted tasks that can be triggered
by some future event, facilitating for _"Business Process Workflows"_ - In addition to scheduling your
tasks to be executed at some specific date and time in the future, and/or in a repeating fashion.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)
