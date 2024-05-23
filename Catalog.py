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
    
    def find_product(self, product):
        if self.product != None:
            return
        for prod in self.children:
            if prod.product != None:
                if product.is_similar(prod.product):
                    return prod.product
                return
            else:
                return prod.find_product(product)
                

