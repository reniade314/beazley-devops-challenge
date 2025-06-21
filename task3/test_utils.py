import pytest
from utils import get_value_from_path

def test_valid_path():
    data = {"a": {"b": {"c": "value"}}}
    assert get_value_from_path(data, "a.b.c") == "value"

def test_invalid_path():
    data = {"a": {"b": {"c": "value"}}}
    assert "Error" in get_value_from_path(data, "a.x.c")

def test_non_nested_path():
    data = {"a": "hello"}
    assert get_value_from_path(data, "a") == "hello"
