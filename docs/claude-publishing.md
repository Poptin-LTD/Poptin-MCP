# Submit Poptin to Claude's directory

The Claude plugin is **`plugins/claude`**, not the repository root. Submit that
folder so unrelated client packages, workflows, and registry files stay outside
the plugin reviewed by Anthropic. This package uses only metadata, text, and a
PNG image, with no local server code; directory approval remains separate.

## Package boundary

The distribution contains exactly six files: the manifest and PNG icon inside
`.claude-plugin`, plus `.mcp.json`, `README.md`, `LICENSE`, and `NOTICE.md` at the
package root. CI enforces this file set, shared identity/version/description,
license consistency, icon requirements, and the hosted endpoint. Claude metadata
is allowed only in `plugins/claude/.claude-plugin`; do not restore a root copy.

The package's `.mcp.json` matches the root `.mcp.json`: `type: "http"` and the
Poptin URL. Claude discovers OAuth and users authenticate through `/mcp`; do not
copy OpenClaw's `auth: "oauth"` field into this package. The root `.mcp.json`
remains because Cursor's manifest references it. The portable root `mcp.json`
uses `streamable-http`, as required by its own schema. These are client-specific
spellings for the same hosted transport.

## Validate and submit

1. Run the repository's Validate workflow. From the repository root, also run:

   ```sh
   claude plugin validate plugins/claude --strict
   claude --plugin-dir /absolute/path/to/Poptin-MCP/plugins/claude
   ```

   In Claude Code, use `/mcp` to sign in and verify a read-only request against
   the intended Poptin account. CLI validation checks structure; it does not
   establish OAuth connectivity or directory acceptance.
2. Merge the reviewed change to the branch the directory should follow.
3. Open the [developer portal](https://claude.ai/directory/manage). Create a
   **Plugin bundle** submission with repository `Poptin-LTD/Poptin-MCP` and
   **Plugin path `plugins/claude`**. Select the intended branch or tag; leaving
   it blank follows the default branch.
4. Run the portal's **Validate** on the merged commit and resolve any findings.
   Check the listing, icon, data handling answers, and compliance details before
   submitting for review. If the Poptin remote server has not been submitted as
   an MCP connector, Anthropic asks that it be submitted separately too.
5. Follow the submission's review and publishing status in the portal. A clean
   CLI result does not guarantee directory approval.

A previously submitted root package cannot have its repository/folder changed:
create a new submission for `plugins/claude`. Resolve or withdraw the old root
submission in the portal as appropriate. If a submission already targets this
folder, continue it instead of creating a duplicate. For a rejected submission
at the same path, use **Resubmit for review**; for a non-rejected failed version,
use **Check for new commits** after pushing the fix.

References: [Anthropic's submission guide](https://claude.com/docs/plugins/submit),
[pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist),
[manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference),
and [MCP configuration](https://code.claude.com/docs/en/mcp).
