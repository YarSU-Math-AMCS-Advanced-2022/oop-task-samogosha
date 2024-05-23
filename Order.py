from abc import ABCMeta, abstractmethod
from Product import Product
from copy import deepcopy
from Store import Store
from Cart import Cart

class Order:


    def __init__(self, title, order_id, recipient, destination, user_cart: Cart, our_store: Store):
        self.title = title
        self.order_id = order_id
        self.recipient = recipient
        self.destination = destination
        self.user_cart = user_cart
        self.store = our_store

    def fix_cart(self):
        flag = True

        for key in self.user_cart.cart_dictionary.keys():
            some_product = self.store.find_by_name(key)
            if some_product.stock_quantity < self.user_cart.cart_dictionary[key]:
                self.user_cart.cart_dictionary[key] = some_product.stock_quantity
                flag = False
        
        return flag
                
    

    def complete_order(self):
        if self.fix_cart():
            for key, value in self.user_cart:
                some_product = self.store.find_by_name(key)
                self.store.change_product(some_product, -value)
        else:
            print('Your shopping cart has been updated')