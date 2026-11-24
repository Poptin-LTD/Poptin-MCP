from dify_plugin import Tool
from client import get_data, PoptinError

class PoptinTool(Tool):
    def _invoke(self, tool_parameters):
        try:
            result = get_data(self.runtime.credentials.get("api_key"), "list_campaigns", tool_parameters)
        except PoptinError as exc:
            raise PoptinError(str(exc)) from None
        yield self.create_json_message(result)
