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
    
    def find_father(self, child):

        if(self.product == None):
            if child in self.children:
                return self
            
            for child_node in self.children:
                buff = child_node.find_father(child)
                if buff != None and child in buff.children:
                    return buff
        return

    def find_by_name(self, name: str):
        if self.name == name:
            return self
        if(self.product == None):
            for child in self.children:
                buff = child.find_by_name(name)
                if buff != None and buff.name == name:
                    return buff
        return None

