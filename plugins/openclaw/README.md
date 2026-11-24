# Poptin for OpenClaw

Connect OpenClaw to your Poptin account to explore popup and form performance,
manage existing poptins, prepare email campaigns, and organize audiences.
Poptin hosts the MCP server at `https://mcp.popt.in/mcp`.

This package uses the Cursor bundle format supported by OpenClaw. It contains
connection metadata, documentation, and artwork; no JavaScript entry point or
Cursor installation is required. Authentication is OAuth;
Poptin API keys cannot authenticate this connection.

## Install and connect

1. Use the install command on this package's published ClawHub listing.
2. Enable the Poptin plugin in OpenClaw.
3. Open the plugin's account settings and complete Poptin sign-in. Choose the
   account or subaccount you want to authorize.
4. Start a new conversation and ask: “Show me the popups and embedded forms in
   my Poptin account.” Confirm that the results belong to the account you chose.

Each connection authorizes one Poptin account. Actions follow your existing
permissions and enabled features. Review email campaigns before confirming a
send or schedule; review destructive actions before approving them.
Creating popups or editing their visual design is not available in this release.

## Connection troubleshooting

If the installed plugin does not offer OAuth sign-in, use OpenClaw's
**Settings → MCP** to configure the same server name, `poptin`, with URL
`https://mcp.popt.in/mcp`, transport `streamable-http`, and `auth: "oauth"`
in its scoped configuration editor. An explicit server configuration overrides
the plugin default. Complete sign-in and verify a read-only tool call.

See [OpenClaw's MCP guide](https://docs.openclaw.ai/tools/mcp) and
[MCP account settings](https://docs.openclaw.ai/cli/mcp/control-ui).
Package validation does not verify OAuth or authenticated tool calls. This
integration's end-to-end OpenClaw connection has not yet been verified.

## Support and licensing

[Poptin MCP guide](https://developers.poptin.com/docs/mcp) ·
[Help Center](https://help.poptin.com/en/) ·
[Privacy policy](https://www.poptin.com/privacy-policy/) ·
[Terms](https://www.poptin.com/terms-of-service/)

The package uses the [MIT license](LICENSE), with branding exclusions in
[NOTICE.md](NOTICE.md).
