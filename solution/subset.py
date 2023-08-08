""" create a subset of HTML elements to use it in the unit test """
from HTML.solution.html_element import HtmlElement

form = HtmlElement("form", HtmlElement("h3", "Log in"), {"method": "post", "action": "login.php"})

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

HtmlElement.append(form, [hr, table, br, submit])

print(HtmlElement.render_html(form))
