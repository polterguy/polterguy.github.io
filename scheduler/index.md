
# Scheduling C# methods

CRUD scaffolding is not the only feature Magic provides. In addition to its CRUD scaffolding abilities,
Magic also features a task scheduler, allowing you to dynamically declare your tasks in Hyperlambda, for
then to have them executed some point in time in the future. You can declare tasks to be executed once,
or according to some sort of repetition pattern, such as _"every Sunday at 22:00 hours"_, etc.

![Creating a scheduled task in Magic](https://servergardens.files.wordpress.com/2019/11/wednesday.png)

This allows you to create automated tasks, that are executed at some interval or point in time in the
future. Due to Magic's Hyperlambda DSL, creating fairly advanced tasks is also relatively easy. The
integrated Hyperlambda editor also gives you AutoComplete, allowing you to easily modify the tasks
_"definition"_. Imagine the following C# code for instance

```csharp
using magic.node;
using magic.node.extensions;
using magic.signals.contracts;

namespace foo
{
    [Slot(Name = "create-database-backup")]
    public class CreateDatabaseBackup : ISlot
    {
        public void Signal(ISignaler signaler, Node input)
        {
            var databaseName = input.GetEx<string>();
            /*
             * Create backup of specified database here ...
             */
        }
    }
}
```

Then realize how the above DSL extension will automatically populate your AutoCompleter during
task creation by allowing you to click CTRL+SPACE to show suggestions. Below is a screenshot
illustrating this relationship.

![AutoCompletion during task creation](https://servergardens.files.wordpress.com/2019/11/create-database-backup.png)

Listing tasks is also integrated, allowing you to easily filter, create, and manage your tasks.

![List of scheduled tasks](https://servergardens.files.wordpress.com/2019/11/list-tasks.png)

Notice, the Magic Scheduler is not yet out of its initial BETA release, and currently not production ready -
But it should be mature enough for you to play around with it to get a feeling for it. Notice, by default
the scheduler is turned _OFF_ as you start your Magic Web API application. Either turn it explicitly _ON_
by clicking the _"Start scheduler"_ button, or change your _"appsettings.json"_ file to configure it to
start out of the box.

[Extending Magic with C#](/csharp)
