from Product import Product
from Catalog_Component import Composite

class Product_Catalog(Composite):
    def get_children_list(self):
        return self.children
       
    def sort_by_price(self):
        for child in self.children:
            if child.product != None:
                self.children = sorted(self.children,
                               key = lambda x: x.product.price)
            else:
                child.sort_by_price()

