import pytest
from HTML.solution.html_element import HtmlElement
from HTML.solution.subset import form


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
    element = HtmlElement("div", form)
    HtmlElement.append(element, HtmlElement("br", ""))
    assert len(element.children) == 2


def test_append() -> None:
    root = HtmlElement("h1", "Hello World", {"class": "testing"})
    child = HtmlElement("h1", "Hello World", {"class": "testing"})
    HtmlElement.append(root, child)
    assert len(root.children) == 2


def test_append_existed_id() -> None:
    with pytest.raises(ValueError):
        root = HtmlElement("h1", "Hello World", {"id": "title"})
        child = HtmlElement("h1", "Hello World", {"id": "title"})
        HtmlElement.append(root, child)


def test_render() -> None:
    string: str = HtmlElement.render(form)
    assert string == "<form method='post' action='login.php'>\n\t<h3>\n\t\tLog " \
                     "in\n\t</h3>\n\t<hr>\n\t\t\n\t<table>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<label for='email' " \
                     "class='my-label'>\n\t\t\t\t\tEmail: \n\t\t\t\t</label>\n\t\t\t</td>" \
                     "\n\t\t\t<td>\n\t\t\t\t<input " \
                     "type='text' name='email' " \
                     "id='email'>\n\t\t\t\t\t\n\t\t\t</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<label " \
                     "for='password' class='my-label'>\n\t\t\t\t\tPassword: " \
                     "\n\t\t\t\t</label>\n\t\t\t</td>\n\t\t\t<td>\n\t\t\t\t<input type='password' name='password' " \
                     "id='password'>\n\t\t\t\t\t\n\t\t\t</td>\n\t\t</tr>\n\t</table>\n\t<br>\n\t\t\n\t<input " \
                     "type='submit' value='Log in'>\n\t\t\n</form>\n"


def test_render_html() -> None:
    string: str = HtmlElement.render_html(form)
    assert string == "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    " \
                     "<meta charset=\"UTF-8\">\n</head>\n<body><form " \
                     "method=\'post\' action=\'login.php\'>\n\t<h3>\n\t\tLog " \
                     "in\n\t</h3>\n\t<hr>\n\t\t\n\t<table>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<label for=\'email\' " \
                     "class=\'my-label\'>\n\t\t\t\t\tEmail: " \
                     "\n\t\t\t\t</label>\n\t\t\t</td>\n\t\t\t<td>\n\t\t\t\t<input type=\'text\' name=\'email\' " \
                     "id=\'email\'>\n\t\t\t\t\t\n\t\t\t</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<label " \
                     "for=\'password\' class=\'my-label\'>\n\t\t\t\t\tPassword: " \
                     "\n\t\t\t\t</label>\n\t\t\t</td>\n\t\t\t<td>\n\t\t\t\t" \
                     "<input type=\'password\' name=\'password\' " \
                     "id=\'password\'>\n\t\t\t\t\t\n\t\t\t</td>\n\t\t</tr>\n\t</table>\n\t<br>\n\t\t\n\t<input " \
                     "type=\'submit\' value=\'Log in\'>\n\t\t\n</form>\n</body>\n</html>"


def test_find_by_tag() -> None:
    array = HtmlElement.find_by_tag(form, "input")
    assert len(array) == 3


def test_find_by_attribute() -> None:
    array = HtmlElement.find_by_attribute(form, "class", "my-label")
    assert len(array) == 2
