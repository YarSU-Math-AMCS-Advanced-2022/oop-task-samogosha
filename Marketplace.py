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
        
    def show_cart(self):
        if len(self.cart.cart_dictionary) == 0:
            print('Your shopping cart is empty')
        else:
            print('Your shopping cart looks like this:')
            self.cart.show_cart()

    def place_order(self):
        self.order.create_order(self.cart, self.store)
        pickup_point = PickUpPoint(self.order.destination)
        self.order.complete_order(pickup_point)
        print('Your order has been placed')
        self.order.user_cart.clear_cart()
        #self.order.user_cart = Cart()  

    def cancel_order(self):
        self.order = Order()
        print('Order successfully canceled')

    def add_prod_from_shop_to_store(self):
        if len(self.product_shop.hash_table) == 0:
            return
        for key in self.product_shop.hash_table:
            self.store.add_product(self.product_shop.hash_table[key])