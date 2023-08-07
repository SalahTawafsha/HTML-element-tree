import pytest
from HTML.Solution.HTMLElement import HTMLElement

arr = [HTMLElement("h1", "Hello World"), HTMLElement("p", "test")]
root_element = HTMLElement("div", arr, {"class": "testing"})
child_element = HTMLElement("h2", "Hello World", {"class": "testing"})
HTMLElement.append(root_element, child_element)
HTMLElement.append(child_element, HTMLElement("h2", "Hello World"))


def test_duplicate_id() -> None:
    with pytest.raises(ValueError):
        element1 = HTMLElement("h1", "Hello World", {"id": "test"})
        element2 = HTMLElement("h2", "Error", {"id": "test"})


def test_invalid_tag() -> None:
    with pytest.raises(ValueError):
        element1 = HTMLElement("hello", "Hello World", {"id": "test"})


def test_valid_tag() -> None:
    element1 = HTMLElement("h1", "Hello World", {"id": "testing"})
    assert element1.name == "h1"
    assert element1.children[0] == "Hello World"
    assert element1.attributes == {"id": "testing"}


def test_no_attributes() -> None:
    element1 = HTMLElement("h1", "Hello World")
    assert element1.name == "h1"
    assert element1.children[0] == "Hello World"
    assert element1.attributes == {}


def test_append() -> None:
    root = HTMLElement("h1", "Hello World", {"class": "testing"})
    child = HTMLElement("h1", "Hello World", {"class": "testing"})
    HTMLElement.append(root, child)
    assert len(root.children) == 2


def test_render() -> None:
    HTMLElement.render(root_element)


def test_render_html() -> None:
    HTMLElement.render_html(root_element)


def test_find_by_tag() -> None:
    array = HTMLElement.find_by_tag(root_element, "h2")
    assert len(array) == 2


def test_find_by_attribute() -> None:
    array = HTMLElement.find_by_attribute(root_element, "class", "testing")
    assert len(array) == 2
