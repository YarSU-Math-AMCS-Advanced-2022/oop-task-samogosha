from copy import deepcopy
from Observer import Observable
from Product import Product

class Store(Observable):

    def __init__(self, products_list: list[Product]):
        self.observers = []
        self.products_list = products_list 


    def notify_observers(self, old_product, product):
        for observer in self.observers:
            observer.update(old_product, product)

    def update_product_quantity(self, old_product, product):
        self.notify_observers(old_product, product)

    def add_product(self, product):
        if product not in self.products_list:
            self.products_list.append(product)
    
    def delete_product(self, product):
        self.products_list.remove(product)

    def change_product(self, product, value):
        old_product = deepcopy(product)
        ind = self.products_list.index(product)   
        self.products_list[ind].stock_quantity += value

        if product in self.products_list:
            if self.products_list[ind].stock_quantity <= 0:
                self.products_list[ind].stock_quantity = 0
                self.update_product_quantity(old_product, product)

    def find_by_name(self, product_name: str):
        for product in self.products_list:
            if product.product_name == product_name:
                return product
        return None
            