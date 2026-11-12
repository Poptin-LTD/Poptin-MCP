# Connect Poptin to your AI client

Use `https://mcp.popt.in/mcp` and complete Poptin's OAuth sign-in. Select the account
you want to authorize. Available tools still follow your permissions and enabled
features. Do not add an API key or a static Authorization header.

The routes below follow each client's documentation. They have not all completed
an end-to-end Poptin OAuth test. Marketplace inclusion is separate from installing
or configuring a connection.

## Claude

### Claude web and desktop

Where custom connectors are available, open **Settings → Connectors**, add a
custom remote connector named **Poptin**, and enter `https://mcp.popt.in/mcp`.
Complete sign-in and enable the connector for your conversation. Your plan or
organization may control access to custom connectors.

[Claude's remote connector guide](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

### Claude Code

Add the server directly:

```sh
claude mcp add --transport http --scope user poptin https://mcp.popt.in/mcp
```

In Claude Code, use `/mcp` to authenticate the Poptin connection.

For local plugin testing, clone this repository and run
`claude --plugin-dir /absolute/path/to/Poptin-MCP`. Its
`.claude-plugin/plugin.json` and root `.mcp.json` package the same connection.
Choose either the plugin or a direct configuration to avoid duplicate tools.

[Claude Code MCP guide](https://code.claude.com/docs/en/mcp) ·
[Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference)

## Cursor

Add this entry to your user-level `~/.cursor/mcp.json`, merging it with any
existing servers:

```json
{
  "mcpServers": {
    "poptin": {
      "url": "https://mcp.popt.in/mcp"
    }
  }
}
```

Open Cursor's MCP settings and complete the Poptin authorization flow. For a
project-specific connection, use `.cursor/mcp.json` in that project instead.

The repository also includes `.cursor-plugin/plugin.json` for native plugin
packaging. It explicitly references `.mcp.json`; the portable root `mcp.json`
uses a different transport spelling. Plugin marketplace review is still separate.

[Cursor MCP guide](https://cursor.com/docs/mcp) ·
[Cursor plugin reference](https://cursor.com/docs/reference/plugins)

## Codex

Add the remote server and sign in:

```sh
codex mcp add poptin --url https://mcp.popt.in/mcp
codex mcp login poptin
```

Alternatively, merge this into your Codex `config.toml`, then run the login command:

```toml
[mcp_servers.poptin]
url = "https://mcp.popt.in/mcp"
```

The root `plugin.json` and `mcp.json` are an Agent Plugins package for clients
supporting that format. OpenAI presentation metadata lives in
`extensions.com.openai`. A `.codex-plugin` compatibility overlay is unnecessary
for this portable package. Public directory submission needs additional review
materials; the files alone do not publish a listing.

[Codex MCP guide](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) ·
[OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)

## GitHub Copilot in VS Code

Run **MCP: Add Server** from the Command Palette, choose **HTTP**, enter
`https://mcp.popt.in/mcp`, and name the server `poptin`. Choose user or workspace
configuration and complete the OAuth sign-in prompt.

For workspace configuration, merge [this example](../examples/vscode.mcp.json)
into `.vscode/mcp.json`. Enable the server's tools in Copilot when prompted.
This guide covers VS Code; other Copilot surfaces have their own configuration
and administration requirements.

[VS Code setup](https://code.visualstudio.com/docs/agent-customization/mcp-servers) ·
[Configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration)

## Gemini CLI

Add Poptin as an HTTP server:

```sh
gemini mcp add --transport http poptin https://mcp.popt.in/mcp
```

In an interactive Gemini CLI session, run `/mcp auth poptin` to complete sign-in.
Gemini discovers the server's OAuth endpoints automatically.

For local extension testing, run `gemini extensions link /absolute/path/to/Poptin-MCP`
and restart Gemini CLI. The root `gemini-extension.json` provides the same HTTP
connection. Use one installation method at a time. These instructions cover
Gemini CLI rather than the Gemini consumer chat app.

[Gemini CLI MCP guide](https://geminicli.com/docs/tools/mcp-server/) ·
[Extension reference](https://geminicli.com/docs/extensions/reference/)

## Grok

Where custom connectors are enabled, open [Grok Connectors](https://grok.com/connectors),
choose **New Connector → Custom**, and enter `https://mcp.popt.in/mcp`.
Complete Poptin sign-in and enable the connection in your conversation.

This uses Grok's custom connector flow. It does not require a `.grok-plugin`
directory in this repository.

[Grok connector documentation](https://docs.x.ai/grok/connectors)

## Other MCP clients

Add a remote **Streamable HTTP** connection using `https://mcp.popt.in/mcp`.
The client must support MCP OAuth discovery and browser sign-in. Authorize the
desired Poptin account and enable the connection in your conversation.

If your client only supports local stdio servers or static API keys, this direct
configuration will not work. Consult that client's documentation for remote
OAuth support.

## Check your connection

Ask: “Show me the popups and embedded forms in my Poptin account.”
Confirm that the assistant accesses the account you authorized. An empty result
can be valid. Reconnect if authorization cannot be renewed, and create a separate
connection for another account.
