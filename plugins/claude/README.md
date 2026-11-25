# Poptin for Claude

Connect Claude to your Poptin account to analyze popup and form performance,
manage existing poptins, prepare email campaigns, and organize audiences.
Poptin hosts the MCP server at `https://mcp.popt.in/mcp`. This plugin connects
to that service over HTTP and does not run a local server or install dependencies.

## Connect

For local testing, clone the repository and start Claude Code with:

```sh
claude --plugin-dir /absolute/path/to/Poptin-MCP/plugins/claude
```

Run `/mcp` in Claude Code and complete Poptin's OAuth sign-in. Choose the account
or subaccount to authorize, then ask: “Show me the popups and embedded forms in
my Poptin account.” Confirm that the results belong to the account you chose.
Use either this plugin or a direct MCP configuration to avoid duplicate tools.

## Account access and data

Each connection authorizes one Poptin account. Claude sends tool requests and
their arguments to Poptin's hosted service and receives the requested account
data and action results. Available actions follow your existing permissions and
enabled features. Review campaigns before confirming a send or schedule, and
review destructive actions before approving them.

If sign-in fails, use `/mcp` to reconnect. Do not add an API key or a static
Authorization header. You can revoke the connection in Poptin's **AI connections**
and remove or disable the plugin in Claude.

## Support and licensing

[Poptin MCP guide](https://developers.poptin.com/docs/mcp) ·
[Help Center](https://help.poptin.com/en/) ·
[Privacy policy](https://www.poptin.com/privacy-policy/) ·
[Terms](https://www.poptin.com/terms-of-service/)

The package uses the [MIT license](LICENSE), with branding exclusions in
[NOTICE.md](NOTICE.md).
