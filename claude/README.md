# Poptin for Claude

Connect Claude to your Poptin account to inspect marketing performance and manage
supported popup, form, email campaign, segment, and contact-property workflows.

This self-contained directory is the Claude plugin submission root. Submit the
`claude/` folder, not the repository root. Development tooling and other clients
remain outside this package.

## Connection

The declared connector is Poptin's hosted MCP server at
`https://mcp.popt.in/mcp`, using Streamable HTTP and OAuth. Sign in to Poptin,
select one account, and approve access. Poptin API keys cannot authenticate this
server. Existing account permissions and enabled features still apply.

Sending or scheduling campaigns and destructive changes require review and
confirmation. Creating popups and editing their visual design are not supported.
This package does not include the hosted server implementation.

## Help and policies

- [Connection guide](https://developers.poptin.com/docs/mcp)
- [Support](https://help.poptin.com/en/)
- [Privacy policy](https://www.poptin.com/privacy-policy/)
- [Terms of service](https://www.poptin.com/terms-of-service/)
- [License](LICENSE) and [branding notice](NOTICE.md)

Version 1.0.1 changes packaging only, not the hosted server. It does not claim
directory approval.
