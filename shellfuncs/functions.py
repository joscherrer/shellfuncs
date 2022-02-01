import re
import json
import sys
from shellfuncs.utils import _get_api_client, _get_current_namespace
from kubernetes.client.api import CoreV1Api

def oclabel(namespace=None, _filter=None):
    """"""
    if not namespace:
        namespace = _get_current_namespace()
    if not _filter and len(sys.argv) > 1:
        _filter = sys.argv[1]

    apps_api = CoreV1Api(_get_api_client())
    pods = apps_api.list_namespaced_pod(namespace)

    filtered = []
    by_label = {}

    for pod in pods.items:
        if _filter in pod.metadata.name:
            filtered.append(pod.metadata.name)

    filtered.sort()

    for pod in pods.items:
        for label, value in pod.metadata.labels.items():
            key = "=".join([label, value])
            if key not in by_label:
                by_label[key] = []
            by_label[key].append(str(pod.metadata.name))

    for label, pods in by_label.items():
        pods.sort()
        if pods == filtered:
            print(label)

    # print(json.dumps(by_label))