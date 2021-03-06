
# Magic, a Cloud Based IDE +++

Magic is actually a lot more than just CRUD. In fact, the application generator is only _one_ aspect
of the system. Magic has 12 additional aspects, such as the ability to query your database using the integrated
SQL manager. Magic also contains an audit logging modules that automatically logs unhandled exceptions for you, and
everything else that might be of interest to you as you create your own apps. It contains a task scheduler, 
allowing you to create, persist, and schedule dynamically declared tasks based upon your own code, etc, etc,
etc. Watch the video below for a walkthrough of these features.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/22mqs2oYbQ8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

This arguably turns Magic into a complete and fully fledged _"Cloud IDE"_, to some extent replacing Visual Studio,
and your 3rd party cloud vendor's features, with your own locally hosted version of the same thing. In addition it
contains a micro service runtime environment, allowing you to create cryptographically signed HTTP REST invocations,
containing Hyperlambda code, securely executing this code over an inheritingly insecure connection such as the World
Wide Web. The closest you can find resembling this is AWS' cryptographically signed HTTP invocations, but they're quite
frankly a pale comparison to Magic's cryptographically signed invocations abilities.
So before you dismiss Magic as a simple CRUD generator, realise this is only _one_ of its 13 aspects, serving all
possible needs your own custom applications might have.

## Aspects

* A complete JWT based authentication and authorisation module
* An integrated SQL management studio
* Application generator allowing you to create both backends and frontends automatically
* Endpoints module allowing you to play around with endpoints, similarly to how Postman works
* File management system allowing you to dynamically manage your server's files
* Evaluator allowing you to execute arbitrary Hyperlambda code
* Task scheduler and persister, allowing you to schedule tasks and persist tasks into your database
* Cryptographically secured lambda HTTP invocations, using public key cryptography to sign payloads, being Hyperlambda by themselves
* Registration module, allowing you to have users sign up as registered users in your database
* Diagnostics module providing diagnostics about the system's health
* Log module, giving you easy access to read your server's logs
* Configuration module, allowing you to edit your app's configuration through the browser

If you have suggestions for additional modules, you can provide these as feature requests at
the [GitHub project website](https://github.com/polterguy/magic). However, the purpose of the
system is to solve repetetive tasks developers are facing as they start out new projects,
by providing automation modules implementing these as automagically as possible.

* [Documentation](/documentation/)
