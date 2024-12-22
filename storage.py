class Storage:
    def __init__(self, parent_global):
        self.storage = {}
        self.parent = parent_global

    def add_value(self, value, name):
        self.storage[name] = value

    def update_value(self, value, name):
        if name in self.storage.keys():
            self.add_value(value, name)
        else:
            if self.parent != None:
                return self.parent.update_value(value, name)
            raise Exception(f"variable '{name}' not declared yet.")

    def get_value(self, name):
        if name in self.storage.keys():
            return self.storage[name]
        else:
            if self.parent != None:
                return self.parent.get_value(name)
            raise Exception(f"variable '{name}' not declared yet.")

