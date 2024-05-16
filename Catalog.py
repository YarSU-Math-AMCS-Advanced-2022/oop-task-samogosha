from Product import Product
from Catalog_Component import Composite

class Product_Catalog(Composite):
    def get_children_list(self):
        return self.children
    
    # def set_products_list(self, new_product_list: list[Product]):
    #     self.__products_list = new_product_list
        
    # def add_product_to_list(self, new_product: Product):
    #     self.__products_list.append(new_product)
        
    # def delete_product_from_list(self, our_product: Product):
    #     if self.__products_list.count(our_product):
    #         self.__products_list.remove(our_product)
    #     else:
    #         print('We dont have this product in catalog')
        
    def sort_by_price(self):
        for child in self.children:
            if child.product != None:
                self.children = sorted(self.children,
                               key = lambda x: x.product.price)
            else:
                child.sort_by_price()

