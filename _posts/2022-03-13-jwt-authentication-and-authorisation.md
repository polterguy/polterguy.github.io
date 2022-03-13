---
layout: post
author: thomas
title: JWT authentication and authorisation
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/authorized.jpeg"
description: JWT is an industry standard for authorisation and authentication. In this article I walk you through the basic ideas of the standard, and explains how it works.
---

JWT is one of those rare things that pops up once every now and then that solves a real problem in such a beautiful way it's almost impossible to ignore, resulting in that it becomes a force of its own and ends up becoming the industry standard. My first reaction to the thing when I discovered it was roughly as follows; _"Golly gosh this is cool!"_ However, it comes with compromises, and it forces you to think differently. In this article I will first explain how it works, then I'll explain its advantages, for then to finish up with how it changes your thinking. First of all a JWT token is simply 3 JSON objects, each of which are base64 encoded, for then to separate each base64 encoded JSON object with a _"."_. A typical JWT token therefor looks like this.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6I
kpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

Notice the two `.` characters in the above example. Also notice I have added CR/LF sequences to the above example to simplify understanding. An actual JWT token _cannot_ have CR/LF sequences in it. If you break down the above token at for instance [jwt.io](https://jwt.io) you can see its 3 segments. These are as follows.

1. Header containing meta information about your token
2. Payload being your actual token
3. Signature making it possible to verify the token's validity on the server

The header information contains information about for instance what type of token you have, what hashing algorithm was used to create its signature, etc. Typically you want to use some sort of HMAC for the latter, probably based upon Sha256. The payload typically contains your username, roles, claims, etc, and is the actual authorisation and authentication parts of your token. Implying your _"identity"_. The last part is simply the token's payload concatenated with some server-side only secret, for then to create a hash from these. The last point is crucial since without your server's secret creating a valid token becomes impossible. Hence assuming you can keep your secret a secret you have a perfectly valid method to create a highly secure authentication and authorisation mechanism to allow for clients invoking your server to be authorised to do whatever it is they need to do.

Typically a token is requested from your backend with a username and password combination, and if it matches your user database, a JWT token is created and returned to the client. The client then typically passes in this token upon consecutive requests towards your server as a _"Bearer"_ token in its Authorization HTTP header. As the server is invoked, it can then retrieve the token's payload from the Authorization HTTP header, append the secret to it, and run the hash algorithm on the concatenated result to verify it's getting the same hash value as the signature parts of the token it was given. If the last step fails, it implies the token is not valid since it was not created with the same secret the server had, and the request can be aborted returning some sort of 401 HTTP response to the client.

The beauty of the above process is that first of all it's highly secure as long as you can keep your secret a _secret_. However, the real beauty of the above is that you _never have to touch your database to verify a token_. The last part is a crucial feature of JWT resulting in that a JWT token is considered a _"lighteweight authorisation mechanism"_, making things blistering fast, with better scalability, since you don't have to touch your database to verify the token. However, this feature also comes with a caveat, which is that unless you manually add code to check the user upon every single request towards your server, the user cannot be _"locked out"_ of your app with immediate effect, and any user having somehow gained access to a valid token by logging in for instance will have access to your backend for as long as the token is valid. For the record, we do _not_ encourage users of Magic to check the user's access on every single request unless it's absolutely crucial to be able to instantly lock out users from your backend. This would defeat the whole purpose of JWT and result in much less scalability and throughput of your server side backend, and/or complicate your solution with advanced caching constructs, making things much more difficult to scale out and load balance, etc ...

Another beautiful fact about JWT tokens is that they are _"transparent"_, implying the frontend can base64 decode your token, find the payload, and know just as much about the identity of the user as the backend knows. This allows you to display username, roles, claims, etc in your frontend, _without_ having to do additional invocations towards your backend besides the original authenticate invocation. The latter part assuming your client is given access to the actual token, and you don't return it as a server-side only cookie or something.

## How we solved "lockouts" in Magic

JWT has one really cool feature, which is that you can set _"expiration time"_ for your tokens. This is a UTC timestamp that says when the token is expired and can no longer be used. In Magic we use 120 minutes into the future for this, implying a token is only valid for 2 hours after having been created originally. This again implies the user needs to login again after 2 hours, which is inconvenient to say the least. The way we solved the last part is by creating a _"refresh-token"_ endpoint that if invoked with an existing token will simply take that token's payload, create a new token from it with a new expiration date 2 additional hours into the future.

This implies that in our clients we can read the JWT token's expiration date, make sure we invoke the refresh token endpoint some few minutes before the token expires, and replace the existing token our client is using with the newly generated token created by the backend as we refresh our token. During this refresh part we can check the database and add additional overhead to verify the user has access, and has not been locked out or anything, since it's an event that is only happening once every 2 hours. This gives us the best from two world since first of all we've got lightweight and secure tokens not needing to access our database to verify a user has access, while we get the ability to lock out users already having acquired an existing token, only not _immediately_ since it'll take two hours before the database is checked again to verify the user has access. The 2 hours parts of course can be configured in Magic by changing the _"valid-minutes"_ configuration setting. I don't recommend changing this to anything below 5 or 10 minutes however, since it kind of invalidates the whole advantage with JWT tokens.

So yes, you loose the ability to lock out users with immediate effect, but the advantages are so great in all other regards that we've chosen to make this the default authentication and authorisation mechanism in Magic. If you want to read up further about Magic's internal auth parts you can find a more extensive guide [here](https://docs.aista.com/tutorials/registering/) that explains user registration, double optin, and other parts of Magic's internal auth mechanisms. You're also of course welcome to download Magic and use it as your _"out of the box"_ registration and SSO user administration system. In addition to being an out of the box JWT solution it also provides you with everything else related to [user administration](https://docs.aista.com/documentation/magic/components/auth/), including high level UI components for administrating your users such as illustrated below.

* [Download Magic](https://docs.aista.com/tutorials/getting-started/)

![User administration in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)
