from Product import Product
from Catalog import Product_Catalog
from Shop import Product_Shop
from Store import Store
from Cart import Cart
from Order import Order
from PickUpPoint import PickUpPoint

# Product_Shop, Store, Cart, Order

class MarketplaceFacade:
    def __init__(self, Product_Shop: Product_Shop, Store: Store, Cart: Cart, Order: Order):
        self.product_shop = Product_Shop
        self.store = Store
        self.cart = Cart
        self.order = Order
        

    def add_product_to_catalog(self):
        print('Select a category to add a product:')
        name_category = input()
        
        exist = self.product_shop.find_in_catalog(name_category)
        if exist == None:
            print('Incorrect category, please try again')
            return
        new_product = Product()
        new_product.create_product()
        self.product_shop.add_product_to_catalog(name_category, new_product)
        print("Product successfully added to the marketplace.")
        
    def add_category_to_catalog(self):
        print('Select a category to add a new category: ')
        name_category = input()
        exist = self.product_shop.find_in_catalog(name_category)
        if exist == None:
            print('Incorrect category, please try again')
            return
        print('Enter new category name: ')
        new_name_category = input()
        self.product_shop.add_category_to_catalog(name_category, new_name_category)
        print('Category successfully added to the marketplace.')

    def remove_product_from_catalog(self):
        print('Select the product you want to delete: ')
        our_product_name = input()
        our_item = self.product_shop.find_in_catalog(our_product_name)
        if our_item == None:
            print('Incorrect product, please try again')
            return
        self.product_shop.remove_product_from_catalog(our_item.product)
        print("Product successfully removed from the marketplace.")
        
    def remove_category_from_catalog(self):
        print('Select the category you want to delete: ')
        our_category_name = input()
        exist = self.product_shop.find_in_catalog(our_category_name)
        if exist == None:
            print('Incorrect category, please try again')
            return
        our_item = self.product_shop.find_in_catalog(our_category_name)
        self.product_shop.remove_category_from_catalog(our_item)
        print("Category successfully removed from the marketplace.")
        
    def add_to_cart(self):
        print('What product would you like to add to your cart? ')
        product_name = input()
        our_item = self.product_shop.find_in_catalog(product_name)
        if our_item == None:
            print('Incorrect product, please try again')
            return
        count = int(input(f'How many {product_name} would you like to add? '))
        self.cart.add_to_cart(product_name, count)
        print("Products successfully added to cart.")

    def edit_cart(self):
        print('What product you want to edit in cart?')
        product_name = input()
        if product_name not in self.cart.cart_dictionary:
            print('This item is not in your cart!')
        else:
            print('Do you want to remove this product from your cart or change its quantity? Print \'d\' or \'c\':')
            action = input()
            if action == 'c':
                quantity_of_product = int(input('Enter the number of products to be removed: '))
                self.cart.rem_from_cart(product_name, quantity_of_product)
            elif action == 'd':
                self.cart.rem_from_cart(product_name)
            else:
                print('Unknown command!')
        
    def show_cart(self):
        if len(self.cart.cart_dictionary) == 0:
            print('Your shopping cart is empty')
        else:
            print('Your shopping cart looks like this:')
            self.cart.show_cart()

    def place_order(self):
        self.order.create_order(self.cart, self.store)
        pickup_point = PickUpPoint(self.order.destination)
        
        if self.order.complete_order(pickup_point):
            print('Your order has been placed')
            order_total = self.order_total()
            self.order.order_total = order_total
            print('Order total:', order_total)
            self.order.payment_type = self.select_payment_type()
            pickup_point.add_package(self.order)
            self.show_order()
            self.order.user_cart.clear_cart()


        #self.order.user_cart = Cart()

    def order_total(self):
        order_total = 0

        for key in self.cart.cart_dictionary.keys():
            our_item = self.product_shop.find_in_catalog(key)
            order_total += our_item.product.price * self.cart.cart_dictionary[key]
        
        return order_total
    
    def select_payment_type(self):
        print('Choose a convenient way to pay for your order: cash on delivery (type \'c\')| bank card (type \'bc\')')
        payment_type = input()

        if payment_type != 'c' or payment_type != 'bc':
            while payment_type != 'c' and payment_type != 'bc':
                print('Incorrect payment method! Chose the right one')
                payment_type = input()
        
        return payment_type
    
    def show_order(self):
        print('Order id:', self.order.order_id)
        print('Order recipient:', self.order.recipient)
        print('Order destination:', self.order.destination.address)
        print('Order products:')
        print('-------------------------------------------------------------------')
        self.order.user_cart.show_cart()
        print('-------------------------------------------------------------------')
        print('Order total:', self.order.order_total)
        print('Order payment type:', self.order.payment_type)

    def cancel_order(self):
        self.order = Order()
        print('Order successfully canceled')

    def add_prod_from_shop_to_store(self):
        if len(self.product_shop.hash_table) == 0:
            return
        for key in self.product_shop.hash_table:
            self.store.add_product(self.product_shop.hash_table[key])