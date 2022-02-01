from kubernetes.config import load_kube_config
from kubernetes.client import ApiClient, Configuration
from kubernetes.config.kube_config import list_kube_config_contexts

def _get_api_client() -> ApiClient:
    load_kube_config()
    _config = Configuration.get_default_copy()
    _config.ssl_ca_cert = "/etc/pki/ca-trust/source/anchors/ca-bundle.crt"

    return ApiClient(_config)

def _get_current_namespace() -> str:
    return list_kube_config_contexts()[1]['context']['namespace']
