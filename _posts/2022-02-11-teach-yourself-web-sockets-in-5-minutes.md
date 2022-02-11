---
layout: post
author: thomas
title: Teach yourself Web Sockets in 5 minutes
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sockets.jpg"
---

In this article we will go through the following concepts.

* The pub/sub design pattern, also known as _"the Hollywood design pattern"_
* Basic web socket theory, and how to publish and subscribe to socket messages
* Authorisation to prevent malicious users from intercepting our messages
* How Magic automatically solves a lot of your socket related problems
* Finally we'll show and tell with a video how Magic's web socket implementation is tied together

Web Sockets allows for a bidirectional communication channel, through which your server can _"push"_ data to the client, triggering events on the client when something occurs on the server. This has huge advantages for some types of web apps, such as for instance trading systems, chat clients, and apps where you need to see live updates in your client as changes occurs on the server.
However, wiring up a web socket module manually is also ridiculously complex, making sockets effectively unavailable for most developers. For these reasons dozens of helper libraries and modules have been created to simplify the subject. For PHP there's [Laravel Sockets](https://medium.com/swlh/guide-to-using-sockets-in-your-laravel-application-596d42367f0e). In this article I
will walk you through how to use web sockets in Magic using [SignalR](https://dotnet.microsoft.com/en-us/apps/aspnet/signalr),
and I will be focusing on the server side parts mostly, since this is the most difficult part. However, once you understand
how sockets works in Magic on the server side, you can easily implement the client side of the equation using SignalR's
Angular implementation, ReactJS implementation, etc.

## The Hollywood Design Pattern

Sockets are typically based upon the [pub/sub design pattern](https://hackernoon.com/publish-subscribe-design-pattern-introduction-to-scalable-messaging-781k3tae). This pattern is often referred to as _"The Hollywood Design Pattern"_, because in Hollywood it's common to be told _"don't call us, we'll call you"_. The pub/sub design pattern also reverses the responsibility, such that instead of your code invoking another function, you provide a _"callback"_ to the other party that the other party can use when it needs to call you.

> Don't call us, we'll call you!

In Magic and most other sane web socket libraries, this is typically implemented such that you inform the backend what
_"type"_ of messages you want to subscribe to. This _"type"_ is typically just a simple name such as illustrated below.
Open up the _"Analytics/Sockets"_ dashboard menu item in Magic, then click the _"Subscribe"_ button, at which point you'll see
something resembling the following.

![Socket message subscription](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sockets.jpg)

When you click the above subscribe button, Magic negotiates a socket _"channel"_ with the server, informing the server of that
it's interested in messages of type _"foo"_, resulting in that every time a _"foo"_ message is published in your backend, your
code will be called. This is the equivalent of leaving your phone number with a Hollywood movie director, hoping for a role
to pop up, having the director call you and offer you the role when the role is available.

## Publishing a message

The screenshot below illustrates how to publish a socket message from your Magic dashboard. Click the _"Publish"_ button
to reproduce what I'm doing below.

![Socket message subscription](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/publish-socket-message.jpg)

When you click _"Send"_ in the above dialog, you will instantly see a message popping up on your page afterwards. This
message was _"pushed"_ from the server, over the bidirectional communication channel established between your client
and your server as the socket connection was negotiated, because your client was subscribing to _"foo"_ messages. If you
had sent a _"bar"_ message, you would not see the message, because you're only subscribing to _"foo"_ messages. In the
video below I am demonstrating the whole process.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/vxXK4dDRWfk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Authorisation

The above creates a dilemma for us, since anyone knowing which messages a server might in theory publish, can just
subscribe to the message type, and such see all data sent between clients. This is obviously not a good thing, and unless
your socket library has some sort of mechanism to allow for only authorised clients to be notified you should switch
library. To use an analogy for this dilemma, imagine a Hollywood actor having an opening for a role, for then to call
200 people having auditioned for the role, letting _everybody_ know they got the role.
The way Magic solves this is to add support for authorisation as the backend is publishing socket messages. There are
3 types of such authorisation schemes in Magic.

* __[roles]__ - Only notifying users belonging to the specified roles
* __[groups]__ - Only notifying users belonging to the specified groups
* __[users]__ - Only notifying the specified users

Below is an example of how this would look like in Hyperlambda.

```
sockets.signal:foo
   roles:root, admin
   args
      greeting:You got the role mate! Congratulations!
```

In the above Hyperlambda you can see how the publishing of the message is making sure only users belonging to
either the _"admin"_ role or the _"root"_ role is notified. If you subscribe to _"foo"_ messages like
we started out with at the top of this article, and execute the above Hyperlambda, you will see the message
popping up on your dashboard. Hint, you can do this by opening up two browser windows at the same time, and
have one of them executing the above Hyperlambda through your _"Evaluator"_ component, and the other subscribing
to _"foo"_ messages through your _"Sockets"_ component. If you change the above authorisation requirements to
only contain the value of _"admin"_ and you invoke your Hyperlambda again, you'll notice how your client does
_not_ get notified, unless your root user also belongs to the _"admin"_ role too of course.

To subscribe to SignalR messages using Angular, you can read [the following article](/tutorials/web-sockets/),
however the code required to subscribe to socket messages from Angular is literally as easy as the following.

```typescript
  ngOnInit() {

    let builder = new HubConnectionBuilder();
    this.hubConnection = builder.withUrl('http://localhost:4444/sockets', {
      skipNegotiation: true,
      transport: HttpTransportType.WebSockets,
    }).build();

    this.hubConnection.start();
    this.hubConnection.on('foo', (args) => {
      console.log(args);
    });

  }

  ngOnDestroy() {
    this.hubConnection.stop();
  }
```

If you create a new Angular component implementing `OnInit` and `OnDestroy`, for then to paste the above code
into it, you'll see console log invocations every time you publish a socket message from your backend of
type _"foo"_. Notice, you'll need to install the Angular SignalR package before you can use SignalR from
Angular. You can achieve this using the following code from a terminal within your project's folder.

```
npm install @aspnet/signalr
```

Notice also that the above Angular code assumes you're using the Docker images of Magic. If you're
using the source code download you'll have to change the `4444` port to `5000`.
