from Observer import Observable
from Product import Product

class Store(Observable):

    def __init__(self, products_list:list[Product]):
        self.observers = []
        self.products_list = products_list 


    def notify_observers(self, product, message:str):
        if message == 'Out of stock':
            for observer in self.observers:
                observer.update()
        elif message == 'In stock':
            for observer in self.observers:
                observer.update()

    def product_out_of_stock(self, product):

        self.notify_observers(product)

    def product_in_stock(self, product):
        self.notify_observers(product)

    def add_product(self, product):
        if product not in self.products_list:
            self.products_list.append(product)
    
    def delete_product(self, product):
        self.products_list.remove(product)

    def change_product(self, product, value):
        if product in self.products_list:
            ind = self.products_list.index(product)

            if self.products_list[ind].stock_quantity == 0 and value > 0:
                self.product_in_stock(product)    

            self.products_list[ind].stock_quantity += value

            if self.products_list[ind].stock_quantity <= 0:
                self.products_list[ind].stock_quantity = 0
                self.product_out_of_stock(product)
        