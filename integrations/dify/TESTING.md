# Poptin Dify 0.0.1 validation record

Prepared 2026-11-17. Source is `poptin/`; test code is `tests/`.

## Completed locally

- Official REST documentation reviewed: authentication, listpoptins, poptinanalytics, listcampaigns, campaignanalytics. Documented host is `https://api.popt.in/v1`; API keys are bearer tokens. MCP OAuth is a separate protocol and is not used by this adapter.
- Duplicate checks: all-state GitHub PR search for Poptin in langgenius/dify-plugins, repository code search, top-level tree scan, GitHub repository search for Poptin+Dify, and public web search for marketplace listings. No matches found. Search/index coverage is not proof of absolute absence.
- Python 3.12, `dify-plugin==0.11.1`, `requests==2.34.2`, `pytest==9.2.0`.
- `python -m pytest integrations/dify/tests -q`: **47 passed**. Synthetic HTTP responses only. Covers fixed paths, bearer headers, timeouts, redirects disabled, input/date validation, pagination, HTTP/network/JSON errors, sanitized credential failures, provider validation, SDK schema loading, and all four SDK tool dispatch paths.
- Two SDK warnings: gevent late SSL monkey-patching in the pytest process; Pydantic class-based configuration deprecation. Neither represents a plugin test failure. The runtime imports the SDK before requests.
- Official toolkit `test-plugin-install.py` with `INSTALL_METHOD=serverless`, from `integrations/dify`: **success**, Flask SDK runtime started and responded on local port 8080. This is an SDK boot smoke check, not a Dify CE/Cloud installation test.
- Unauthenticated read-only `GET https://api.popt.in/v1/campaigns?per_page=1`: **401**, expected documented authentication envelope. No customer credential used; no marketing sends or writes performed.
- `dify plugin package ./poptin` with official Dify CLI 0.6.15: package builds. Archive entries inspected: source, manifest, provider/tool YAML, README, privacy/license/notice, icon, requirements, `.difyignore` only; no tests, environments, caches, secrets, or executable binaries.
- Official `langgenius/dify-marketplace-toolkit` local package validator run including online OSV lookup: zero blocking failures. Outbound-domain and dependency reports are informational: declared fixed host is api.popt.in, dynamically concatenated fixed operation paths; no known vulnerabilities reported for the two pinned direct dependencies. This is not a transitive dependency audit.

## Remaining release gates

- No Poptin Public API credential was provided for this task. Authenticate through Dify's provider credential UI and verify all four tools against a known account, including nonempty datasets, pagination, current permissions, and analytics semantics. Never paste credentials into an issue or PR.
- Install and test the final archive on current Dify Community Edition and/or Dify Cloud, including remote debugging. No CE/Cloud end-to-end run has been completed. Version 1.9.0 is a declared floor, not an independently verified compatibility claim.
- Merge/review the public source draft PR, review support/branding metadata, and keep the Marketplace PR draft until the missing checks are completed.

Package validator reports and SHA-256 for the submitted bytes are included in the Marketplace draft PR. The source tree deliberately does not commit a duplicate package artifact.
