---
title: Hyperlambda and Web Sockets
description: This article shows you how to use SignalR and web sockets with Magic and Hyperlambda, by walking you through creating a simple chat client, allowing multiple users to chat in real time, using Angular and Hyperlambda.
---

# Hyperlambda and Web Sockets

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* How to use Web Sockets in Hyperlambda and Magic
* How to create a minimalistic chat client using Hyperlambda and Angular

In addition to [plain CRUD](/tutorials/database-crud/) Magic also supports web sockets. In case you're new to web sockets,
a web socket is a bidirectional communication channel through which your web server can _"push"_ data to clients.
A typical use case for this is a chat application, but obviously this is useful in a lot of other scenarios too. In
this tutorial, we will create a chat client in Angular and Hyperlambda, using the server side SignalR plugin
in Magic, to let multiple users chat with each other, having the messages transmitted in real time to all clients.
If you prefer to see me walk you through this in a video, you can watch the following YouTube video.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/8NXO1V1i-JY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


## Our Angular frontend

First we'll need a frontend. Use the Angular CLI to create a new Angular project and name it _"chat"_.
Open a terminal on your development machine and execute the following command in it.

```
ng new chat
```

You can choose whatever setting you wish, but I chose the following as I went through the questions.

1. No routing
2. SCSS

Change into this folder in your terminal using `cd chat`, and use for instance Visual Studio Code to open the
folder. If you have the Visual Studio Code command line binding, you can do this by typing `code ./` into
your terminal. Then we'll need a terminal window in VS Code. You can open a new terminal window in
the _"Terminal"_ menu item of VS Code. Type the following command into your VS Code terminal window.

```
npm link
```

This ensures we link in all packaged our project depends upon. This might take some time. Afterwards we'll
need to add the client side SignalR package. Execute the following command in your terminal window.

```
npm install @aspnet/signalr
```

Now we can serve our project with the following command.

```
ng serve --port 4201
```

The reason why we need to override the port, is because the Magic Dashboard is probably already running
on the default port which is 4200. You can now visit [localhost:4201](http://localhost:4201/) to see
your app. Use VS Code and open the _"app.component.html"_ file in the folder _"/src/app/"_ and replace its existing code
with the following HTML.

```html
<div>
  <h1>Chat client</h1>
  <textarea id="" cols="30" rows="10" [(ngModel)]="message">{{message}}</textarea>
  <br />
  <button (click)="send()">Submit</button>
  <br />
  <textarea id="" cols="30" rows="10" [(ngModel)]="content"></textarea>
</div>
```

The UI isn't going to win a design contest, but to keep the tutorial relevant to web sockets,
we'll ignore the UI for now. If you wish to create a better UI you might benefit from reading up
on [Angular Material](https://material.angular.io). If you saved your above HTML file, you've now got a couple of
compiler errors. This is because we are using fields on our `AppComponent` class that still doesn't
exist. Modify your _"app.component.ts"_ file to resemble the following.

```typescript
import {
  Component,
  OnDestroy,
  OnInit
} from '@angular/core';

import {
  HttpTransportType,
  HubConnection,
  HubConnectionBuilder
} from '@aspnet/signalr';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {

  content = '';
  message = '';
  hubConnection: HubConnection;

  ngOnInit() {

    let builder = new HubConnectionBuilder();
    this.hubConnection = builder.withUrl('http://localhost:5000/sockets', {
      skipNegotiation: true,
      transport: HttpTransportType.WebSockets,
    }).build();

    this.hubConnection.start();
    this.hubConnection.on('chat.new-message', (args) => {
      this.content += JSON.parse(args).message + '\r\n\r\n';
    });

  }
  
  ngOnDestroy() {
    this.hubConnection.stop();
  }

  send() {

    this.hubConnection.invoke(
      'execute',
      '/tutorials/add-chat',
      JSON.stringify({
        message: this.message,
      }));

    this.message = '';

  }
}
```

You might have to change the URL above to _"http://localhost:5555/sockets"_ if you
installed Magic using the docker images.
The above code ensure we are initialising SignalR as the component is initialised, and that we
are disconnecting SignalR as the component is destroyed - In addition to that we are transmitting new
chat messages over our SignalR connection as the user clicks the _"Submit"_ button. There are 3 methods
in the above Angular TypeScript, and they do the following.

1. `ngOnInit` - Initialising our SignalR socket and connects to our backend
2. `ngOnDestroy` - Stops our socket connection
3. `send` - Transmits the chat input textbox' content to the backend file _"/modules/tutorials/add-chat.socket.hl"_ file

Then we'll need to import the `FormsModule` which you can do by modifying your _"app.module.ts"_
file to contain the following code.

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

And we are done with our frontend. Save all your files, and let's move onwards to our backend.

## Your Hyperlambda SignalR backend

If you click the _"Submit"_ button, you will see that your console window gives you an error. This
is because we have still not yet created our backend file responsible for executing as
we submit chat messages to the server. Open up your Magic Dashboard with the [localhost:4200](http://localhost:4200/)
URL in a different browser window, log in with your root account, and open the _"Hyper IDE"_ menu item.
Then do _exactly as follows_.

1. Click the _"modules"_ folder
2. Click the _"New"_ button
3. Type _"tutorials"_ into the textbox
4. Check the _"Folder"_ checkbox to make sure we create a _folder_ and not a file
5. Click _"Create"_

Notice, if you've followed some of the previous hands on tutorials, you might already have this folder,
at which point you can ignore the above, and move onwards to the next task.
The above creates a new folder called _"tutorials"_ inside your _"modules"_ folder. Then do exactly as follows.

1. Click the _"tutorials"_ folder
2. Click the _"New"_ button
3. Type _"add-chat.socket.hl"_ into the textbox
4. Click _"Create"_

This creates a new Hyperlambda file for you. This file will be resolved as the above `send()` Angular method
is invoked over our SignalR web socket connection. Paste in the following into your file.

```
.arguments
   message:string

unwrap:x:+/*/*
sockets.signal:chat.new-message
   args
      message:x:@.arguments/*/message
```

Then save your file, and switch back to your chat client browser window, and try writing something into
the textarea and click _"Submit"_. Your app should resemble the following screenshot now.

![Chat client](https://servergardens.files.wordpress.com/2021/06/chat-client.png)

## Internals

As I started out with, web sockets are a _bidirectional_ transport channel, implying we can both
send and receive data over a socket. In the above `send()` method we are pushing data _to_ the server.
The above **[sockets.signal]** Hyperlambda slot transmits this message to all subscribers of our
_"chat.new-message"_ message. In our above Angular code we are subscribing to these messages with
the following TypeScript.

```typescript
this.hubConnection.on('chat.new-message', (args) => {
  this.content += JSON.parse(args).message + '\r\n\r\n';
});
```

This ensures that all clients having connected to our web socket backend registering interest in
the above messages, will be notified every time the message is published by our Hyperlambda.
If you wish, you can open up multiple browser windows simultaneously and point them
to [localhost:4201](http://localhost:4201/), and write something into any chat, and see how the
message is instantly received in all browser windows.

### Endpoint resolving

One crucial point which separates the Hyperlambda web sockets implementation from other
SignalR implementations, is the dynamic endpoint resolving. What this implies is that the file
called _"add-chat.socket.hl"_ is dynamically executed due to our invocation in the following
Angular code.

```typescript
this.hubConnection.invoke('execute', '/tutorials/add-chat', JSON.stringify({
   message: this.message,
}));
```

Notice how the second argument resembles the relative path of the file. What the endpoint
resolver will do, is roughly to add _".sockets.hl"_ to the relative URL specified, load
this file dynamically, add the input arguments, and execute its Hyperlambda. This gives
us a way to dynamically execute Hyperlambda files to respond to incoming SignalR messages.
In addition it gives us the same method to declare arguments and pass in arguments to our
SignalR invocations as we would use for normal HTTP REST invocations - Which of course makes
it much simpler to consume and learn as you start out with web sockets in Magic.

The endpoint resolver works almost exactly the same way any HTTP Hyperlambda
file resolves, except instead of ending with the HTTP verb, it ends with _".socket.hl"_.
Besides from that, it loads arguments and converts these the same way, it dynamically resolves
the files the same way, etc. You don't have access to the HTTP context, such as response,
status code, etc - But besides from that, the socket parts of Magic is similar enough to the HTTP
Hyperlambda endpoint resolver that you can most of the time interchange these by simply changing
the extension of your Hyperlambda filenames.
You can also mix and match socket Hyperlambda files and HTTP Hyperlambda files
as you see fit, such as for instance publish a message using **[socket.signal]** from any
HTTP backend Hyperlambda file, etc.

* Continue with [Threading and async Hyperlambda programming](/tutorials/threading/)
