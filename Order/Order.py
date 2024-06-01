from abc import ABCMeta, abstractmethod
from Product.Product import Product
from copy import deepcopy
from Store.Store import Store
from Cart.Cart import Cart
from PickUpPoint.PickUpPoint import PickUpPoint
import random

class Order:

    def __init__(self, order_id = None, 
                       recipient = None, 
                       destination: str | None = None,
                       user_cart: Cart | None = None, 
                       our_store: Store | None = None,
                       order_total: int | None = None,
                       payment_type: str | None = None):
        self.order_id = order_id
        self.recipient = recipient
        self.destination = destination
        self.user_cart = user_cart
        self.store = our_store
        self.order_total = order_total
        self.payment_type = payment_type

    def fix_cart(self):
        flag = True

        for key in self.user_cart.cart_dictionary.keys():
            some_product = self.store.find_by_name(key)
            if some_product.stock_quantity < self.user_cart.cart_dictionary[key]:
                self.user_cart.cart_dictionary[key] = some_product.stock_quantity
                flag = False

        return flag
    
    def create_order(self, cart: Cart, store: Store):
        self.order_id = random.randint(10000000,100000000-1)
        self.recipient = input('Enter your surname and first name: ')
        list_places = ['Zavolga', 'Bragino', 'Center']
        print(*list_places)
        temp_dest = input('Select a pickup point from the line above: ')
        flag = False
        
        while flag == False:      
            if temp_dest == 'Zavolga':
                self.destination = 'Zavolga'
                flag = True
            elif temp_dest == 'Bragino':
                self.destination = 'Bragino'
                flag = True
            elif temp_dest == 'Center':
                self.destination = 'Center'
                flag = True
            else:
                print('Incorrect adress of pickup point, please try again')
                temp_dest = input('Select a pickup point from the line above: ')


        self.user_cart = cart
        self.store = store
        

    def complete_order(self, pick_up_point: PickUpPoint):
        if self.fix_cart():
            for key in self.user_cart.cart_dictionary.keys():
                some_product = self.store.find_by_name(key)
                self.store.change_product(some_product, 
                                          -self.user_cart.cart_dictionary[key])
                self.destination = pick_up_point.address
            #self.destination.add_package(self)
        else:
            print('Your shopping cart has been updated')
            return False
        return True
    
    def show_order(self):
        print('Order id:', self.order_id)
        print('Order recipient:', self.recipient)
        print('Order destination:', self.destination)
        print('Order products:')
        print('-------------------------------------------------------------------')
        self.user_cart.show_cart()
        print('-------------------------------------------------------------------')
        print('Order total:', self.order_total)
        print('Order payment type:', self.payment_type)
    
    def add_order_to_output_file(self):
        file = open('Marketplace\data_orders.txt', 'a')
        order_data = str(self.order_id) + ' ' + \
            str(self.recipient) + ' ' + \
            str(self.destination) + ' ' + \
            str(self.order_total) + ' ' + \
            str(self.payment_type) + ' ' + \
            self.user_cart.return_products_from_cart()
        
        file.write(order_data)
        file.close()
        