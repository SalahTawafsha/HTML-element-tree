""" class that represent nano HTML framework"""
from __future__ import annotations
from typing import Union, Self


class InvalidTagError(Exception):
    """ custom exception for invalid tag """

    def __init__(self, tag_name: str = None):
        if not isinstance(tag_name, str):
            self.message = "HTML tag is not a string"
        else:
            self.message = f"HTML tag <{tag_name}> is NOT defined"
        super().__init__(self.message)


class DuplicatedIDError(Exception):
    """ custom exception for invalid id """

    def __init__(self, tag_name: str = None):
        if not isinstance(tag_name, str):
            self.message = "This ID is already used in the HTML tree"
        else:
            self.message = f"ID {tag_name} is already used in the HTML tree"
        super().__init__(self.message)


ALLOWED_VALUE_TYPE = Union[str, Self, list[Union[str, Self]], set[Union[str, Self]], tuple[
    Union[str, Self]]]


class HtmlElement:
    """ this class has name, attributes and children fields"""

    # tags into two sets based on whether they require a closing tag or not
    tag_with_close: set = {
        "a", "abbr", "address", "article", "aside", "audio", "b", "bdi", "bdo",
        "blockquote", "body", "button", "canvas", "caption", "cite", "code", "data",
        "datalist", "dd", "del", "details", "dfn", "dialog", "div", "dl", "dt",
        "em", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2",
        "h3", "h4", "h5", "h6", "header", "i", "iframe", "ins", "kbd", "label",
        "legend", "li", "main", "mark", "menu", "nav", "object", "ol", "optgroup",
        "option", "output", "p", "pre", "progress", "q", "ruby", "s", "samp",
        "section", "select", "small", "span", "strong", "sub", "summary", "sup",
        "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead",
        "time", "title", "tr", "ul", "var", "video"
    }

    tag_without_close: set = {
        "area", "base", "br", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"
    }

    def __init__(self, name: str, value: ALLOWED_VALUE_TYPE = None,
                 attributes: dict = None) -> None:
        if attributes is None:
            attributes = {}

        if not HtmlElement.__validate_input(value):
            raise ValueError(
                f"{type(value)} is not allowed for value, the allowed is {ALLOWED_VALUE_TYPE}")

        if not isinstance(attributes, dict):
            raise ValueError("attributes must be a dict")

        if not isinstance(name, str):
            raise ValueError("name must be a string")

        # check if element name is true HTML tag
        if name.lower() not in HtmlElement.tag_with_close and name.lower() not in HtmlElement.tag_without_close:
            raise InvalidTagError(name)

        self.usedIDs: set = set()
        self.name = name
        self.attributes = attributes
        self.children = []
        self.parent = None

        if "id" in attributes:
            self.usedIDs.add(attributes["id"])

        HtmlElement.append(self, value)

    def __str__(self) -> str:
        # generate open tag string with all attributes
        return HtmlElement.render(self)

    def __append_element(self, new_element: ALLOWED_VALUE_TYPE):
        if not HtmlElement.__validate_input(new_element):
            raise ValueError(
                f"{type(new_element)} is not allowed for value, the allowed is {ALLOWED_VALUE_TYPE}")

        if isinstance(new_element, HtmlElement):
            if new_element.usedIDs.intersection(self.usedIDs):
                raise DuplicatedIDError(str(new_element.usedIDs.intersection(self.usedIDs)))
            self.usedIDs.update(new_element.usedIDs)
            new_element.parent = self

        self.children.append(new_element)
        if isinstance(self.parent, HtmlElement):
            HtmlElement.__append_new_ids_with_parents(self.parent, new_element.usedIDs)

    @classmethod
    def append(cls, element: HtmlElement,
               new_element: ALLOWED_VALUE_TYPE) -> None:
        """ add new element to element as a child """

        if not isinstance(element, HtmlElement):
            raise ValueError("element must be an instance of HtmlElement")

        if not HtmlElement.__validate_input(new_element):
            raise ValueError(
                f"{type(new_element)} is not allowed for value, the allowed is {ALLOWED_VALUE_TYPE}")

        # check if there are ID in attributes and if it is unique
        if isinstance(new_element, (list, tuple, set)):
            for child in new_element:
                if child != "":
                    element.__append_element(child)

        else:
            if new_element != "":
                element.__append_element(new_element)

    @classmethod
    def render(cls, element: Union[HtmlElement, str], level: int = 0) -> str:
        """ print element tree as HTML string """

        if not isinstance(element, (str, HtmlElement)):
            raise ValueError("element must be an instance of HtmlElement")

        # print tabs based on level of tree
        output = "\t" * level

        # increment level to use when call children
        level += 1

        # print open tag or string that are child
        if isinstance(element, HtmlElement) and not element.children and element.name in cls.tag_with_close:
            output += f"{element.__get_open_tag()}</{element.name}>\n"
            return output
        elif isinstance(element, HtmlElement):
            output += f"{element.__get_open_tag()}\n"
        else:
            output += f"{element}\n"

        if isinstance(element, HtmlElement):
            for child in element.children:
                output += cls.render(child, level)

            # check if element need close tag and add it
            if element.name in cls.tag_with_close:
                output += "\t" * (level - 1)
                output += f"</{element.name}>\n"

        return output

    @classmethod
    def render_html_file(cls, element: HtmlElement) -> str:
        """ generate full HTML file that ready to run """

        if not isinstance(element, (str, HtmlElement)):
            raise ValueError("element must be an instance of HtmlElement")

        # print doctype that is HTML and head of file
        html_code: str = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>'''

        # open the body tag to print element
        html_code += "\n<body>\n"

        # print element
        html_code += cls.render(element, 1)

        # close body tag
        html_code += "</body>\n</html>"
        return html_code

    @classmethod
    def find_elements_by_tag(cls, element: Union[HtmlElement, str], tag_name: str) -> list:
        """ get all elements by tagName """

        if not isinstance(element, (HtmlElement, str)):
            raise ValueError(f"{type(element)} must be an instance of HtmlElement")

        if not isinstance(tag_name, str):
            raise ValueError("tag_name must be a string")

        result = cls.find_elements(element, tag_name=tag_name)

        return result

    @classmethod
    def find_elements_by_attribute(cls, element: Union[HtmlElement, str],
                                   attribute: str, value: str) -> list:
        """ get all elements that has an attribute value """

        if not isinstance(element, (HtmlElement, str)):
            raise ValueError(f"{type(element)} must be an instance of HtmlElement")

        if not isinstance(attribute, str):
            raise ValueError("attribute must be a string")

        if not isinstance(value, str):
            raise ValueError("value must be a string")

        result = cls.find_elements(element, attribute=attribute, value=value)

        return result

    @classmethod
    def find_elements(cls, element: Union[HtmlElement, str], tag_name: str = None,
                      attribute: str = None, value: str = None, result: list = None) -> list:

        if result is None:
            result = []

        # check if element has attributes and if it's the target
        if attribute is not None and value is not None:
            if hasattr(element, "attributes") and element.attributes.get(attribute) == value:
                result.append(element)
        elif tag_name is not None:
            if hasattr(element, "name") and element.name == tag_name:
                result.append(element)
        else:
            raise ValueError("tag_name or attribute must be filled")

        # check if element has children and find in each
        if hasattr(element, "children"):
            for child in element.children:
                cls.find_elements(child, tag_name, attribute, value, result)

        return result

    @staticmethod
    def __validate_input(value):
        if isinstance(value, (str, HtmlElement, set, list, tuple)):
            if isinstance(value, (list, set, tuple)):
                for item in value:
                    if not isinstance(item, (str, HtmlElement)):
                        return False
            return True
        return False

    @staticmethod
    def __append_new_ids_with_parents(new_element: ALLOWED_VALUE_TYPE, new_ids):
        if isinstance(new_element, HtmlElement):
            if new_element.usedIDs.intersection(new_ids):
                raise DuplicatedIDError(str(new_element.usedIDs.intersection(new_ids)))
            new_element.usedIDs.update(new_ids)
            if isinstance(new_element.parent, HtmlElement):
                HtmlElement.__append_new_ids_with_parents(new_element.parent, new_ids)

    def __get_open_tag(self) -> str:
        # generate open tag string with all attributes
        string: str = f"<{self.name}"
        for name, value in self.attributes.items():
            string += f" {name}='{value}'"
        return string + '>'
