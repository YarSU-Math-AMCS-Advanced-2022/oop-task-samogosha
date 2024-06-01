from abc import ABCMeta, abstractmethod
from Product.Product import Product
from copy import deepcopy

class Cart:
    def __init__(self):
        self.cart_dictionary = dict()
            
    def clear_cart(self):
        self.cart_dictionary = dict()

    def add_to_cart(self, name_product: str, count: int):
        if name_product not in self.cart_dictionary.keys():
            self.cart_dictionary[name_product] = 0
        self.cart_dictionary[name_product] += count


    def rem_from_cart(self, name_product: str, count = None):
        if count == None or count >= self.cart_dictionary[name_product]:
            self.cart_dictionary.pop(name_product)
        else:
            self.cart_dictionary[name_product] -= count
            
    def show_cart(self):
        for keys in self.cart_dictionary:
            print(keys, self.cart_dictionary[keys])
            
    def return_products_from_cart(self):
        our_products = ''
        for keys in self.cart_dictionary:
            our_products += str(keys) + ' '+ str(self.cart_dictionary[keys])
        return our_products