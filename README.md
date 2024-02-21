# HTML element tree builder

This is a html element tree builder. It is a class that can be used to build a tree of html elements.

the class is implemented by N-Ary tree data structure, with update to let child has a reference to its parent. and this
will use to has unique id for each element.

## Features

- Create a new HTML element.
- Append some element to a parent.
- Find elements by attributes.
- Find elements by tag name.
- Render element as HTML format
- Render full HTML file.

## Installation

```bash
git clone https://github.com/SalahTawafsha/HTML-element-tree.git
py -m pip install -r .\documents\requirements.txt
```

## Testing

```bash
python -m pytest .\unit_test\html_element_test.py -v
```

## Usage

we will be able to write python code to generate HTML elements or full file by using the HtmlElement class.

### 1. Create the new HTML element

this feature is by creating a new instance of the HtmlElement class.

```python
from solution import HtmlElement

if __name__ == '__main__':
    h1 = HtmlElement("h1", "WWF", {"id": "h1"})

    p = HtmlElement("p",
                    "The World Wide Fund for Nature (WWF) is an international organization working on issues regarding the conservation, research and restoration of the environment, formerly named the World Wildlife Fund. WWF was founded in 1961.",
                    {"id": "p"})

    section = HtmlElement("section", [h1, p], {"id": "section"})

```

## 2. render HTML element

print the element as HTML format.
Note that it will also return from str method.

```python
from solution import HtmlElement

if __name__ == '__main__':
    h1 = HtmlElement("h1", "WWF", {"id": "h1"})

    p = HtmlElement("p",
                    "The World Wide Fund for Nature (WWF) is an international organization working on issues regarding the conservation, research and restoration of the environment, formerly named the World Wildlife Fund. WWF was founded in 1961.",
                    {"id": "p"})

    section = HtmlElement("section", [h1, p], {"id": "section"})

    print(HtmlElement.render(section))
```

## 3. Append some element to a parent

this feature is by using the append method to add a child to a parent.

```python
from solution import HtmlElement

if __name__ == '__main__':
    h2 = HtmlElement("h2", "Google Chrome", {"id": "h2"})

    p = HtmlElement("p",
                    "Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!",
                    {"id": "p"})

    article = HtmlElement("article", [h2, p], {"id": "article"})

    print(article)

```

## 4. Find elements by attributes

this feature is by using the find_by_attribute method to find elements by attributes.

```python
from solution import HtmlElement

if __name__ == '__main__':
    h1 = HtmlElement("h1", "WWF", {"id": "h1"})

    p = HtmlElement("p",
                    "The World Wide Fund for Nature (WWF) is an international organization working on issues regarding the conservation, research and restoration of the environment, formerly named the World Wildlife Fund. WWF was founded in 1961.",
                    {"id": "p"})

    section = HtmlElement("section", [h1, p], {"id": "section"})

    result = HtmlElement.find_elements_by_attribute(section, "id", "p")

    for element in result:
        print(element, "--------------------------------------------")
```

## 5. Find elements by tag name

this feature is by using the find_elements_by_tag method to find elements by tag name.

```python
from solution import HtmlElement

if __name__ == '__main__':
    h1 = HtmlElement("h1", "WWF", {"id": "h1"})

    p = HtmlElement("p",
                    "The World Wide Fund for Nature (WWF) is an international organization working on issues regarding the conservation, research and restoration of the environment, formerly named the World Wildlife Fund. WWF was founded in 1961.",
                    {"id": "p"})

    section = HtmlElement("section", [h1, p], {"id": "section"})

    result = HtmlElement.find_elements_by_tag(section, "section")

    for element in result:
        print(element, "--------------------------------------------")
```

## 6. Render full HTML file

this feature is by using the render_html_file method to render full HTML file.

```python
from solution import HtmlElement

if __name__ == '__main__':
    h1 = HtmlElement("h1", "WWF", {"id": "h1"})

    p = HtmlElement("p",
                    "The World Wide Fund for Nature (WWF) is an international organization working on issues regarding the conservation, research and restoration of the environment, formerly named the World Wildlife Fund. WWF was founded in 1961.",
                    {"class": "paragraph"})

    section = HtmlElement("section", [h1, p], {"id": "section"})

    h2 = HtmlElement("h2", "Google Chrome", {"id": "h2"})

    p = HtmlElement("p",
                    "Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!",
                    {"class": "paragraph"})

    article = HtmlElement("article", [h2, p], {"id": "article"})

    div = HtmlElement("div", [section, article], {"id": "div"})

    print(HtmlElement.render_html_file(div))
```

