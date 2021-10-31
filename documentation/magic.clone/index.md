
# Magic Clone - Develop Magic locally

This recipe assumes you've got VS Code, MySQL or SQL Server accessible somewhere, NodeJS, Angular,
and the .Net SDK version 5 or higher. You can also use Visual Studio instead of VS Code if you're
on Windows, at which point you only need to open the _"magic.sln"_ file. When you've made sure
you've got all of these parts, clone this repository locally using the following.

```
git clone https://github.com/polterguy/magic.clone.git
```

Then run the _"clone.sh"_ file, and wait until it's done - At which point you will find everything
needed to run and debug Magic locally within your _"src/"_ folder. Whenever you need to pull the
repositories again simply execute _"pull.sh"_. To debug, and/or run Magic, type the following in a terminal.

```bash
cd src

// This requires having VS Code locally installed and in your path
code ./
```

Then open _two_ terminal windows and type the following into the first.

```bash
cd magic
cd backend
dotnet run -p dev_backend.csproj
```

Type the following into the second terminal window.

```bash
cd magic
cd frontend
npm link
ng serve
```

When `ng serve` and `dotnet run` is done, you can visit [localhost:4200](https://localhost:4200) in your
browser, and you should be set.

To debug, click F5 in VS Code, and choose _".Net Core"_, then click _"Configure"_ and choose _"Attach to existing .Net Core command line program"_. Save your _"launch.js"_ file, and click F5 once again, and choose the process
called _"backend.exe"_ (something) at the top of your choices. You can now set breakpoints, and/or debug
Magic locally on your development machine.

