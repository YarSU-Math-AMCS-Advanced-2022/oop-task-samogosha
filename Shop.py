from Catalog import Product_Catalog

class Product_Shop:
    '''
    __instance = None
    __catalog = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Product_Shop, cls).__new__(cls)
        return cls.__instance
    
    def __init__(self, catalog: Product_Catalog):
        self.catalog = catalog
    
    
    
    def __init__(self, catalog: Product_Catalog):
        if not Product_Shop.__instance:
            # Product_Shop.__instance = self.getInstance(Product_Shop)
            #self.__instance = self.getInstance()
            #self
            Product_Shop.__instance = self.getInstance(catalog)
            self.catalog = catalog
            
    
    @classmethod
    def getInstance(cls, catalog: Product_Catalog):
        if not cls.__instance:
            cls.__instance = Product_Shop(catalog)
        return cls.__instance
     
    
    def sort_by_price(self):
        self.catalog.sort_by_price()

    def show_catalog(self):
        for i in self.catalog.get_products_list():
            i.Product_print()
            print()
            
    '''
    __instance = None

    def __init__(self, catalog: Product_Catalog):
        if not Product_Shop.__instance:
            Product_Shop.__instance = self
            self.catalog = catalog

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
    