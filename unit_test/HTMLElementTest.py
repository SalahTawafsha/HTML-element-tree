import pytest
from HTML.Solution.html_element import HtmlElement

arr = [HtmlElement("h1", "Hello World"), HtmlElement("p", "test")]
root_element = HtmlElement("div", arr, {"class": "testing"})
child_element = HtmlElement("h2", "Hello World", {"class": "testing"})
HtmlElement.append(root_element, child_element)
HtmlElement.append(child_element, HtmlElement("h2", "Hello World"))


def test_duplicate_id() -> None:
    with pytest.raises(ValueError):
        element1 = HtmlElement("h1", "Hello World", {"id": "test"})
        element2 = HtmlElement("h2", "Error", {"id": "test"})


def test_invalid_tag() -> None:
    with pytest.raises(ValueError):
        element1 = HtmlElement("hello", "Hello World", {"id": "test"})


def test_valid_tag() -> None:
    element1 = HtmlElement("h1", "Hello World", {"id": "testing"})
    assert element1.name == "h1"
    assert element1.children[0] == "Hello World"
    assert element1.attributes == {"id": "testing"}


def test_no_attributes() -> None:
    element1 = HtmlElement("h1", "Hello World")
    assert element1.name == "h1"
    assert element1.children[0] == "Hello World"
    assert element1.attributes == {}


def test_html_element_value() -> None:
    element = HtmlElement("div", HtmlElement("h1", "hello"))
    assert len(element.children) == 1


def test_html_element_list() -> None:
    element = HtmlElement("div", arr)
    assert len(element.children) == 2


def test_append() -> None:
    root = HtmlElement("h1", "Hello World", {"class": "testing"})
    child = HtmlElement("h1", "Hello World", {"class": "testing"})
    HtmlElement.append(root, child)
    assert len(root.children) == 2


def test_render() -> None:
    string: str = HtmlElement.render(root_element)
    assert string == "<div class='testing'>\n\t<h1>\n\t\tHello World\n\t</h1>\n\t<p>\n\t\ttest\n\t</p>\n\t<h2 " \
                     "class='testing'>\n\t\tHello World\n\t\t<h2>\n\t\t\tHello World\n\t\t</h2>\n\t</h2>\n</div>\n"


def test_render_html() -> None:
    string: str = HtmlElement.render_html(root_element)
    assert string == "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n</head>\n<body><div " \
                     "class=\'testing\'>\n\t<h1>\n\t\tHello World\n\t</h1>\n\t<p>\n\t\ttest\n\t</p>\n\t<h2 " \
                     "class=\'testing\'>\n\t\tHello World\n\t\t<h2>\n\t\t\tHello " \
                     "World\n\t\t</h2>\n\t</h2>\n</div>\n</body>\n</html>"


def test_find_by_tag() -> None:
    array = HtmlElement.find_by_tag(root_element, "h2")
    assert len(array) == 2


def test_find_by_attribute() -> None:
    array = HtmlElement.find_by_attribute(root_element, "class", "testing")
    assert len(array) == 2
