from Product.Product import Product
from Catalog.Catalog import ProductCatalog
from Shop.Shop import ProductShop
from Store.Store import Store
from Cart.Cart import Cart
from Order.Order import Order
from PickUpPoint.PickUpPoint import PickUpPoint
from copy import deepcopy

class MarketplaceFacade:
    def __init__(self):
        self.product_shop = ProductShop()
        self.product_shop.add_category_from_file('CatalogComponent\category_data.txt')
        self.product_shop.add_products_from_file('Product\data_of_products.txt')
        self.store = Store(list())
        self.cart = Cart()
        self.order = Order()
        self.add_prod_from_shop_to_store()

        FilePickUpPoint = open('PickUpPoint/ListPickUpPoint.txt', 'r')
        ListPoint = FilePickUpPoint.readlines()
        for i in range(len(ListPoint)):
            ListPoint[i] = ListPoint[i][:-1]

        self.list_of_pickup_points: list[PickUpPoint] = \
            self.create_list_of_pickup_points(ListPoint)
        self.add_orders_from_file()


    def create_list_of_pickup_points(self, list_of_pickup_points):
        list_of_points = []
        for points in list_of_pickup_points:
            list_of_points.append(PickUpPoint(points))
        return list_of_points
    

    def add_product_to_catalog(self):
        print('-----------------------------')
        print('Select a category to add a product:')
        name_category = input()
        
        exist = self.product_shop.find_in_catalog(name_category)
        if exist == None:
            print('Incorrect category, please try again')
            return
        new_product = Product()
        new_product.create_product()
        self.product_shop.add_product_to_catalog(name_category, new_product)
        print('*Product successfully added to the marketplace*')
        print('-----------------------------')
        

    def add_category_to_catalog(self):
        print('-----------------------------')
        print('Select a category to add a new category:')
        name_category = input()
        exist = self.product_shop.find_in_catalog(name_category)
        if exist == None:
            print('Incorrect category, please try again')
            return
        print('Enter new category name:')
        new_name_category = input()
        self.product_shop.add_category_to_catalog(name_category, new_name_category)
        print('*Category successfully added to the marketplace*')
        print('-----------------------------')


    def remove_product_from_catalog(self):
        print('-----------------------------')
        print('Select the product you want to delete:')
        our_product_name = input()
        our_item = self.product_shop.find_in_catalog(our_product_name)
        if our_item == None:
            print('Incorrect product, please try again')
            return
        self.product_shop.remove_product_from_catalog(our_item.product)
        print('*Product successfully removed from the marketplace*')
        print('-----------------------------')
        

    def remove_category_from_catalog(self):
        print('-----------------------------')
        print('Select the category you want to delete:')
        our_category_name = input()
        exist = self.product_shop.find_in_catalog(our_category_name)
        if exist == None:
            print('Incorrect category, please try again')
            return
        our_item = self.product_shop.find_in_catalog(our_category_name)
        self.product_shop.remove_category_from_catalog(our_item)
        print('*Category successfully removed from the marketplace*')
        print('-----------------------------')


    def add_to_cart(self):
        print('-----------------------------')
        print('What product would you like to add to your cart?')
        product_name = input()
        our_item = self.product_shop.find_in_catalog(product_name)
        if our_item == None:
            print('Incorrect product, please try again')
            return
        count = int(input(f'How many {product_name} would you like to add?\n'))
        self.cart.add_to_cart(product_name, count)
        print('*Products successfully added to cart*')
        print('-----------------------------')


    def edit_cart(self):
        print('-----------------------------')
        print('What product you want to edit in cart?')
        product_name = input()
        if product_name not in self.cart.cart_dictionary:
            print('This item is not in your cart!')
        else:
            print('Do you want to remove this product from your cart or change its quantity? Print \'d\' or \'c\':')
            action = input()
            if action == 'c':
                quantity_of_product = int(input('Enter the number of products to be removed:\n'))
                self.cart.rem_from_cart(product_name, quantity_of_product)
            elif action == 'd':
                self.cart.rem_from_cart(product_name)
            else:
                print('Unknown command!')
        print('-----------------------------')
        

    def show_cart(self):
        print('-----------------------------')
        if len(self.cart.cart_dictionary) == 0:
            print('Your shopping cart is empty')
        else:
            print('Your shopping cart looks like this:')
            self.cart.show_cart()
        print('-----------------------------')


    def place_order(self):
        print('-----------------------------')
        self.order.create_order(self.cart, self.store)
        
        pickup_point = PickUpPoint(self.order.destination)
        
        if self.order.complete_order(pickup_point):
            print('\nYour order has been placed')
            order_total = self.order_total()
            self.order.order_total = order_total
            print('Order total:', order_total)
            self.order.payment_type = self.select_payment_type()
            our_pick_up_point = next((pick_up_point for pick_up_point in self.list_of_pickup_points if pick_up_point.address == self.order.destination ), None)
            our_pick_up_point.add_package(deepcopy(self.order), True)
            self.show_order()
            self.order.add_order_to_output_file()
            self.order.user_cart.clear_cart()

        print('-----------------------------')
 
        
    def show_orders_at_the_pickup_point(self):
        print('-----------------------------')
        for points in self.list_of_pickup_points:
            print(points.address, sep=' ')
        pickup_point_name = input('\nSelect the pickup point from the line above:\n')
        our_pick_up_point = next((pick_up_point for pick_up_point in self.list_of_pickup_points if pick_up_point.address == pickup_point_name), None)
        for package in our_pick_up_point.packages:
            package.show_order()
        print('-----------------------------')


    def create_pickup_point(self):
        print('-----------------------------')
        address = input('Enter the address of the pick-up point:\n')
        
        file_list_of_point = open('PickUpPoint/ListPickUpPoint.txt', 'a')

        for pickup in self.list_of_pickup_points:
            if pickup.address == address:
                file_list_of_point.close()
                return pickup
        
        address += '\n'
        new_pickup: PickUpPoint = PickUpPoint(address)
        self.list_of_pickup_points.append(new_pickup)
        file_list_of_point.write(address)
        file_list_of_point.close()
        print('-----------------------------')
        return new_pickup
        
        
    def order_total(self):
        order_total = 0

        for key in self.cart.cart_dictionary.keys():
            our_item = self.product_shop.find_in_catalog(key)
            order_total += our_item.product.price * self.cart.cart_dictionary[key]
        
        return order_total
    

    def select_payment_type(self):
        print('-----------------------------')
        print('Choose a convenient way to pay for your order: cash on delivery (type \'c\')| bank card (type \'bc\')')
        payment_type = input()

        if payment_type != 'c' or payment_type != 'bc':
            while payment_type != 'c' and payment_type != 'bc':
                print('Incorrect payment method! Chose the right one')
                payment_type = input()
        
        print('-----------------------------')
        return payment_type
    

    def show_order(self):
        self.order.show_order()


    def cancel_order(self):
        self.order = Order()
        print('*Order successfully canceled*')


    def add_prod_from_shop_to_store(self):
        if len(self.product_shop.hash_table) == 0:
            return
        for key in self.product_shop.hash_table:
            self.store.add_product(self.product_shop.hash_table[key])


    def add_orders_from_file(self):
        file = open('Marketplace/data_orders.txt', 'r')
        file_list = file.readlines()
        our_pick_up_point = PickUpPoint('')

        for line in file_list:
            order_data = line.split()
            our_pick_up_point = next((pick_up_point for pick_up_point 
                                    in self.list_of_pickup_points 
                                    if pick_up_point.address == order_data[3]), None)
            
            if our_pick_up_point != None:
                cur_order = Order(int(order_data[0]), ' '.join(order_data[1:3]), order_data[3], Cart(), self.store, int(order_data[4]), order_data[5])
                
                if len(order_data) > 7:
                    new_cart = Cart()

                    for i in range(7, len(order_data), 2):
                        new_cart.add_to_cart(order_data[i - 1], int(order_data[i]))

                cur_order.user_cart = new_cart
                our_pick_up_point.add_package(cur_order, False)


    def find_order_in_pickup_point(self):
        pickup_point = input('Enter point where you want to search: ')
        id_package = int(input('Enter id of order: '))
        self.find_order_by_id(pickup_point, id_package).show_order()
    

    def find_order_by_id(self, pickup_point, id_package: int):
        our_pick_up_point = next((pick_up_point for pick_up_point in self.list_of_pickup_points if pick_up_point.address == pickup_point), None)
        package = our_pick_up_point.search_order_by_id(id_package)
        return package




       
