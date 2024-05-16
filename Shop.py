from Catalog import Product_Catalog

class Product_Shop:
    def __init__(self, catalog: Product_Catalog):
        self.catalog = catalog
    
    def sort_by_price(self):
        self.catalog.sort_by_price()

    def show_catalog(self):
        for i in self.catalog.get_products_list():
            i.Product_print()
            print()