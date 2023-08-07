class HTMLElement:
    html_tags = {
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
    usedIDs = set()

    def __init__(self, name, value, attributes=None) -> None:
        if attributes is None:
            attributes = {}
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
        return self.name

    @classmethod
    def append(cls, element, new_element) -> None:
        element.children.append(new_element)

    @classmethod
    def render(cls, element, level=0):
        if not element:
            return

        print("\t" * level, end="")
        level += 1

        if hasattr(element, "children"):
            print(f"<{element}>")
            for child in element.children:
                HTMLElement.render(child, level)
            print("\t" * (level - 1), end="")
            print(f"</{element}>")
        else:
            print(element)

    @classmethod
    def render_html(cls, element):
        html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>'''
        print(html_code)
        print("<body>")
        HTMLElement.render(element)
        print("</body>\n</html>")

    @classmethod
    def find_by_tag(cls, element, tag_name, result=None) -> list:
        if result is None:
            result = []

        if not element:
            return result

        if hasattr(element, "name") and element.name == tag_name:
            result.append(element)

        if hasattr(element, "children"):
            for child in element.children:
                HTMLElement.find_by_tag(child, tag_name, result)
