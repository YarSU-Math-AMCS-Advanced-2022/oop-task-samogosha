from Catalog import Product_Catalog
from Observer import Observer
from Product import Product

class Product_Shop(Observer):
    __instance = None
    

    def __init__(self):
        if not Product_Shop.__instance:
            Product_Shop.__instance = self
            self.catalog = Product_Catalog('root')
            self.hash_table = [0] * (10**8)

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

    def find_in_catalog(self, name: str):
        return self.catalog.find_by_name(name)

    def remove_product_from_catalog(self, product: Product):
        self.catalog.find_by_name(product).remove()
        
    def remove_category_from_catalog(self, category: Product_Catalog):
        delete = self.catalog.find_by_name(category.name)
        self.catalog.find_father(delete).remove(delete)

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

    def add_category_to_catalog(self, category_name: str, new_category_name: str):
        new_category = Product_Catalog(new_category_name)
        self.find_in_catalog(category_name).add(new_category)

    def add_product_to_catalog(self, category_name: str, product: Product):
        new_product = Product_Catalog(product.product_name, product)
        self.find_in_catalog(category_name).add(new_product)
        self.add_to_hash(product)  
