import pytest
import HTML.Solution.HTMLElement as HTMLElement

arr = [HTMLElement.HTMLElement("h1", "Hello World"), HTMLElement.HTMLElement("p", "test")]
root_element = HTMLElement.HTMLElement("div", arr, {"class": "testing"})
child_element = HTMLElement.HTMLElement("h2", "Hello World", {"class": "testing"})
HTMLElement.HTMLElement.append(root_element, child_element)
HTMLElement.HTMLElement.append(child_element, HTMLElement.HTMLElement("h3", "Hello World"))


def test_duplicate_id() -> None:
    with pytest.raises(ValueError):
        element1 = HTMLElement.HTMLElement("h1", "Hello World", {"id": "test"})
        element2 = HTMLElement.HTMLElement("h2", "Error", {"id": "test"})


def test_invalid_tag() -> None:
    with pytest.raises(ValueError):
        element1 = HTMLElement.HTMLElement("hello", "Hello World", {"id": "test"})


def test_valid_tag() -> None:
    element1 = HTMLElement.HTMLElement("h1", "Hello World", {"id": "testing"})
    assert element1.name == "h1"
    assert element1.children[0] == "Hello World"
    assert element1.attributes == {"id": "testing"}


def test_no_attributes() -> None:
    element1 = HTMLElement.HTMLElement("h1", "Hello World")
    assert element1.name == "h1"
    assert element1.children[0] == "Hello World"
    assert element1.attributes == {}


def test_append() -> None:
    root = HTMLElement.HTMLElement("h1", "Hello World", {"class": "testing"})
    child = HTMLElement.HTMLElement("h1", "Hello World", {"class": "testing"})
    HTMLElement.HTMLElement.append(root, child)
    assert len(root.children) == 2


def test_render() -> None:
    HTMLElement.HTMLElement.render(root_element)


def test_render_html() -> None:
    HTMLElement.HTMLElement.render_html(root_element)


def test_find_by_tag() -> None:
    array = HTMLElement.HTMLElement.find_by_tag(root_element, "div")
    print(array)
