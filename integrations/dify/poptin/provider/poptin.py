from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from client import get_data, PoptinError

class PoptinProvider(ToolProvider):
    def _validate_credentials(self, credentials):
        try:
            get_data(credentials.get("api_key"), "list_campaigns", {"per_page": 1})
        except PoptinError as exc:
            raise ToolProviderCredentialValidationError(str(exc)) from None
