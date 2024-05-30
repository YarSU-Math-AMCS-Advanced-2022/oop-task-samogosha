from abc import ABCMeta, abstractmethod
from Product import Product
from copy import deepcopy
from Store import Store
from Cart import Cart
from PickUpPoint import PickUpPoint

class Order:

    def __init__(self, order_id = None, 
                       recipient = None, 
                       destination: PickUpPoint | None = None,
                       user_cart: Cart | None = None, 
                       our_store: Store | None = None):
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
    
    def create_order(self, cart: Cart, store: Store):
        self.order_id = 0
        self.recipient = input('Enter your surname and first name: ')
        print('Zavolga', 'Bragino', 'Center')
        self.destination = input('Select a pickup point from the line above: ')
        self.user_cart = cart
        self.store = store
        

    def complete_order(self, pick_up_point: PickUpPoint):
        if self.fix_cart():
            for key in self.user_cart.cart_dictionary.keys():
                some_product = self.store.find_by_name(key)
                self.store.change_product(some_product, -self.user_cart.cart_dictionary[key])
                self.destination = pick_up_point
            self.destination.add_package(self.order_id)
        else:
            print('Your shopping cart has been updated')
        return self