# Publish Poptin to ClawHub

ClawHub hosts the discoverable plugin listing. The Poptin MCP service continues
to run at `https://mcp.popt.in/mcp`. Publishing runs in GitHub Actions; maintainers
do not need to install ClawHub or OpenClaw on their computers.

## Owner and credentials

The workflow publishes as the ClawHub owner `poptin`. The token's account must
have publishing access to that owner. The bundle's display name is `Poptin` and
OpenClaw derives the runtime ID `poptin` from it. The bundle explicitly sets
the ClawHub catalog ID to `poptin`.
The owner is fixed in the workflow, so each run uses the same publisher.
This flow publishes to ClawHub and does not require an npm account or release.

Store the ClawHub API token in this repository's Actions secret named
`CLAWHUB_TOKEN`. Tokens are created in ClawHub **Settings → API tokens**.
The secret is passed only to the manually invoked publishing workflow.

## Package contents

The dedicated [package directory](../plugins/openclaw/README.md) contains:

- `.cursor-plugin/plugin.json`: one supported bundle marker and Poptin metadata.
- `.mcp.json`: the hosted Streamable HTTP connection and OAuth requirement.
- `assets/icon.png`: Poptin's existing logo at ClawHub's required path.
- `README.md`, `LICENSE`, and `NOTICE.md`: setup, support, and license information.

The workflow selects ClawHub's `bundle-plugin` family. OpenClaw supports the
Cursor-format bundle without requiring Cursor to be installed. This package
contains no JavaScript, native manifest, or npm package metadata.

ClawHub's pinned publisher requires exactly one supported bundle marker.
Publishing this subdirectory avoids the root repository's combined client
formats. Keep the bundle identity, version, description, endpoint, and logo
consistent with the source metadata; repository validation checks these values.
Runtime/OAuth verification is still required before release.

## Preview and publish

1. Merge the reviewed package and workflow into the default branch.
2. Open **Actions → Publish to ClawHub → Run workflow** on the default branch.
3. Leave **Preview the package without publishing** checked for the first run.
   The workflow always selects owner `poptin`.
4. Review the validation reports and `clawhub-package-publish-json` artifact.
   Check the resolved owner, name, version, package files, and source commit.
   Fix validation or ownership errors before continuing.
5. Run the workflow again on the same reviewed commit, with preview
   unchecked. It submits the release and waits for publication checks.
6. Open the resulting listing and verify public discovery. In an OpenClaw
   environment, install the listed package, enable it, complete Poptin OAuth,
   and verify a read-only inventory request before describing it as tested.

The workflow is manual and restricted to the upstream default branch. It uses
the official reusable package workflow pinned to a commit, publishing only
`plugins/openclaw` from the run's checkout, with the repository, commit, and ref
recorded as source attribution. This avoids a second GitHub API fetch of the
same commit. The pinned publisher requires an explicit workflow `version`;
validation checks that it matches the bundle manifest. Its Node/Bun dependencies
are installed on the GitHub runner. No release is published by an ordinary push.

A successful static check does not prove OAuth compatibility or tool execution.
If the publication wait times out, inspect that version's state on ClawHub
before retrying. For later changed releases, increment the package version and
keep the repository's version consistency checks satisfied.

## References

- [ClawHub publishing](https://docs.openclaw.ai/clawhub/publishing)
- [Package CLI and GitHub Actions](https://docs.openclaw.ai/clawhub/cli)
- [ClawHub authentication](https://docs.openclaw.ai/clawhub/auth)
- [OpenClaw bundle formats](https://docs.openclaw.ai/plugins/bundles)
