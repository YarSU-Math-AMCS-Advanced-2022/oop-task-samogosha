import enum 

class Product_Type(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

# Класс "Товар"
class Product:
    def __init__(self, product_name = None, 
                
                 product_type = None, 
                 product_price = None, 
                 product_photo = None,
                 product_stock_quantity = None,
                 product_description = None):
        self.product_name = product_name
        self.type = product_type
        self.price = product_price
        self.photo = product_photo
        self.stock_quantity = product_stock_quantity
        self.description = product_description
    
    def create_product(self):
        #!!!!ДОПИСАТЬ
        a = int(input())
        self.type = a
    
    def Select_Product_Type(self, our_type):
        if our_type == Product_Type.FIRST.value:
            self.type = Product_Type.FIRST
        elif our_type == Product_Type.SECOND.value:
            self.type = Product_Type.SECOND
        elif our_type == Product_Type.THIRD.value:
            self.type = Product_Type.THIRD
        else:
            print('Invalid input of product type')
            
    def Product_print(self):
        print(f"Product_name = {self.product_name}" + "\n" 
              + f"Product_type = {self.type}" + "\n"
              + f"Product_price = {self.price}" + "\n"
              + f"Product_photo = {self.photo}" + "\n"
              + f"Product_stock_quantity = {self.stock_quantity}" + "\n"
              + f"Product_description = {self.description}")
        
    def copy(self, product):
        self.product_name = product.product_name
        self.type = product.type
        self.price = product.price
        self.photo = product.photo
        self.stock_quantity = product.stock_quantity
        self.description = product.description
    
    def is_similar(self, product):
        if (self.product_name == product.product_name and
            self.type == product.type and
            self.price == product.price and
            self.photo == product.photo and
            self.stock_quantity == product.stock_quantity and
            self.description == product.description):
            return True
        else:
            return False