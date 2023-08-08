""" class that represent nano HTML framework"""
from typing import Union


class HtmlElement:
    """ this class has name, attributes and children"""

    # tags into two sets based on whether they require a closing tag or not
    tag_with_close: set = {
        "a", "abbr", "address", "article", "aside", "audio", "b", "bdi", "bdo",
        "blockquote", "button", "canvas", "caption", "cite", "code", "data",
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

    # static set to store all used IDs
    usedIDs: set = set()

    def __init__(self, name: str, value: Union[str, 'HtmlElement', list['HtmlElement']],
                 attributes: dict = None) -> None:
        if attributes is None:
            attributes = {}

        # check if element name is true HTML tag
        if name not in HtmlElement.tag_with_close and name not in HtmlElement.tag_without_close:
            raise ValueError("Invalid HTML tag")

        # check if there are ID in attributes and if it is unique
        if "id" in attributes:
            if attributes["id"] in HtmlElement.usedIDs:
                raise ValueError("ID already used")
            HtmlElement.usedIDs.add(attributes["id"])

        self.name = name
        self.attributes = attributes
        self.children = []

        # check if value is list to store it as children one by one
        if isinstance(value, list):
            for val in value:
                self.children.append(val)
        else:
            self.children.append(value)

    def __str__(self) -> str:
        # generate open tag string with all attributes
        string: str = f"<{self.name}"
        for name, value in self.attributes.items():
            string += f" {name}='{value}'"
        return string + '>'

    @classmethod
    def append(cls, element: 'HtmlElement',
               new_element: Union['HtmlElement', list['HtmlElement']]) -> None:
        """ add new element to element as a child """

        # check if there are ID in attributes and if it is unique
        if isinstance(new_element, list):
            for child in new_element:
                if "id" in child.attributes:
                    if child.attributes["id"] in HtmlElement.usedIDs:
                        raise ValueError("ID already used")
                    HtmlElement.usedIDs.add(child.attributes["id"])
                element.children.append(child)
        else:
            if "id" in new_element.attributes:
                if new_element.attributes["id"] in HtmlElement.usedIDs:
                    raise ValueError("ID already used")
                HtmlElement.usedIDs.add(new_element.attributes["id"])
            element.children.append(new_element)

    @classmethod
    def render(cls, element: 'HtmlElement', level: int = 0) -> str:
        """ print element tree as HTML string """

        # print tabs based on level of tree
        output = "\t" * level

        # increment level to use when call children
        level += 1

        # print open tag or string that are child
        output += f"{element}\n"

        if hasattr(element, "children"):
            for child in element.children:
                output += HtmlElement.render(child, level)

            # check if element need close tag and add it
            if element.name in HtmlElement.tag_with_close:
                output += "\t" * (level - 1)
                output += f"</{element.name}>\n"

        return output

    @classmethod
    def render_html(cls, element: 'HtmlElement') -> str:
        """ generate full HTML file that ready to run """

        # print doctype that is HTML and head of file
        html_code: str = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>'''

        # open the body tag to print element
        html_code += "\n<body>"

        # print element
        html_code += HtmlElement.render(element)

        # close body tag
        html_code += "</body>\n</html>"
        return html_code

    @classmethod
    def find_by_tag(cls, element: 'HtmlElement', tag_name: str, result: list = None) -> list:
        """ get all elements by tagName """
        if result is None:
            result = []

        # check if the element is HTML element (not str)
        # and compare if it's the target
        if hasattr(element, "name") and element.name == tag_name:
            result.append(element)

        # check if element has children and find in each
        if hasattr(element, "children"):
            for child in element.children:
                HtmlElement.find_by_tag(child, tag_name, result)

        return result

    @classmethod
    def find_by_attribute(cls, element: 'HtmlElement',
                          attribute: str, value: str, result: list = None) -> list:
        """ get all elements that has an attribute value """
        if result is None:
            result = []

        # check if element has attributes and if it's the target
        if hasattr(element, "attributes") and element.attributes.get(attribute) == value:
            result.append(element)

        # check if element has children and find in each
        if hasattr(element, "children"):
            for child in element.children:
                HtmlElement.find_by_attribute(child, attribute, value, result)

        return result
