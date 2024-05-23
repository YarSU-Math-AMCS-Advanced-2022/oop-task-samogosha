from abc import ABCMeta, abstractmethod
from Product import Product
from copy import deepcopy

class Cart:
    __instance = None
    cart_dictionary = dict()

    def __init__(self):
        if not Cart.__instance:
            self.__instance = self

    def add_to_cart(self, name_product: str, count: int):
        if name_product not in self.cart_dictionary.keys():
            self.cart_dictionary[name_product] = 0
        self.cart_dictionary[name_product] += count


    def rem_from_cart(self, name_product: str, count = None):
        if count == None:
            self.cart_dictionary.pop(name_product)
        else:
            self.cart_dictionary[name_product] -= count