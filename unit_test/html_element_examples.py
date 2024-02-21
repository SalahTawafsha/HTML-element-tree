""" create a subset of HTML elements to use it in the unit test """
from solution import HtmlElement

h1 = HtmlElement("h1", "", {"id": "test"})

p = HtmlElement("p", "", {"id": "hi"})

section = HtmlElement("section", "", {"id": "section"})
