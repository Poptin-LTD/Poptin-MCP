# Security policy

## Scope

This repository contains Poptin MCP documentation, registry metadata, client
configuration, and validation tooling. Poptin operates the hosted MCP server at
`https://mcp.popt.in/mcp`; its implementation is maintained separately.

## Report a vulnerability privately

Contact Poptin through the support options in the
[Poptin Help Center](https://help.poptin.com/en/). Identify your message as a
**Poptin MCP security report** and ask for it to be routed to the MCP maintainers.
Use this route for issues in either this repository or the hosted MCP service.

Do not disclose vulnerabilities through public GitHub issues, discussions, or
pull requests. If you need to share sensitive evidence, first ask support how to
provide it privately.

## What to include

- A description of the issue and its potential impact.
- Reproduction steps or a minimal proof of concept.
- Whether the issue affects this repository or the hosted MCP server.
- For repository issues: the affected file and commit or package version.
- For connection issues: the AI client and version, approximate time and timezone,
  affected MCP operation, and relevant error messages.

Redact passwords, API keys, OAuth tokens, cookies, and customer data from logs and
screenshots. Use accounts and data you are authorized to access when reproducing
an issue.

For ordinary setup questions or product bugs, use
[Poptin support](https://help.poptin.com/en/).

## If you suspect your account or an AI connection is compromised

In Poptin, open **AI connections**, review the connected applications and accounts,
and choose **Revoke** for any connection you do not recognize or no longer trust.
Confirm **Revoke access** to end that connection's access to the authorized account.
If you cannot access these controls, contact Poptin support for help.

Also disable or remove the Poptin connection in your AI application and follow
that application's disconnect or authorization-revocation options. Revoking
access does not undo actions already performed.

Contact Poptin support privately if you suspect unauthorized activity. Reconnect
through Poptin sign-in only when you are ready to authorize access again. See
[the MCP guide's help and common questions](https://developers.poptin.com/docs/mcp#help--common-questions)
for disconnect guidance.
