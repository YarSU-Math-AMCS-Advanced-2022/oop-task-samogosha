from Catalog import Product_Catalog
from Observer import Observer
from Product import Product

class Product_Shop(Observer):
    __instance = None
    

    def __init__(self, catalog: Product_Catalog):
        if not Product_Shop.__instance:
            Product_Shop.__instance = self
            self.hash_table = [0]*1e8

    def update(self, old_product, product):
        updated_prod = self.find_product(old_product)
        updated_prod.copy(product)


    @classmethod
    def getInstance(cls, catalog: Product_Catalog):
        if not cls.__instance:
            cls.__instance = Product_Shop(catalog)
        return cls.__instance
    
    def find_product(self, product):
        return self.catalog.find_product(product)


    def sort_by_price(self):
        self.catalog.sort_by_price()

    def show_catalog(self):
        for product in self.catalog.get_children_list():
            product.Product_print()
            print()
            
    def get_hash(self, product: Product):
        return hash(product.product_name)
    
    def add_to_hash(self, product: Product):
        self.hash_table[self.get_hash(product) % len(self.hash_table)] = product


    