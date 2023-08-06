class HTMLElement:
    html_tags = [
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
    ]
    usedIDs = set()

    def __init__(self, name, value, attributes=None):
        if attributes is None:
            attributes = {}
        if name not in HTMLElement.html_tags:
            raise ValueError("Invalid HTML tag")
        if "id" in attributes:
            if attributes["id"] in HTMLElement.usedIDs:
                raise ValueError("ID already used")
            HTMLElement.usedIDs.add(attributes["id"])

        self.name = name
        self.value = value
        self.attributes = attributes


att = HTMLElement("h1", "Hello World", {"id": "test", "class": "testing"})

print(att.name)
print(att.value)
print(att.attributes)
