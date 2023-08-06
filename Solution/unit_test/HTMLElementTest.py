import pytest
import HTML.Solution.HTMLElement as HTMLElement


def test_duplicate_id():
    with pytest.raises(ValueError):
        element1 = HTMLElement.HTMLElement("h1", "Hello World", {"id": "test"})
        element2 = HTMLElement.HTMLElement("h2", "Error", {"id": "test"})


def test_invalid_tag():
    with pytest.raises(ValueError):
        element1 = HTMLElement.HTMLElement("hello", "Hello World", {"id": "test"})


def test_valid_tag():
    element1 = HTMLElement.HTMLElement("h1", "Hello World", {"id": "testing"})
    assert element1.name == "h1"
    assert element1.value == "Hello World"
    assert element1.attributes == {"id": "testing"}


def test_no_attributes():
    element1 = HTMLElement.HTMLElement("h1", "Hello World")
    assert element1.name == "h1"
    assert element1.value == "Hello World"
    assert element1.attributes == {}
