# Poptin Dify plugin privacy policy

This plugin transmits your configured Public API key in the Authorization header and tool filters (reporting dates, campaign name/status, website domain, pagination) to Poptin at `https://api.popt.in/v1` over verified HTTPS. Credentials are scoped to the Poptin account where they were created. It makes only the four documented GET operations described in the README; provider validation reads one page of campaign data.

The plugin returns successful Poptin API responses to Dify. These can contain account-specific campaign or popup names, domains, identifiers, performance metrics and other information included by those API endpoints. Workflow authors control whether results are subsequently passed to a model provider, other tools, or external destinations. Avoid using personal data in campaign names or filters. No contacts endpoint is called by this plugin.

The plugin itself does not persist user data, credentials, responses, or logs, and includes no analytics, tracking or telemetry service. It keeps data in memory during requests. Dify stores provider credentials and may retain workflow inputs, outputs, traces and conversation history according to the deployment's configuration and privacy policy. Poptin processes requests and may keep service logs under [Poptin's privacy policy](https://www.poptin.com/privacy-policy/). The plugin does not control those services' retention or delete their records.

Only the Poptin API receives requests directly from plugin code. Raw HTTP error bodies and network exception details are suppressed. Successful response payloads are account data and should only be shared with intended workflow users. Revoke a credential in Poptin's API Keys settings and remove the provider credential from Dify to disconnect; this does not erase records already retained by Dify or Poptin.

Questions: support@poptin.com. Effective date: 2026-11-17.
