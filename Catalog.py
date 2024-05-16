from Product import Product

class Product_Catalog:
    # def __init__(self, products: list[Product]):
    #     self.__products_list = products
        
    # def get_products_list(self):
    #     return self.__products_list
    
    # def set_products_list(self, new_product_list: list[Product]):
    #     self.__products_list = new_product_list
        
    # def add_product_to_list(self, new_product: Product):
    #     self.__products_list.append(new_product)
        
    # def delete_product_from_list(self, our_product: Product):
    #     if self.__products_list.count(our_product):
    #         self.__products_list.remove(our_product)
    #     else:
    #         print('We dont have this product in catalog')
        
    # def sort_by_price(self):
    #     self.__products_list = sorted(self.__products_list, 
    #                              key = lambda x: x.price)