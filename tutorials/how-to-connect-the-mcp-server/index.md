---
title: How to connect the MCP server
description: Connect Claude, Cursor, and any MCP client to your Magic cloudlet over OAuth, giving the AI secure access to your backend, data, and Hyperlambda Generator.
header:
  image: /assets/images/hero/mcp.png
  og_image: /assets/images/hero/mcp-og.png
  image_description: The Magic MCP server
---

**Prerequisite** - This tutorial assumes you already have Magic up running. If you don't, visit [Getting Started](/getting-started/) first.

Magic comes with an integrated MCP server, allowing you to connect AI clients such as Claude, Claude Code, Codex, Cursor, and anything else supporting the [Model Context Protocol](https://modelcontextprotocol.io) to your cloudlet. Once connected, the AI can discover and invoke your backend's endpoints as MCP _"tools"_ — and since the Hyperlambda Generator itself is exposed as a tool, the AI can even _create new tools on demand_, by generating Hyperlambda endpoints for you.

## Installing the MCP server

The MCP server is delivered as two plugins you install through your dashboard. Open your dashboard, go to _"Plugins"_, and install the following two plugins.

* __oauth__ - The OAuth 2.1 authorization server, allowing MCP clients to authenticate through the normal browser login and consent flow
* __mcp__ - The MCP server itself, exposing your endpoints as tools

You can read more about installing plugins [here](/dashboard/plugins/). Once both plugins are installed, the MCP server is live, and its URL is your cloudlet's domain followed by the path below.

```
https://YOUR-CLOUDLET/magic/modules/mcp/mcp
```

That URL is all you need. Magic's MCP server supports OAuth 2.1 with automatic discovery and client registration, so there are no tokens to copy and paste — when you add the URL to your MCP client, it will open your browser, ask you to log in with your Magic username and password, and ask for your consent. Once you click _"Allow"_, the client is connected, and acts on your behalf, with your user's roles.

Once the MCP module is installed, your dashboard's landing page shows a _"This cloudlet is an AI agent"_ panel containing this exact URL, together with a _"Copy MCP URL"_ button - so you never have to construct it by hand.

![The Copy MCP URL button on the Magic dashboard](/assets/images/mcp-dashboard-copy-url.png)

## Adding the connector

You add your MCP URL to your AI client as a custom connector. Below is Claude's own _"Connectors"_ settings, with the Magic MCP server added and ready to connect.

![Adding the Magic MCP server as a connector in Claude](/assets/images/mcp-add-magic-connector.png)

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

## Built-in tools the MCP server exposes

In addition to your own endpoints, the MCP server ships with a large library of built-in tools, grouped by area. Below is an overview of the most important groups, with a standout tool from each - your connected AI can use all of these, subject to your user's roles.

* **Hyperlambda** - generate and run backend code. `generate-hyperlambda` turns a plain-English description into working Hyperlambda, while `execute-hyperlambda` and `execute-file` run it.
* **Modules & endpoints** - scaffold entire APIs. `crudify` generates a complete CRUD backend wrapping a database, alongside `create-sql-endpoint`, `create-module` and `get-openapi-spec`.
* **Database** - work with SQL databases. `execute-sql` and `select-sql` run queries, with `get-database-schema`, `create-sqlite-database` and `create-database-backup` for management.
* **Files** - read and write the cloudlet's file system. `read-file` and `create-file` edit files, with `list-files`, `search-files` and `download-from-web` for the rest.
* **Machine Learning** - build AI chatbots and models. `crawl-website` scrapes a website into training data, with `create-type`, `vectorize-type` and `create-ai-function`.
* **Browser automation** - drive a headless browser. `puppeteer-goto` opens a page and `puppeteer-content` scrapes it, with click, fill, screenshot and evaluate tools for everything in between.
* **Git & GitHub** - version control your work. `git-commit` and `git-push` save changes, with `git-clone-repo` and `github-create-repo`.
* **Users & roles** - manage RBAC access. `create-user`, `list-users`, `create-role` and `add-to-role`.
* **Tasks** - schedule background jobs. `create-task` and `schedule-task`, plus `list-tasks`.
* **Plugins** - extend the cloudlet on the fly. `install-plugin` and `list-plugins`.
* **Misc & integrations** - the glue that ties everything together. `invoke-http` calls any external HTTP API, `send-email` sends mail, `execute-python` and `execute-terminal-command` run code, `generate-image` creates images, and `list-endpoints` / `list-slots` let the AI introspect what your cloudlet can do.

Every one of these runs with the roles of the user who consented, so the AI can only ever do what that user is itself allowed to do.

## Creating new tools with AI

Because the Hyperlambda Generator is itself available over MCP, a connected AI client can create new endpoints for you — you describe what you want in plain English, the generator creates the Hyperlambda, and the new endpoint immediately becomes available as a tool. This turns your cloudlet into a backend the AI can both _use_ and _extend_, while your data stays in your own database, behind your own authorization.

Notice, some clients cache the tool list at the moment you connect. If you have created new endpoints and they don't show up as tools, disconnect and reconnect the MCP server in your client to refresh its tool list.

## Troubleshooting

* Invoking the MCP URL without a token returns a 401 — this is correct behaviour, and is what triggers the OAuth flow in your client.
* Verify `https://YOUR-CLOUDLET/.well-known/oauth-authorization-server` returns JSON referencing your real domain with `https://` — this is the discovery document MCP clients use to find the login flow.
* The consent page asks for your Magic username and password — the same credentials you use for your dashboard.
