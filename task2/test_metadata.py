import pytest
from metadata import get_metadata_key

sample_metadata = {
    "compute": {"name": "test-vm", "location": "centralus"},
    "network": {"interface": [{"ipv4": {"ipAddress": [{"privateIpAddress": "10.0.0.5"}]}}]}
}

def test_valid_key(monkeypatch):
    monkeypatch.setattr("metadata.get_metadata", lambda: sample_metadata)
    assert get_metadata_key("compute.name") == "test-vm"

def test_nested_key(monkeypatch):
    monkeypatch.setattr("metadata.get_metadata", lambda: sample_metadata)
    assert get_metadata_key("network.interface") == [{"ipv4": {"ipAddress": [{"privateIpAddress": "10.0.0.5"}]}}]

def test_invalid_key(monkeypatch):
    monkeypatch.setattr("metadata.get_metadata", lambda: sample_metadata)
    with pytest.raises(KeyError):
        get_metadata_key("compute.invalid")
