import importlib
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import Mock
import pytest
import requests
import yaml

ROOT = Path(__file__).resolve().parents[1] / 'poptin'
sys.path.insert(0, str(ROOT))
from client import get_data, validate_parameters, PoptinError, OPERATIONS

@pytest.fixture
def http(monkeypatch):
    response = Mock(status_code=200)
    response.json.return_value = {'data': [], 'meta': {'current_page': 1}}
    call = Mock(return_value=response)
    monkeypatch.setattr(requests, 'get', call)
    return call, response

@pytest.mark.parametrize('operation', OPERATIONS)
def test_fixed_endpoint_and_envelope(operation, http):
    call, response = http
    params = {'stat_from': '2026-10-01', 'stat_to': '2026-10-31'} if 'poptin' in operation else {}
    assert get_data('synthetic-test-key', operation, params) == response.json.return_value
    args, kwargs = call.call_args
    assert args == ('https://api.popt.in/v1' + OPERATIONS[operation][0],)
    assert kwargs == dict(params=params, headers={'Authorization':'Bearer synthetic-test-key','Accept':'application/json'}, timeout=(5,30), allow_redirects=False)
    response.close.assert_called_once()

@pytest.mark.parametrize('params', [
    {}, {'stat_from':'2026-01-01'},
    {'stat_from':'2026-02-30','stat_to':'2026-03-01'},
    {'stat_from':'20260101','stat_to':'2026-03-01'},
    {'stat_from':'2026-04-01','stat_to':'2026-03-01'},
    {'stat_from':'2026-01-01','stat_to':'2026-03-01','device':'tablet'},
    {'stat_from':'2026-01-01','stat_to':'2026-03-01','type':'unknown'},
])
def test_reporting_validation(params, http):
    with pytest.raises(PoptinError):get_data('test', 'list_poptins', params)
    http[0].assert_not_called()

@pytest.mark.parametrize('params', [{'page':0},{'page':True},{'page':1.1},{'page':float('inf')},{'page':'1'},{'per_page':101},{'per_page':-1},{'url':'https://example.com'},{'status':'a\nb'},{'name':'x'*513},{'created_from':'2026-02-31'}])
def test_filter_validation(params, http):
    with pytest.raises(PoptinError):get_data('test', 'list_campaigns', params)
    http[0].assert_not_called()

@pytest.mark.parametrize('key', [None,'','bad\r\nkey','a b'])
def test_invalid_credentials_never_sent(key,http):
    with pytest.raises(PoptinError):get_data(key,'list_campaigns',{})
    http[0].assert_not_called()

@pytest.mark.parametrize('status',[301,302,401,403,422,429,500])
def test_error_redaction(status,http):
    call,response=http;response.status_code=status;response.text='private-key private-customer-data'
    with pytest.raises(PoptinError) as error:get_data('private-key','list_campaigns',{})
    assert 'private' not in str(error.value)
    response.json.assert_not_called()
    response.close.assert_called_once()

@pytest.mark.parametrize('exc',[requests.Timeout('private-key'),requests.ConnectionError('private-key')])
def test_network_errors_sanitized(exc,http):
    http[0].side_effect=exc
    with pytest.raises(PoptinError) as error:get_data('private-key','list_campaigns',{})
    assert 'private-key' not in str(error.value)

@pytest.mark.parametrize('payload',[[],None,'bad'])
def test_bad_response_shape(payload,http):
    http[1].json.return_value=payload
    with pytest.raises(PoptinError):get_data('test','list_campaigns',{})
    http[1].close.assert_called_once()

def test_non_json(http):
    http[1].json.side_effect=ValueError('private-data')
    with pytest.raises(PoptinError,match='invalid JSON'):get_data('test','list_campaigns',{})

def test_numeric_defaults_and_optional_values(http):
    assert validate_parameters('list_campaigns',{'page':1.0,'per_page':100,'name':'','status':None})=={'page':1,'per_page':100}

def test_provider_validates_with_read_only_call(http):
    from provider.poptin import PoptinProvider
    PoptinProvider._validate_credentials(None,{'api_key':'test'})
    assert http[0].call_args.args == ('https://api.popt.in/v1/campaigns',)
    assert http[0].call_args.kwargs['params']=={'per_page':1}

def test_provider_sanitized_failure(http):
    from provider.poptin import PoptinProvider
    from dify_plugin.errors.tool import ToolProviderCredentialValidationError
    http[1].status_code=401
    with pytest.raises(ToolProviderCredentialValidationError):PoptinProvider._validate_credentials(None,{'api_key':'test'})

@pytest.mark.parametrize('operation',OPERATIONS)
def test_sdk_tool_dispatch(operation,http):
    module=importlib.import_module('tools.'+operation)
    tool=module.PoptinTool.from_credentials({'api_key':'test'})
    params={'stat_from':'2026-01-01','stat_to':'2026-01-31'} if 'poptin' in operation else {}
    messages=list(tool._invoke(params))
    assert len(messages)==1
    assert messages[0].message.json_object==http[1].json.return_value

def test_manifest_provider_and_tools_load_in_sdk(monkeypatch):
    monkeypatch.chdir(ROOT)
    from dify_plugin.core.entities.plugin.setup import PluginConfiguration
    from dify_plugin.entities.tool import ToolProviderConfiguration,ToolConfiguration
    manifest=yaml.safe_load((ROOT/'manifest.yaml').read_text())
    PluginConfiguration.model_validate(manifest)
    provider=yaml.safe_load((ROOT/'provider/poptin.yaml').read_text())
    ToolProviderConfiguration.model_validate(provider)
    for filename in provider['tools']:
        ToolConfiguration.model_validate(yaml.safe_load((ROOT/filename).read_text()))
