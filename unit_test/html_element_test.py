""" unit test for HtmlElement class """
import pytest
from HTML.solution.html_element import DuplicatedIDError, InvalidTagError
from functools import partial
from .html_element_examples import *


@pytest.fixture
def form_render():
    return "<form method='post' action='login.php'>\n\t<h3>\n\t\tLog in\n\t" \
           "</h3>\n\t<hr>\n\t<table>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t" \
           "<label for='email' class='my-label'>\n\t\t\t\t\tEmail: \n\t\t\t\t" \
           "</label>\n\t\t\t</td>\n\t\t\t<td>\n\t\t\t\t<input type='text' name='email' id='email'>" \
           "\n\t\t\t</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<label for='password' class='my-label'>" \
           "\n\t\t\t\t\tPassword: \n\t\t\t\t</label>\n\t\t\t</td>\n\t\t\t<td>\n\t\t\t\t" \
           "<input type='password' name='password' id='password'>\n\t\t\t</td>\n\t\t</tr>\n\t</table>\n\t" \
           "<br>\n\t<input type='submit' value='Log in'>\n</form>\n"


@pytest.fixture
def form_render_html(form_render):
    return "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    " \
           "<meta charset=\"UTF-8\">\n</head>\n<body>\n\t" \
           "<form method='post' action='login.php'>\n\t\t<h3>\n\t\t\tLog in\n\t\t" \
           "</h3>\n\t\t<hr>\n\t\t<table>\n\t\t\t<tr>\n\t\t\t\t<td>\n\t\t\t\t\t" \
           "<label for='email' class='my-label'>\n\t\t\t\t\t\tEmail: \n\t\t\t\t\t" \
           "</label>\n\t\t\t\t</td>\n\t\t\t\t<td>\n\t\t\t\t\t<input type='text' name='email' id='email'>" \
           "\n\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr>\n\t\t\t\t<td>\n\t\t\t\t\t<label for='password' class='my-label'>" \
           "\n\t\t\t\t\t\tPassword: \n\t\t\t\t\t</label>\n\t\t\t\t</td>\n\t\t\t\t<td>\n\t\t\t\t\t" \
           "<input type='password' name='password' id='password'>\n\t\t\t\t</td>\n\t\t\t</tr>\n\t\t</table>\n\t\t" \
           "<br>\n\t\t<input type='submit' value='Log in'>\n\t</form>\n" \
           "</body>\n</html>"


@pytest.fixture
def html_tree() -> HtmlElement:
    hr = HtmlElement("hr", "")

    email_label = HtmlElement("label", "Email: ", {"for": "email", "class": "my-label"})
    email_input = HtmlElement("input", "", {"type": "text", "name": "email", "id": "email"})

    password_label = HtmlElement("label", "Password: ", {"for": "password", "class": "my-label"})
    password_input = \
        HtmlElement("input", "", {"type": "password", "name": "password", "id": "password"})

    table = \
        HtmlElement("table",
                    [HtmlElement("tr", [HtmlElement("td", email_label),
                                        HtmlElement("td", email_input)]),
                     HtmlElement("tr", [HtmlElement("td", password_label),
                                        HtmlElement("td", password_input)])])

    br = HtmlElement("br", "")

    submit = HtmlElement("input", "", {"type": "submit", "value": "Log in"})

    form = partial(HtmlElement, name="form")

    return form(value=[HtmlElement("h3", "Log in"), hr, table, br, submit],
                attributes={"method": "post", "action": "login.php"})


@pytest.fixture
def last_child_of_complex_tree():
    body = HtmlElement("body", "", {"id": "body"})

    header = HtmlElement("header", "", {"id": "header"})

    main = HtmlElement("main", "", {"id": "main"})

    footer = HtmlElement("footer", "", {"id": "footer"})

    HtmlElement.append(body, [header, main, footer])

    # header elements
    header_ul = HtmlElement("ul", "", {"id": "header-ul"})

    HtmlElement.append(header, header_ul)

    header_ul_li1 = HtmlElement("li", "", {"id": "header-ul-li1"})
    header_ul_li2 = HtmlElement("li", "", {"id": "header-ul-li2"})

    HtmlElement.append(header_ul, [header_ul_li1, header_ul_li2])

    a = HtmlElement("a", "test", {"href": ".", "id": "a-id"})
    HtmlElement.append(header_ul_li1, a)

    img = HtmlElement("img", "", {"src": "https://upload.wikimedia.org/"
                                         "wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png",
                                  "alt": "random image", "width": "100px"})
    HtmlElement.append(header_ul_li2, img)

    # main elements
    main_table = HtmlElement("table", "", {"id": "main-table"})

    HtmlElement.append(main, main_table)

    main_table_thead = HtmlElement("thead", "", {"id": "thead"})
    main_table_tbody = HtmlElement("tbody", "", {"id": "tbody"})

    HtmlElement.append(main_table, [main_table_thead, main_table_tbody])

    # main_table header
    main_table_thead_tr = HtmlElement("tr", "", {"id": "thead-tr"})
    main_table_thead_tr_th1 = HtmlElement("th", "Name", {"id": "thead-tr-th1"})
    main_table_thead_tr_th2 = HtmlElement("th", "Age", {"id": "thead-tr-th2"})

    HtmlElement.append(main_table_thead_tr, [main_table_thead_tr_th1, main_table_thead_tr_th2])

    HtmlElement.append(main_table_thead, main_table_thead_tr)

    # main_table body
    main_table_tbody_tr1 = HtmlElement("tr", "", {"id": "tbody-tr"})
    main_table_tbody_tr1_td1 = HtmlElement("td", "John", {"id": "tbody-tr1-td1"})
    main_table_tbody_tr1_td2 = HtmlElement("td", "25", {"id": "tbody-tr1-td2"})

    HtmlElement.append(main_table_tbody_tr1, [main_table_tbody_tr1_td1, main_table_tbody_tr1_td2])

    HtmlElement.append(main_table_tbody, main_table_tbody_tr1)

    # exception is here since the id a-id is used in a that in header (not directly in header)

    form = HtmlElement("form", "", {"id": "form-id"})

    HtmlElement.append(form, main_table)
    HtmlElement.append(form, HtmlElement("input", "", {"type": "text", "id": "main"}))

    return footer


NUM_ZERO: int = 0
NUM_ONE: int = 1
NUM_TWO: int = 2
NUM_THREE: int = 3
NUM_FIVE: int = 5


def test_duplicate_id() -> None:
    """ test if duplicate id is detected """
    with pytest.raises(DuplicatedIDError):
        h2 = HtmlElement("h2", h1, {"id": "test"})
        assert h2


def test_not_duplicate_id() -> None:
    """ test if duplicate id is detected """
    h2 = HtmlElement("h2", h1, {"id": "accepted"})
    assert h2


def test_reuse_element_in_different_tree() -> None:
    """ test if reuse element in different tree is allowed """
    div = HtmlElement("div", [h1, p], {"id": "id1"})

    HtmlElement.append(p, section)
    HtmlElement.append(p, HtmlElement("div", "", {"id": "x"}))

    table = HtmlElement("table", "", {"id": "id1"})
    assert HtmlElement.render(div) == "<div id='id1'>\n\t<h1 id='test'></h1>\n\t<p id='hi'>\n\t\t<section " \
                                      "id='section'></section>\n\t\t<div id='x'></div>\n\t</p>\n</div>\n"
    assert HtmlElement.render(table) == "<table id='id1'></table>\n"


def test_invalid_tag() -> None:
    """ test if invalid tag is detected """
    with pytest.raises(InvalidTagError):
        invalid = HtmlElement("hello", "Hello World", {"id": "test"})
        assert invalid


def test_valid_tag() -> None:
    """ test if valid tag is accepted """
    element = HtmlElement("h1", "Hello World", {"id": "testing"})
    assert element.name == "h1"


def test_no_attributes() -> None:
    """ test if no attributes is accepted """
    element = HtmlElement("h1", "Hello World")
    assert element.attributes == {}


def test_has_attributes() -> None:
    """ test if no attributes is accepted """
    element = HtmlElement("input", "", {"type": "password", "name": "password", "id": "password"})
    assert element.attributes == {"type": "password", "name": "password", "id": "password"}


def test__html_element_with_list() -> None:
    """ test if HtmlElement value can be a value of another HtmlElement """
    element = HtmlElement("div", HtmlElement("h1", "hello"))
    assert len(element.children) == NUM_ONE


def test_html_element_list(html_tree) -> None:
    """ test if HtmlElement value can be a list of another HtmlElement """
    assert len(html_tree.children) == NUM_FIVE


def test_complex_html_tree(last_child_of_complex_tree) -> None:
    """ test if HtmlElement value can be a list of another HtmlElement """
    with pytest.raises(DuplicatedIDError):
        footer_p = HtmlElement("p", "", {"id": "a-id"})

        HtmlElement.append(last_child_of_complex_tree, footer_p)


def test_append() -> None:
    """ test if append method works """
    root = HtmlElement("h1", "Hello World", {"class": "testing"})
    HtmlElement.append(root, h1)
    assert len(root.children) == NUM_TWO


def test_append_existed_id() -> None:
    """ test if append method rise error when have duplicate ID """
    with pytest.raises(DuplicatedIDError):
        root = HtmlElement("h1", "Hello World", {"id": "test"})
        HtmlElement.append(root, h1)


def test_render(html_tree, form_render) -> None:
    """ test if render method works """
    string: str = HtmlElement.render(html_tree)
    assert string == form_render


def test_render_for_empty_elements():
    empty_h1 = HtmlElement("h1", "")
    empty_p = HtmlElement("p", "")

    div = HtmlElement("div", [empty_h1, empty_p])

    string: str = HtmlElement.render(div)
    assert string == "<div>\n\t<h1></h1>\n\t<p></p>\n</div>\n"


def test_render_html(html_tree, form_render_html) -> None:
    """ test if render_html method works """
    string: str = HtmlElement.render_html(html_tree)
    assert string == form_render_html


def test_find_by_tag(html_tree) -> None:
    """ test that find_by_tag method works """
    array = HtmlElement.find_elements_by_tag(html_tree, "input")
    assert len(array) == NUM_THREE


def test_empty_in_find_by_tag(html_tree) -> None:
    """ test that find_by_tag method works """
    array = HtmlElement.find_elements_by_tag(html_tree, "h1")
    assert len(array) == NUM_ZERO


def test_find_by_attribute(html_tree) -> None:
    """ test that find_by_attribute method works """
    array = HtmlElement.find_elements_by_attribute(html_tree, "class", "my-label")
    assert len(array) == NUM_TWO


def test_empty_in_find_by_attribute(html_tree) -> None:
    """ test that find_by_attribute method works """
    array = HtmlElement.find_elements_by_attribute(html_tree, "action", "test.php")
    assert len(array) == NUM_ZERO
