
class Catalog_Component:
    def __init__(self, name, product = None):
        self.name = name
        self.product = product

    def display(self):
        pass


class Composite(Catalog_Component):
    product = None

    def __init__(self, name, product = None):
        if product != None:
            super().__init__(name, product = None)
            self.product = product
        else:
            super().__init__(name)
            self.children = []

    def add(self, component):
        if self.product == None:
            self.children.append(component)
        else:
            print('This component is not a category!')

    def remove(self, component):
        self.children.remove(component)

    def display(self, cnt_space):
        print('-' * cnt_space, self.name, sep='')
        # if self.product == None:
        #     for child in self.children:
        #         print("- ", end="")
        #         child.display()
        for child in self.children:
            if child.product == None:
                child.display(cnt_space + 1)
            else:
                print('-' * (cnt_space + 1), child.name, sep='')