from typing import Union


class HTMLElement:
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
        "track", "u", "ul", "var", "video", "wbr",
    }
    usedIDs: set = set()

    def __init__(self, name: str, value: Union[str, 'HTMLElement', list['HTMLElement']],
                 attributes: dict = None) -> None:
        if attributes is None:
            attributes = dict()
        if name not in HTMLElement.html_tags:
            raise ValueError("Invalid HTML tag")
        if "id" in attributes:
            if attributes["id"] in HTMLElement.usedIDs:
                raise ValueError("ID already used")
            HTMLElement.usedIDs.add(attributes["id"])

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
    def append(cls, element: 'HTMLElement', new_element: 'HTMLElement') -> None:
        element.children.append(new_element)

    @classmethod
    def render(cls, element: 'HTMLElement', level: int = 0) -> str:
        if not element:
            return ""

        output = "\t" * level
        level += 1

        if hasattr(element, "children"):
            output += f"{element}\n"
            for child in element.children:
                output += HTMLElement.render(child, level)
            output += "\t" * (level - 1)
            output += f"</{element.name}>\n"
        else:
            output += f"{element}\n"

        return output

    @classmethod
    def render_html(cls, element: 'HTMLElement') -> str:
        html_code: str = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>'''
        html_code += "\n<body>"
        html_code += HTMLElement.render(element)
        html_code += "</body>\n</html>"
        return html_code

    @classmethod
    def find_by_tag(cls, element: 'HTMLElement', tag_name: str, result: list = None) -> list:
        if result is None:
            result = []

        if hasattr(element, "name") and element.name.__eq__(tag_name):
            result.append(element)

        if hasattr(element, "children"):
            for child in element.children:
                HTMLElement.find_by_tag(child, tag_name, result)

        return result

    @classmethod
    def find_by_attribute(cls, element: 'HTMLElement', attribute: str, value: str, result: list = None) -> list:
        if result is None:
            result = []

        if hasattr(element, "attributes") and element.attributes.get(attribute) == value:
            result.append(element)

        if hasattr(element, "children"):
            for child in element.children:
                HTMLElement.find_by_attribute(child, attribute, value, result)

        return result
