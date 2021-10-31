
# Magic Lambda System

This project contains _"system slots"_ to be able to invoke system commands. More specifically the project
contains the following slots.

* __[system.terminal.create]__ - Creates a new terminal process on the server
* __[system.terminal.write-line]__ - Writes a line/command to a previously opened terminal process on the server
* __[system.terminal.destroy]__ - Destroys/kills a previously created terminal process on the server

By combining the above slots with for instance the magic.lambda.sockets project, you can spawn off terminal/bash
processes on your server, creating _"virtual web based terminal sessions"_ on your server. To create a new
terminal process, use something such as the following.

```
system.terminal.create:my-terminal
   folder:/

   /*
    * STDOUT callback, invoked when something is channeled over STDOUT.
    */
   .stdOut

      /*
       * Do standard out stuff here, with the incoming [.arguments]/[cmd] command.
       */
      log.info:x:@.arguments/*/cmd


   /*
    * STDERROR callback, invoked when something is channeled over STDOUT.
    */
   .stdErr

      /*
       * Do standard out stuff here, with the incoming [.arguments]/[cmd] command.
       */
      log.info:x:@.arguments/*/cmd
```

The above **[.stdOut]** and **[.stdErr]** lambda objects are invoked when output data or error data is
received from the process, allowing you to handle it any ways you see fit. The **[folder]** argument
is the default/initial folder to spawn of the process in. All of these arguments are optional.

The name or the value of the **[system.terminal.create]** invocation however is important. This becomes
a unique reference for you, which you can later use to de-reference the instance, while for instance
feeding the terminal lines of input, using for instance the **[system.terminal.write-line]** slot.
To write a command line to an existing terminal window, such as the one created above, you can use
something such as the following.

```
system.terminal.write-line:my-terminal
   cmd:ls -l
```

The above will execute the `ls -l` command in your previously create _"my-terminal"_ instance, and
invoke your **[.stdOut]** callback once for each line of output the command results in. To destroy
the above created terminal, you can use something such as the following.

```
system.terminal.destroy:my-terminal
```

All terminal slots _requires a name_ to be able to uniquely identify _which_ instance you wish to create,
write to, or destroy. This allows you to create as many terminals as you wish on your server, only restricted
by memory on your system, and/or your operating system of choice.

The terminal slots works transparently for both Windows, Linux and Mac OS X, except of course the commands
you pass into them will differ depending upon your operating system.

**Notice** - If you don't reference a terminal session for more than 30 minutes, the process will be
automatically killed and disposed, and any future attempts to reference it, will resolve in an error.
This is to avoid having hanging processes on the server, in case a terminal process is started, and
then something happens, which disconnects the client, resulting in _"hanging sessions"_.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.system](https://github.com/polterguy/magic.lambda.system), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.system&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.system)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)
