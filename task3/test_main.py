import pytest
from main import get_value_from_path

def test_valid_key():
    obj = {
        "employee": {
            "details": {
                "name": "Reni"
            }
        }
    }
    assert get_value_from_path(obj, "employee/details/name") == "Reni"

def test_invalid_key():
    obj = {
        "employee": {
            "details": {
                "name": "Reni"
            }
        }
    }
    assert "Error" in get_value_from_path(obj, "employee/details/age")

def test_empty_path():
    obj = {"a": {"b": "c"}}
    assert "Error" in get_value_from_path(obj, "")

def test_non_dict_access():
    obj = {"a": "b"}
    assert "Error" in get_value_from_path(obj, "a/b")
