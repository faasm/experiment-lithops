#!/usr/bin/python3
from subprocess import check_output
import yaml
import os

PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BASE_DIR = os.path.dirname(PROJ_ROOT) + "/experiment-base"
CONFIG_FILE = "{}/.lithops_config".format(PROJ_ROOT)


def get_key():
    key = (
        check_output(
            "inv -r {} azure.storage-account-get-key lithops".format(BASE_DIR),
            shell=True,
        )
        .decode("utf-8")
        .split("\n")[1]
    )
    return key


def get_endpoint():
    endpoint = (
        check_output("inv -r {} knative.get-service-ip".format(BASE_DIR), shell=True)
        .decode("utf-8")
        .split("\n")[1]
    )
    return endpoint


def update_config():
    with open(CONFIG_FILE) as f:
        doc = yaml.load(f)

    print("Detected Istio Ingress endpoint: https://{}:80".format(endpoint))

    doc["azure_blob"]["storage_account_key"] = key
    doc["knative"]["istio_endpoint"] = "http://{}:80".format(endpoint)

    with open(CONFIG_FILE) as f:
        yaml.dump(doc, f)


if __name__ == "__main__":
    update_config()
