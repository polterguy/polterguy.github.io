
# Magic Cloud, beyond CRUD and Low-Code

Magic is actually a lot more than just Low-Code and CRUD. In fact, the application generator is only _one_ aspect
of the system. Magic has 16 additional aspects, such as the ability to query your database using the integrated
SQL manager. Magic also contains an audit logging modules that automatically logs unhandled exceptions for you, and
everything else that might be of interest to you as you create your own apps. It contains a task scheduler, 
allowing you to create, persist, and schedule dynamically declared tasks based upon your own code, etc, etc,
etc. Watch the video below for a walkthrough of these features.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/22mqs2oYbQ8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

This arguably turns Magic into a complete and fully fledged _"Cloud IDE"_, to some extent replacing Visual Studio,
and your 3rd party cloud vendor's features, with your own locally hosted version of the same thing. In addition it
contains a micro service runtime environment, allowing you to create cryptographically signed HTTP REST invocations,
containing Hyperlambda code, securely executing this code over an inheritingly insecure connection such as the World
Wide Web. The closest you can find resembling this is AWS' cryptographically signed HTTP invocations, but they're quite
frankly a shallow comparison to Magic's cryptographically signed invocations abilities.
So before you dismiss Magic as a simple CRUD generator, realise this is only _one_ of its 13 aspects, serving all
possible needs your own custom applications might have.

## Aspects

* A fully fledged web based IDE (Integrated Development Environment)
* A complete JWT based authentication and authorisation module
* An integrated SQL management studio
* Application generator allowing you to create both backends and frontends automatically
* Endpoints module allowing you to play around with endpoints, similarly to how Postman works
* File management system allowing you to dynamically manage your server's files
* Evaluator allowing you to execute arbitrary Hyperlambda code
* A bash/terminal component allowing you to execute bash commands towards your backend
* Task scheduler and persister, allowing you to schedule tasks and persist tasks into your database
* Cryptographically secured lambda HTTP invocations, using public key cryptography to sign payloads, being Hyperlambda by themselves
* Registration module, allowing you to have users sign up as registered users in your database
* Diagnostics module providing diagnostics about the system's health
* Logging module, giving you easy access to read your server's logs
* Web sockets administration module allowing you to see meta information about currently connected clients, etc
* Configuration module, allowing you to edit your app's configuration through your browser
* An integrated Bazar component, basically an _"AppStore"_ for your server, through which you can obtain micro services for your backend
* Etc, etc, etc

If you have suggestions for additional modules, you can provide these as feature requests at
the [GitHub project website](https://github.com/polterguy/magic). However, the purpose of the
system is to solve repetetive tasks developers are facing as they start out new projects,
by providing automation modules implementing these as automagically as possible.
