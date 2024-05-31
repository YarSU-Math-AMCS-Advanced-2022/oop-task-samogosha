from Product.Product import Product

class CatalogComponent:
    def __init__(self, name, product: Product | None = None):
        self.name = name
        self.product = product

    def display(self):
        pass


class Composite(CatalogComponent):
    product = None

    def __init__(self, name, product: Product | None = None):
        if product != None:
            super().__init__(name, product)
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
        # print(self.product.product_name)
        # if self.product != None:
        #    print(self.product.product_name)
        for child in self.children:
            if child.product == None:
                child.display(cnt_space + 1)
            else:
                # print('-' * (cnt_space + 1), child.name, sep='')
                print('-'*(cnt_space + 1), end='')
                print(f"{child.name}, It's price = {child.product.price},", end=' ') 
                print(f"On store: {child.product.stock_quantity} items,", end=' ')
                print(f"Product description: {child.product.description}")