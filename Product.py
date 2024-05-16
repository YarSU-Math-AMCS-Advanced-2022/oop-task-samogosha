import enum 

class Product_Type(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

# Класс "Товар"
class Product:
    def __init__(self, product_name: str, 
                 
                 #ЗДЕСЬ ВРЕМЕННО INT
                 product_type: int, 
                 
                 
                 product_price: int, 
                 product_photo: str,
                 product_stock_quantity: int,
                 product_description : str):
        self.product_name = product_name
        self.type = product_type
        self.price = product_price
        self.photo = product_photo
        self.stock_quantity = product_stock_quantity
        self.description = product_description
    
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