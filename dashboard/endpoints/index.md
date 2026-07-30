---
title: Endpoints
description: The Endpoints component in Magic allows you to browse your endpoints and execute these, similarly to how Swagger works.
header:
  image: /assets/images/hero/endpoints-dash.png
  og_image: /assets/images/hero/endpoints-dash-og.png
  image_description: The Endpoints component
faq:
  - q: "What is the Endpoints component?"
    a: "It lets you browse every HTTP endpoint in your cloudlet and invoke them, similarly to how Swagger works - documenting your endpoints and letting you test them from the same screen."
  - q: "How do I parametrise an invocation?"
    a: "When you expand an endpoint, every argument it accepts becomes a typed input field - checkboxes for booleans, date pickers for dates, and so on. CRUD endpoints additionally expose paging, sorting, and per-column filter arguments."
  - q: "Which payload formats are supported?"
    a: "JSON, YAML, Hyperlambda, and XML - all with syntax highlighting - for your POST, PUT and PATCH endpoints. Endpoints consuming multipart/form-data are also supported, rendering one input field per form field, in addition to letting you attach files."
  - q: "Can I get an OpenAPI specification for my endpoints?"
    a: "Yes. Every endpoint has an OpenAPI button giving you its OpenAPI specification. You can copy both the URL and the specification itself, and paste it into another orchestrator LLM or AI agent, allowing the other party to understand your backend."
  - q: "Can I test file uploads and downloads?"
    a: "Yes. You can upload files to endpoints that accept file uploads, and download the files an endpoint returns, directly from the component."
  - q: "What does the response dialog show?"
    a: "The HTTP status code, how many milliseconds the invocation took, the response headers, and the response body with syntax highlighting - plus a button to copy the response."
---

The Endpoints component allows you to see your HTTP endpoints, and invoke these, similarly to how Swagger works. From your endpoints menu item you can search for, parametrise, and invoke your endpoints - Allowing you to simulate a client, to understand how your endpoints work, and _"debug"_ these as you develop them. This component hence serves two purposes; One being documenting your endpoints, another being testing your endpoints.

![Screenshot of the Endpoints component in Magic and how it allows you to execute HTTP endpoints in your cloudlet](/images/endpoints.jpg)

## Parametrising your invocations

When you expand an endpoint, every argument the endpoint accepts becomes an input field, with its type displayed next to its name. For a CRUD read endpoint this means you can page with `limit` and `offset`, sort with `order` and `direction`, and expand the _"Filter arguments"_ section to filter on individual columns - all without writing a single line of code.

![Screenshot of parametrising an endpoint invocation with limit, offset and order arguments](/assets/images/endpoints-parametrising-invocations.jpeg)

When you click _"Invoke"_, the component shows you the response; its HTTP status code, how many milliseconds the invocation took, the response headers, and the response body itself with syntax highlighting. A _"Copy response"_ button lets you bring the result into your own code or documentation.

![Screenshot of the response dialog showing status code, timing, and the JSON response body](/assets/images/endpoints-invocation-response.jpeg)

## OpenAPI specifications

Every endpoint has an _"OpenAPI"_ button, giving you the OpenAPI specification for that particular endpoint - and every _module_ has one too, giving you the specification for all endpoints in the module at once.

![Screenshot of the OpenAPI specification for the chinook module](/assets/images/endpoints-openapi-chinook.jpeg) You can copy both the OpenAPI URL and the specification itself. This is particularly useful when working with AI - copy and paste the OpenAPI specification into some other orchestrator LLM or AI agent, and the other party immediately understands your backend; what endpoints exist, what arguments they take, and what they return - allowing the AI to correctly invoke your API, or generate a frontend consuming it.

The component also allows for uploading and downloading of files - you can upload files to endpoints accepting file uploads, and download the files an endpoint returns, allowing you to test binary and document endpoints directly from the component.

## Your endpoints as MCP tools

Notice, if the [MCP server](/tutorials/how-to-connect-the-mcp-server/) is installed, all endpoints in your system are automatically added as _"tools"_ to the MCP server - implying every endpoint you see in this component is also invocable by a connected AI agent. MCP tool invocations obey the same RBAC requirements as everything else; an agent can only invoke the endpoints its authenticated user's roles permit.

## Hyperlambda endpoint meta data

Hyperlambda endpoints have a type declaration providing some sort of semantic type of information about your endpoint, and typically if this type declaration is _"internal"_, the endpoint is _not_ intended for being consumed by your own code, but only for internal usage by Magic. This meta data is displayed in the endpoint component, and allows you to more easily classify your endpoints, understanding what an endpoint does.

Magic will automatically determine what type your query parameter is, and show the correct form control in its endpoint component for whatever type is required as input to your endpoint. This implies it will show checkbox elements for boolean arguments, date time pickers for date and time arguments, etc. This component also supports providing request payloads to your POST, PUT and PATCH endpoints in all the most common formats - such as JSON, YAML, Hyperlambda, and XML - with syntax highlighting through CodeMirror. In addition you can upload files to endpoints that accept file uploads, and download the files an endpoint returns, allowing you to work with binary and document endpoints directly from the component.

## Endpoint meta data features

As you are browsing your endpoints, and you expand individual items, you'll notice that each endpoint shows you a whole range of _"meta data"_. This gives you high level information about your endpoints, such as:

* Relative URL
* HTTP verb
* Type of endpoint
* What type of data the endpoint consumes (JSON, Hyperlambda, form-data, etc)
* What type of result the endpoint produces
* Humanly readable description of your endpoint
* Authorisation requirements for invoking the endpoint, implying roles users must belong to in order to invoke the endpoint
* Etc, etc, etc

The endpoint's meta information is retrieved directly from your Hyperlambda files. Magic automatically allows you to invoke your user defined endpoints with this component.

The endpoints component in Magic is obviously not as strong as something such as OpenAPI, Swagger, or Postman - But for Hyperlambda endpoints, it's probably more than enough.

{% include faq.html %}
