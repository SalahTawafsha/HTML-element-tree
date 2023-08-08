""" unit test for HtmlElement class """
import pytest
from HTML.solution.html_element import HtmlElement
from HTML.solution.subset import form


def test_duplicate_id() -> None:
    """ test if duplicate id is detected """
    with pytest.raises(ValueError):
        element1 = HtmlElement("h1", "Hello World", {"id": "test"})
        element2 = HtmlElement("h2", "Error", {"id": "test"})
        # that just to ignore warning on unused variable element1 and element2
        bool_1 = not element1
        bool_2 = not element2
        assert bool_1 and bool_2


def test_invalid_tag() -> None:
    """ test if invalid tag is detected """
    with pytest.raises(ValueError):
        element1 = HtmlElement("hello", "Hello World", {"id": "test"})
        # that just to ignore warning on unused variable element1
        bool_1 = not element1
        assert bool_1


def test_valid_tag() -> None:
    """ test if valid tag is accepted """
    element1 = HtmlElement("h1", "Hello World", {"id": "testing"})
    assert element1.name == "h1"
    assert element1.children[0] == "Hello World"
    assert element1.attributes == {"id": "testing"}


def test_no_attributes() -> None:
    """ test if no attributes is accepted """
    element1 = HtmlElement("h1", "Hello World")
    assert element1.name == "h1"
    assert element1.children[0] == "Hello World"
    assert element1.attributes == {}


def test_html_element_value() -> None:
    """ test if HtmlElement value can be a value of another HtmlElement """
    element = HtmlElement("div", HtmlElement("h1", "hello"))
    assert len(element.children) == 1


def test_html_element_list() -> None:
    """ test if HtmlElement value can be a list of another HtmlElement """
    element = HtmlElement("div", form)
    HtmlElement.append(element, HtmlElement("br", ""))
    assert len(element.children) == 2


def test_append() -> None:
    """ test if append method works """
    root = HtmlElement("h1", "Hello World", {"class": "testing"})
    child = HtmlElement("h1", "Hello World", {"class": "testing"})
    HtmlElement.append(root, child)
    assert len(root.children) == 2


def test_append_existed_id() -> None:
    """ test if append method rise error when have duplicate ID """
    with pytest.raises(ValueError):
        root = HtmlElement("h1", "Hello World", {"id": "title"})
        child = HtmlElement("h1", "Hello World", {"id": "title"})
        HtmlElement.append(root, child)


def test_render() -> None:
    """ test if render method works """
    string: str = HtmlElement.render(form)
    assert string == "<form method='post' action='login.php'>\n\t<h3>\n\t\tLog " \
                     "in\n\t</h3>\n\t<hr>\n\t\t\n\t<table>\n\t\t<tr>\n\t\t\t" \
                     "<td>\n\t\t\t\t<label for='email' " \
                     "class='my-label'>\n\t\t\t\t\tEmail: \n\t\t\t\t</label>\n\t\t\t</td>" \
                     "\n\t\t\t<td>\n\t\t\t\t<input " \
                     "type='text' name='email' " \
                     "id='email'>\n\t\t\t\t\t\n\t\t\t</td>\n\t\t</tr>" \
                     "\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<label " \
                     "for='password' class='my-label'>\n\t\t\t\t\tPassword: " \
                     "\n\t\t\t\t</label>\n\t\t\t</td>\n\t\t\t" \
                     "<td>\n\t\t\t\t<input type='password' name='password' " \
                     "id='password'>\n\t\t\t\t\t\n\t\t\t</td>" \
                     "\n\t\t</tr>\n\t</table>\n\t<br>\n\t\t\n\t<input " \
                     "type='submit' value='Log in'>\n\t\t\n</form>\n"


def test_render_html() -> None:
    """ test if render_html method works """
    string: str = HtmlElement.render_html(form)
    assert string == "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    " \
                     "<meta charset=\"UTF-8\">\n</head>\n<body><form " \
                     "method=\'post\' action=\'login.php\'>\n\t<h3>\n\t\tLog " \
                     "in\n\t</h3>\n\t<hr>\n\t\t\n\t<table>\n\t\t" \
                     "<tr>\n\t\t\t<td>\n\t\t\t\t<label for=\'email\' " \
                     "class=\'my-label\'>\n\t\t\t\t\tEmail: " \
                     "\n\t\t\t\t</label>\n\t\t\t</td>\n\t\t\t<td>" \
                     "\n\t\t\t\t<input type=\'text\' name=\'email\' " \
                     "id=\'email\'>\n\t\t\t\t\t\n\t\t\t</td>\n\t\t" \
                     "</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<label " \
                     "for=\'password\' class=\'my-label\'>\n\t\t\t\t\tPassword: " \
                     "\n\t\t\t\t</label>\n\t\t\t</td>\n\t\t\t<td>\n\t\t\t\t" \
                     "<input type=\'password\' name=\'password\' " \
                     "id=\'password\'>\n\t\t\t\t\t\n\t\t\t</td>\n\t\t" \
                     "</tr>\n\t</table>\n\t<br>\n\t\t\n\t<input " \
                     "type=\'submit\' value=\'Log in\'>\n\t\t\n</form>\n</body>\n</html>"


def test_find_by_tag() -> None:
    """ test that find_by_tag method works """
    array = HtmlElement.find_by_tag(form, "input")
    assert len(array) == 3


def test_find_by_attribute() -> None:
    """ test that find_by_attribute method works """
    array = HtmlElement.find_by_attribute(form, "class", "my-label")
    assert len(array) == 2
