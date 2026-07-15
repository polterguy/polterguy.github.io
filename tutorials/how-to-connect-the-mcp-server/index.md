---
title: How to connect the MCP server
description: Magic contains an integrated MCP server with OAuth, allowing you to connect Claude, Claude Code, Cursor, and any other MCP client to your cloudlet, giving the AI secure access to your backend, your data, and your Hyperlambda Generator.
---

Magic comes with an integrated MCP server, allowing you to connect AI clients such as Claude, Claude Code, Codex, Cursor, and anything else supporting the [Model Context Protocol](https://modelcontextprotocol.io) to your cloudlet. Once connected, the AI can discover and invoke your backend's endpoints as MCP _"tools"_ — and since the Hyperlambda Generator itself is exposed as a tool, the AI can even _create new tools on demand_, by generating Hyperlambda endpoints for you.

## Installing the MCP server

The MCP server is delivered as two plugins you install through your dashboard. Open your dashboard, go to _"Misc/Plugins"_, and install the following two plugins.

* __oauth__ - The OAuth 2.1 authorization server, allowing MCP clients to authenticate through the normal browser login and consent flow
* __mcp__ - The MCP server itself, exposing your endpoints as tools

You can read more about installing plugins [here](/dashboard/plugins/). Once both plugins are installed, the MCP server is live, and its URL is your cloudlet's domain followed by the path below.

```
https://YOUR-CLOUDLET/magic/modules/mcp/mcp
```

That URL is all you need. Magic's MCP server supports OAuth 2.1 with automatic discovery and client registration, so there are no tokens to copy and paste — when you add the URL to your MCP client, it will open your browser, ask you to log in with your Magic username and password, and ask for your consent. Once you click _"Allow"_, the client is connected, and acts on your behalf, with your user's roles.

## Connecting Claude

In Claude's settings, go to _"Connectors"_, click _"Add custom connector"_, and paste in your MCP server's URL. Claude will take you through the browser login and consent flow, and afterwards your cloudlet's tools show up in Claude's tool list.

## Connecting Claude Code

Add the server with the following command.

```bash
claude mcp add --transport http magic https://YOUR-CLOUDLET/magic/modules/mcp/mcp
```

Then run `/mcp` inside Claude Code to authenticate, which triggers the same browser login and consent flow.

## Connecting Cursor

Add the following to your `mcp.json` file.

```json
{
  "mcpServers": {
    "magic": {
      "url": "https://YOUR-CLOUDLET/magic/modules/mcp/mcp"
    }
  }
}
```

Other clients supporting remote MCP servers over HTTP are configured the same way — the only thing they need is the URL.

## What the AI gets access to

Every dynamic HTTP endpoint you have created beneath your cloudlet's `modules/` folder is exposed as an MCP tool, with a JSON schema derived from the endpoint's declared arguments. This implies your existing endpoints — whether you created them with the [Endpoint Generator](/dashboard/endpoint-generator/), the [Hyperlambda Generator](/dashboard/hyperlambda-generator/), or by hand — become tools the AI can invoke, without you having to maintain a separate tool registry.

Authorization is enforced the exact same way as for any other HTTP client: the access token carries the roles of the user who consented, and each endpoint's own authorization requirements still apply. If you consent as a user who cannot invoke some endpoint, neither can the AI. Notice, this also implies that if you consent as _"root"_, the AI has root access to your cloudlet — for day-to-day use we recommend creating a dedicated user with only the roles the AI actually needs, and consenting as that user.

## Creating new tools with AI

Because the Hyperlambda Generator is itself available over MCP, a connected AI client can create new endpoints for you — you describe what you want in plain English, the generator creates the Hyperlambda, and the new endpoint immediately becomes available as a tool. This turns your cloudlet into a backend the AI can both _use_ and _extend_, while your data stays in your own database, behind your own authorization.

Notice, some clients cache the tool list at the moment you connect. If you have created new endpoints and they don't show up as tools, disconnect and reconnect the MCP server in your client to refresh its tool list.

## Troubleshooting

* Invoking the MCP URL without a token returns a 401 — this is correct behaviour, and is what triggers the OAuth flow in your client.
* Verify `https://YOUR-CLOUDLET/.well-known/oauth-authorization-server` returns JSON referencing your real domain with `https://` — this is the discovery document MCP clients use to find the login flow.
* The consent page asks for your Magic username and password — the same credentials you use for your dashboard.
