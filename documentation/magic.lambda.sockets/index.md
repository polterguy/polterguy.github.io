
# Magic Lambda Sockets

This project provides web sockets hooks for for [Magic](https://github.com/polterguy.magic).
The main idea of the project, is that it allows you to resolve Hyperlambda files, execute these,
passing in a URL and JSON arguments over a web socket connection - In addition to subscribing to messages
published by the server over a web socket connection. The project builds upon SignalR, but the internals are
completely abstracted away, and you could probably easily exchange SignalR with any other web socket
library with similar capabilities. The project contains one socket SignalR hub method with
the following signature.

```
execute(string file, string json);
```

To connect to the hub use the relative URL `/sockets`, optionally passing in a JWT token, and then
transmit messages to the hub using something such as for instance the following TypeScript.

```typescript
let builder = new HubConnectionBuilder();

this.connection = builder.withUrl('https://api.your-domain.com/sockets', {
    accessTokenFactory: () => 'returns-your-JWT-token-here'
  }).build();

this.connection.invoke(
  'execute',
  '/foo/some-hyperlambda-file',
  JSON.stringify({
    foo:'bar'
  }));
```

The above will resolve to a Hyperlambda file expected to exist at `/modules/foo/some-hyperlambda-file.socket.hl`,
passing in the `foo` argument as lambda nodes. In addition you can invoke SignalR methods by signaling
the **[sockets.signal]** slot, which will automatically transform the specified children nodes to JSON
and invoke the specified method for all subscribers. Below is an example.

```
sockets.signal:foo.bar
   roles:root, admin
   args
      howdy:world
```

The above will invoke the `foo.bar` method, passing in `{"howdy":"world"}` as a JSON string, but only users belonging
to the roles of either `admin` or `root` will be notified. Both the **[roles]** and the **[args]** arguments are optional.
To subscribe to the above invocation, you could use something such as the following in TypeScript.

```typescript
this.connection.on('foo.bar', (args) => {
  console.log(JSON.parse(args));
});
```

The **[sockets.signal]** slot can handle the following optional arguments but _only one_ of these can be supplied.
If you instead of signaling all belonging to a specific role only want to signal a list of users, you can use
something such as the following.

```
sockets.signal:foo.bar
   users:user1, user2, user3
   args
      howdy:world
```

## Arguments to [sockets.signal]

* __[roles]__ - Comma separated list of roles to send message to
* __[users]__ - Comma separated list of users to send message to
* __[args]__ - Arguments to transmit to subscribers

Only one of **[users]** or **[roles]** can be supplied.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.sockets](https://github.com/polterguy/magic.lambda.sockets), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sockets&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sockets)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.
