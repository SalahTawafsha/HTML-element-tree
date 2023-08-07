""" class that represent nano HTML framework"""
from typing import Union


class HtmlElement:
    """ this class has name, attributes and children"""

    html_tags: set = {
        "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi",
        "bdo", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code",
        "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog",
        "div", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer",
        "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hr", "html", "i",
        "iframe", "img", "input", "ins", "kbd", "label", "legend", "li", "link", "main",
        "map", "mark", "meta", "meter", "nav", "noscript", "object", "ol", "optgroup",
        "option", "output", "p", "param", "picture", "pre", "progress", "q", "rb", "rp",
        "rt", "rtc", "ruby", "s", "samp", "script", "section", "select", "slot", "small",
        "source", "span", "strong", "style", "sub", "summary", "sup", "table", "tbody",
        "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr",
        "track", "u", "ul", "var", "video", "wbr"
    }
    usedIDs: set = set()

    def __init__(self, name: str, value: Union[str, 'HtmlElement', list['HtmlElement']],
                 attributes: dict = None) -> None:
        if attributes is None:
            attributes = {}
        if name not in HtmlElement.html_tags:
            raise ValueError("Invalid HTML tag")
        if "id" in attributes:
            if attributes["id"] in HtmlElement.usedIDs:
                raise ValueError("ID already used")
            HtmlElement.usedIDs.add(attributes["id"])

        self.name = name
        self.attributes = attributes
        self.children = []
        if isinstance(value, list):
            for val in value:
                self.children.append(val)
        else:
            self.children.append(value)

    def __str__(self) -> str:
        string: str = f"<{self.name}"
        for name, value in self.attributes.items():
            string += f" {name}='{value}'"
        return string + '>'

    @classmethod
    def append(cls, element: 'HtmlElement', new_element: 'HtmlElement') -> None:
        """ add new Element to element as a child """
        if "id" in new_element.attributes:
            if new_element.attributes["id"] in HtmlElement.usedIDs:
                raise ValueError("ID already used")
            HtmlElement.usedIDs.add(new_element.attributes["id"])

        element.children.append(new_element)

    @classmethod
    def render(cls, element: 'HtmlElement', level: int = 0) -> str:
        """ print element tree as HTML string """
        output = "\t" * level
        level += 1

        if hasattr(element, "children"):
            output += f"{element}\n"
            for child in element.children:
                output += HtmlElement.render(child, level)
            output += "\t" * (level - 1)
            output += f"</{element.name}>\n"
        else:
            output += f"{element}\n"

        return output

    @classmethod
    def render_html(cls, element: 'HtmlElement') -> str:
        """ generate full HTML file that ready to run """
        html_code: str = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>'''
        html_code += "\n<body>"
        html_code += HtmlElement.render(element)
        html_code += "</body>\n</html>"
        return html_code

    @classmethod
    def find_by_tag(cls, element: 'HtmlElement', tag_name: str, result: list = None) -> list:
        """ get all element by tagName """
        if result is None:
            result = []

        if hasattr(element, "name") and element.name == tag_name:
            result.append(element)

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

        if hasattr(element, "attributes") and element.attributes.get(attribute) == value:
            result.append(element)

        if hasattr(element, "children"):
            for child in element.children:
                HtmlElement.find_by_attribute(child, attribute, value, result)

        return result
