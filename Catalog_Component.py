class Catalog_Component:
    def __init__(self, name):
        self.name = name

    def display(self):
        pass


class Composite(Catalog_Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(self.name)
        for child in self.children:
            print("- ", end="")
            child.display()