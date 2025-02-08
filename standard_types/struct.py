class StructItem:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}: {self.value}"

    def to_string(self):
        return f"{self.name}: {self.value}"

class StructType:
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f"{{ {", ".join(map(lambda t: t.to_string(), self.values))} }}"

    def to_string(self):
        return f"{self.name}: {self.value}"
