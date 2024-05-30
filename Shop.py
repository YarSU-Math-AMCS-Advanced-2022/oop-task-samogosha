from Catalog import Product_Catalog
from Observer import Observer
from Product import Product
from PickUpPoint import PickUpPoint

class Product_Shop(Observer):
    __instance = None
    

    def __init__(self):
        if not Product_Shop.__instance:
            Product_Shop.__instance = self
            self.catalog = Product_Catalog('root')
            self.hash_table = dict()
            self.pick_up_points = []

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
        delete = self.catalog.find_by_name(product.product_name)
        self.catalog.find_father(delete).remove(delete)
        
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
        self.hash_table[self.get_hash(product) % 10000] = product

    def add_category_to_catalog(self, category_name: str, new_category_name: str):
        new_category = Product_Catalog(new_category_name)
        self.find_in_catalog(category_name).add(new_category)

    def add_product_to_catalog(self, category_name: str, product: Product):
        new_product = Product_Catalog(product.product_name, product)
        self.find_in_catalog(category_name).add(new_product)
        self.add_to_hash(product) 

    def add_products_from_file(self, file_name: str):
        file = open(file_name)
        for line in file:
            if line == '\n':
                break
            lst = line.split()
            prod = Product(lst[1], int(lst[2]), int(lst[3]), ' '.join(lst[4:]))
            self.add_product_to_catalog(lst[0], prod)
        file.close()

    def add_category_from_file(self, file_name: str):
        file = open(file_name)
        for line in file:
            lst = line.split()
            self.add_category_to_catalog(lst[0], lst[1])
        file.close()