import enum 


# Класс "Товар"
class Product:
    def __init__(self, product_name = None, 
                 product_price = None, 
                 product_stock_quantity = None,
                 product_description = None):
        self.product_name = product_name
        self.price = product_price
        self.stock_quantity = product_stock_quantity
        self.description = product_description
    
    def create_product(self):
        #!!!!ДОПИСАТЬ
        a = int(input())
        self.type = a
    
            
    def Product_print(self):
        print(f"Product_name = {self.product_name}" + "\n" 
              + f"Product_price = {self.price}" + "\n"
              + f"Product_stock_quantity = {self.stock_quantity}" + "\n"
              + f"Product_description = {self.description}")
        
    def copy(self, product):
        self.product_name = product.product_name
        self.price = product.price
        self.stock_quantity = product.stock_quantity
        self.description = product.description
    
    def is_similar(self, product):
        if (self.product_name == product.product_name and
            self.price == product.price and
            self.stock_quantity == product.stock_quantity and
            self.description == product.description):
            return True
        else:
            return False