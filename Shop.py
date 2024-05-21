from Catalog import Product_Catalog
from Observer import Observer
from Product import Product

class Product_Shop(Observer):
    __instance = None

    def __init__(self, catalog: Product_Catalog):
        if not Product_Shop.__instance:
            Product_Shop.__instance = self
            self.catalog = catalog

    def update(self, product, message):
        if message == 'Out of stock':
            


    @classmethod
    def getInstance(cls, catalog: Product_Catalog):
        if not cls.__instance:
            cls.__instance = Product_Shop(catalog)
        return cls.__instance

    def sort_by_price(self):
        self.catalog.sort_by_price()

    def show_catalog(self):
        for product in self.catalog.get_products_list():
            product.Product_print()
            print()

    