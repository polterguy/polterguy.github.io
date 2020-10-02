# Scheduling tasks and creating business workflows

One of the things I personally love with Hyperlambda, is its built in task scheduler,
and business workflow engine, allowing me to decorate and persist _"function invocations"_ -
For later to execute these tasks, either through some other code trigger, or according
to some kind of repetition pattern. In the video below I am demonstrating how this works.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/5kRIcGdHehI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Business workflows

If you've been around for a while in the .Net Ecosystem you've probably heard of Microsoft Workflow
Foundation. Maybe even used it for a couple of projects. Although MWF was incredibly powerful, it
suffered by a whole range of problems, such as extremely poor scaling features, impossible to
understand XML syntax, dependencies upon Visual Studio, etc, etc, etc. From a business perspective
it was brilliant. From a developer's perspective it was (errh) _a piece of crap_. More importantly,
Microsoft completely abandoned the project as they moved into .Net Core land - Which makes sense,
considering all of its weaknesses too may I add.

Magic however, has its own similar construct, which you can find in the _"Tasks"_ menu item in
the Magic Dashboard. This is just its frontend GUI though, and everything related to tasks in
Magic, can be controlled through code. This allows you to create, decorate and persist _"function invocations_",
for then to later execute these, lending itself perfectly to solving the same problem as MWF solved.
Only without the dinosaur XML syntax, the crappy GUI parts for declaring control statements,
and the ridiculously slow implementation built on reflection.

## Scheduled tasks

Combining the task persister, with repetition patterns, happens to extend it in such a
way that this feature also gives you everything you're used to getting from other task
schedulers, such as Hangfire, etc - Except Magic of course gives you a perfectly valid
dynamic DSL (Hyperlambda), which of course allows you to _dynamically_ create these tasks,
not requiring recompilation of your site, or any other static changes to it, forcing
you to bring it out of production, to update its tasks. See an example of me creating
a send email task in the screenshot below.

![Scheduling a Hyperlambda Task](https://servergardens.files.wordpress.com/2020/10/task-scheduler.png)

You can create tasks with any Hyperlambda you wish, which at this point should fairly
easily and obviously explain the advantage with the Magic task scheduler, compared to
other schedulers. Watch the video above for details about how this works. Or
check out [the documentation](/documentation/magic.lambda.scheduler/) for the scheduler
project for more information.

* [Documentation](/documentation/)
