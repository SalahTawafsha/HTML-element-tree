class HTMLNanoframework:
    def __init__(self, name, value, attributes=None):
        if attributes is None:
            attributes = {}
        self.name = name
        self.value = value
        self.attributes = attributes


att = HTMLNanoframework("h1", "Hello World", {"id": "test"})

print(att.name)
print(att.value)
print(att.attributes)
