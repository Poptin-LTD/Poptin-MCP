"""Fixed-endpoint, read-only Poptin Public API client."""
from datetime import date
import math
import requests

BASE_URL = "https://api.popt.in/v1"
OPERATIONS = {
    "list_poptins": ("/poptins", {"stat_from", "stat_to", "device", "type", "domain", "page", "per_page"}),
    "poptin_analytics": ("/poptins/analytics", {"stat_from", "stat_to", "device", "type", "domain"}),
    "list_campaigns": ("/campaigns", {"name", "status", "created_from", "created_to", "page", "per_page"}),
    "campaign_analytics": ("/campaigns/analytics", {"created_from", "created_to"}),
}

class PoptinError(Exception):
    """Safe message suitable for a workflow result."""


def validate_parameters(operation, parameters):
    if operation not in OPERATIONS:
        raise PoptinError("Unsupported operation.")
    allowed = OPERATIONS[operation][1]
    if set(parameters) - allowed:
        raise PoptinError("Unsupported parameter.")
    params = {k: v for k, v in parameters.items() if v is not None and v != ""}
    for key, value in list(params.items()):
        if key in {"page", "per_page"}:
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or int(value) != value:
                raise PoptinError("Pagination values must be whole numbers.")
            if value < 1 or (key == "per_page" and value > 100):
                raise PoptinError("Page must be positive; per_page must be between 1 and 100.")
            params[key] = int(value)
        else:
            if not isinstance(value, str) or len(value) > 512 or any(ord(c) < 32 for c in value):
                raise PoptinError("Filters must be strings of at most 512 characters without control characters.")
            if key in {"stat_from", "stat_to", "created_from", "created_to"}:
                try:
                    parsed = date.fromisoformat(value)
                    if parsed.isoformat() != value:
                        raise ValueError()
                except ValueError:
                    raise PoptinError("Dates must use YYYY-MM-DD.") from None
    for start, end in [("stat_from", "stat_to"), ("created_from", "created_to")]:
        if start in params and end in params and params[start] > params[end]:
            raise PoptinError("Start date must not be after end date.")
    if operation in {"list_poptins", "poptin_analytics"}:
        if not {"stat_from", "stat_to"} <= params.keys():
            raise PoptinError("stat_from and stat_to are required.")
        for key, choices in {"device": {"desktop", "mobile"}, "type": {"popup", "form"}}.items():
            if key in params and params[key] not in choices:
                raise PoptinError("Unsupported device or product type.")
    return params


def get_data(api_key, operation, parameters):
    params = validate_parameters(operation, parameters)
    if not isinstance(api_key, str) or not api_key.strip() or any(c.isspace() for c in api_key):
        raise PoptinError("Configure a valid Poptin Public API key in the provider credentials.")
    # Never accept a user-supplied URL or follow redirects with a credential.
    try:
        response = requests.get(
            BASE_URL + OPERATIONS[operation][0], params=params,
            headers={"Authorization": "Bearer " + api_key, "Accept": "application/json"},
            timeout=(5, 30), allow_redirects=False,
        )
    except requests.RequestException:
        raise PoptinError("Poptin connection failed or timed out. Try again later.") from None
    try:
        status = response.status_code
        errors = {
            401: "Poptin rejected the API key. Check or replace the provider credential.",
            403: "Poptin denied access. Check account permissions and plan restrictions.",
            422: "Poptin rejected the filters. Check them against the API documentation.",
            429: "Poptin rate limit reached. Wait before retrying.",
        }
        if status != 200:
            raise PoptinError(errors.get(status, "Poptin returned an unexpected HTTP status. Try again later."))
        try:
            data = response.json()
        except ValueError:
            raise PoptinError("Poptin returned invalid JSON.") from None
        if not isinstance(data, dict):
            raise PoptinError("Poptin returned an unexpected response shape.")
        return data
    finally:
        response.close()
