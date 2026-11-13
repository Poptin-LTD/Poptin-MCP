# Publishing and validation

This repository is the public documentation and distribution companion for
Poptin's hosted MCP server. It contains no server implementation. Preparing or
validating these files does not publish a listing. Commit and push changes only
when the maintainer chooses to do so.

## Package map

| File | Consumer |
| --- | --- |
| `server.json` | Official MCP Registry metadata |
| `plugin.json` + `mcp.json` | Portable Agent Plugins package, including Codex presentation metadata |
| `.claude-plugin/plugin.json` + `.mcp.json` | Native Claude plugin |
| `.cursor-plugin/plugin.json` + `.mcp.json` | Native Cursor plugin |
| `gemini-extension.json` | Gemini CLI extension |
| `examples/vscode.mcp.json` | Copyable VS Code / GitHub Copilot configuration |

Portable MCP uses `streamable-http`, native Claude/Cursor and VS Code use `http`,
and Gemini CLI uses `httpUrl`. These all target `https://mcp.popt.in/mcp`.
Keep the release version and description consistent across manifests.

The registry's optional `repository` field describes server source code. It is
omitted because this public repository contains metadata rather than the hosted
implementation. Plugin manifests do link to this public package repository.

## Run validation

Validation is defined explicitly in .github/workflows/validate.yml using
Python 3.12 and pinned jsonschema and PyYAML dependencies. There is no separate
executable script or development dependency manifest in the distributed root.

Pushes and pull requests run schema, endpoint, version, image, local-document,
workflow-permission, root-package file-type and public-link checks. A manual
Run workflow can skip public-link checking. The workflow has read-only
permissions and never publishes. Existing schema and integration checks are
preserved; validation code is visible in the workflow, not hidden in an asset.

Where Claude Code is installed, run "claude plugin validate . --strict" too.
Repository checks do not replace client-runtime tests or directory review.
Missing pages (404/410) fail; rate limits and network failures are reported as
unverified. Dynamic badges and Grok's signed-in installation route are skipped.

## Official MCP Registry

1. Review `server.json`, the README, and the live OAuth discovery documents.
2. Commit and push the intended public files using your normal review process.
3. Install the official publisher: `brew install mcp-publisher`.
4. Run `mcp-publisher login github` using an identity authorized to publish under
   the **Poptin-LTD organization**. Check organization access if namespace
   authorization fails; do not publish under an employee's namespace as a workaround.
5. From this directory, run `mcp-publisher publish server.json`.
6. Search the registry for `io.github.Poptin-LTD/poptin` and verify its version,
   endpoint, and active/latest status.

No npm, PyPI, or Docker package is required for a remote-only listing. Users
still authenticate to Poptin with OAuth; registry publisher authentication is
separate from customer sign-in. Bump the version before publishing an update;
do not assume that a published version can be overwritten.

[Remote publishing](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/remote-servers.mdx) ·
[Namespace authentication](https://modelcontextprotocol.io/registry/authentication) ·
[Publisher commands](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/cli/commands.md)

## GitHub and client marketplaces

GitHub's MCP catalog has a separate onboarding step. After publishing to the
official registry, request consideration with the registry name, live entry,
version, endpoint, OAuth authentication, public repo, license scope, and a short
description. Publication upstream does not guarantee inclusion.

[GitHub onboarding discussion](https://github.com/github/github-mcp-server/discussions/1257)

For Claude and Cursor, submit the public repo through their plugin submission
routes after testing the native package. For Gemini CLI, test the extension
before requesting gallery inclusion. Copilot in VS Code and Grok can use the
direct connection routes in the [client guide](clients.md).

For OpenAI, the root manifest is a source package, **not a completed public
submission**. Initial review preparation still needs:

- The intended verified publisher identity and supported countries.
- Confirmation of whether the integration involves purchases and where they occur.
- Confirmation that the published privacy policy and terms cover the MCP integration.
- A dedicated reviewer account with appropriate sample data and feature access.
- A real, reviewer-accessible demo recording and executed review cases.

The public policy and support links are populated from Poptin's existing pages.
Their presence does not establish integration-specific policy coverage. Keep
reviewer credentials in the portal's secure fields, never this repo or an archive.
Country targeting and commerce declarations are intentionally absent until confirmed.

[OpenAI packaging](https://developers.openai.com/plugins/build/plugins) ·
[OpenAI submission](https://developers.openai.com/plugins/deploy/submission) ·
[Cursor submission reference](https://cursor.com/docs/reference/plugins) ·
[Gemini extension reference](https://geminicli.com/docs/extensions/reference/)

## Connection tests

Recorded on **November 12, 2026**:

| Check | Status | Evidence |
| --- | --- | --- |
| Repository schemas and consistency | Passed | Registry and portable JSON schemas; native endpoints; versions; image files; local docs; workflow YAML |
| Validator failure checks | Passed | Rejected wrong endpoints, static credentials, version drift, missing files/headings, escaping paths, duplicate keys, and workflow write permissions |
| Branding assets | Passed | Banner rendered and inspected; square icon rendered from existing Poptin vector artwork at 256 × 256 |
| Public protected-resource discovery | Passed | Advertises `https://mcp.popt.in/mcp`, issuer `https://app.popt.in/mcp-oauth`, scope `mcp:use` |
| Authorization-server discovery | Passed | Advertises authorization code + refresh, S256 PKCE, client registration, and CIMD support |
| Unauthenticated MCP initialization | Passed | Returns HTTP 401 with a protected-resource metadata challenge |
| Complete OAuth sign-in and token renewal | Not run here | Requires an interactive Poptin login in each intended client |
| Claude / Cursor / Codex / VS Code / Gemini CLI / Grok | Not run here | Record exact client version, setup route, authorized test account, and result after testing |
| Marketplace approval | Not submitted here | Track each marketplace separately |

After sign-in, list popups and forms, check that the correct account is used,
verify reconnection and revocation, and exercise the features intended for each
listing. Use a dedicated test account for changes or external sends. Never
infer full OAuth compatibility from a successful discovery request.

## Review cases and demo

Five positive and three negative draft cases are embedded in
`plugin.json` under `extensions.com.openai.review.test_cases`. **All are not run.**
They cover inventory, reporting, email campaign inspection, segment preview,
contact properties/topics, and three unsupported requests. Prepare the fixtures
described in each case, compare actual tool calls and results with its expected
behavior, and record pass/fail evidence before submission.

For a short demo, show the installed package/version and sign in using a dedicated
test account. List its popups and forms, ask for a performance summary, preview an
audience without saving, and demonstrate the unsupported popup-design request.
Capture actual prompts and results, hide credentials and unrelated account data,
and verify playback before adding the recording URL to the OpenAI review metadata.
A script is not a completed recording.

Prepare a clean plugin archive only after selecting the target format and
completing its review requirements. Include the manifests, connection configuration,
referenced artwork, license, and notice. Exclude `.git`, `.venv`, workflow tooling,
and credentials. No account upload, publication, or automatic release workflow
is configured in this repository.

## Claude directory submission package

Use the repository root as the plugin path. Version **1.0.2** removes the
duplicate Claude subfolder and SVG sources, uses existing PNG artwork, and
keeps validation in the read-only GitHub workflow. All client manifests share
the release version. Endpoints, OAuth behavior and other client configurations
are unchanged.

The Claude manifest is .claude-plugin/plugin.json; .claude-plugin/ alone
is not the plugin root because it excludes the sibling MCP configuration.

After merging, rerun directory checks against the new commit and root path.
This cleanup does not establish directory acceptance. In particular, the
portable mcp.json and other clients' metadata remain intentionally available;
any directory discovery or policy finding about those must be reviewed rather
than deleting an integration merely to suppress a warning. No directory
submission or client runtime test is performed by repository validation.
