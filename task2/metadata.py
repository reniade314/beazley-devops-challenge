import requests

AZURE_METADATA_URL = "http://169.254.169.254/metadata/instance?api-version=2021-02-01"

def get_metadata():
    headers = {"Metadata": "true"}
    response = requests.get(AZURE_METADATA_URL, headers=headers)
    response.raise_for_status()
    return response.json()

def get_metadata_key(key_path):
    metadata = get_metadata()
    keys = key_path.split(".")
    value = metadata
    for key in keys:
        value = value.get(key)
        if value is None:
            raise KeyError(f"Key path '{key_path}' not found.")
    return value
