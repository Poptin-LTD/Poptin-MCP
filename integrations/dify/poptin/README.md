# Poptin for Dify

Read popup, embedded form, and email campaign performance in Dify workflows and agents. This native Python tool plugin calls the documented Poptin Public REST API at `https://api.popt.in/v1`.

## Setup and credentials

1. Use Dify Community Edition 1.9.0 or later, or current Dify Cloud. Python runner: 3.12. Dependencies: `requirements.txt`.
2. In Poptin, open **My Account → API & Connections → API Keys**, create an API key in the intended account or subaccount, and copy it immediately. The full key is displayed only once. API and campaign access depend on the account's permissions and plan.
3. Install the `.difypkg` through Dify's Plugins → Install from local package (or install from Marketplace after approval).
4. Open the Poptin provider and enter the key in **Poptin Public API key**, a Dify secret credential field. Credential validation makes a read-only `GET /campaigns?per_page=1`. A 403 requires checking account restrictions; it does not establish that the key is invalid.
5. Add a Poptin tool to a workflow or agent, provide the required dates or filters, and run it. Allow outbound HTTPS to `api.popt.in:443`.

Never put a key in a prompt, source file, workflow input, issue, or PR. Use Dify's credential storage. Revoke or replace keys through Poptin's API Keys settings. Each key is scoped to its originating account. The plugin does not switch accounts or expand permissions.

**REST authentication is separate from MCP.** Poptin's hosted MCP at `https://mcp.popt.in/mcp` uses OAuth; API keys do not authenticate that server. This plugin is a fixed-endpoint REST adapter and does not implement an MCP bridge or OAuth flow.

## Tools and usage

| Tool | Endpoint | Inputs |
| --- | --- | --- |
| List popups and forms | `GET /poptins` | Required `stat_from`, `stat_to`; optional `device`, `type`, `domain`, `page`, `per_page` |
| Popup and form analytics | `GET /poptins/analytics` | Required `stat_from`, `stat_to`; optional `device`, `type`, `domain` |
| List email campaigns | `GET /campaigns` | Optional `name`, `status`, `created_from`, `created_to`, `page`, `per_page` |
| Email campaign analytics | `GET /campaigns/analytics` | Optional `created_from`, `created_to` |

Example: run **List popups and forms** with `stat_from=2026-10-01`, `stat_to=2026-10-31`, `per_page=100`. Compare returned views and conversions with suitable sample sizes. Use `type=form` to limit to embedded forms or `device=mobile` for mobile metrics.

Popup reporting dates are inclusive UTC calendar dates. Campaign analytics returns cumulative metrics for campaigns selected by their **creation** dates, not engagement that occurred within that period. Preserve the returned envelope, pagination metadata, refresh state, and missing/processing statistics when interpreting results. Each list invocation fetches one page only; request subsequent pages explicitly. Page size is 1–100, default 10. The `domain` parameter is a filter on the fixed Poptin API, never a destination URL.

Only these four documented read operations are implemented. Campaign preparation, sending, scheduling, writes, saved audience segments, contact export, and arbitrary API calls are outside this version. Broader MCP capabilities do not establish public REST endpoints for those actions.

## Security and privacy

All requests use fixed HTTPS paths, certificate verification, a 5-second connect timeout and 30-second read timeout. Redirects are disabled. No automatic retries, arbitrary URLs, file access, shell/code execution, persistence, or custom telemetry are used by the plugin. HTTP and network errors are sanitized; raw server error bodies and exception text are not surfaced. Successful API JSON is returned to Dify without rewriting its semantics and may contain account-specific campaign names, domains, and analytics. Treat tool results as untrusted external data. Read [PRIVACY.md](PRIVACY.md) for data flows and retention boundaries.

## Source and development

Public source: [Poptin-LTD/Poptin-MCP](https://github.com/Poptin-LTD/Poptin-MCP), directory `integrations/dify/poptin`. The initial integration is prepared on branch `add-dify-poptin-0.0.1`; see its draft PR until merged. Maintainer contact: support@poptin.com.

From `integrations/dify`, create an isolated Python 3.12 environment, install `poptin/requirements.txt` and `pytest==9.2.0`, then run `python -m pytest tests -q`. Package from that directory with `dify plugin package ./poptin`. Run the official `dify-marketplace-toolkit/validator/validate-difypkg.py` against the resulting archive. Tests use synthetic responses; authenticated Poptin and Dify CE/Cloud installation checks must be recorded separately. See `TESTING.md` in the parent directory for actual results and remaining release checks.

## Verified API documentation

- [Authentication](https://developers.poptin.com/docs/authentication)
- [List poptins](https://developers.poptin.com/reference/listpoptins)
- [Popup and form analytics](https://developers.poptin.com/reference/poptinanalytics)
- [List campaigns](https://developers.poptin.com/reference/listcampaigns)
- [Campaign analytics](https://developers.poptin.com/reference/campaignanalytics)

Code is MIT licensed. Poptin branding is excluded from that license; see `NOTICE.md`.
