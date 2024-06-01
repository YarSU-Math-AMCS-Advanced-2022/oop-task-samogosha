from Product.Product import Product
from Store.Store import Store
from Cart.Cart import Cart

class PickUpPoint:
    def __init__(self, address: str):
        self.address = address
        self.packages = []  # список посылок, принятых на пункт выдачи

    def add_package(self, package, flag_for_print: bool):
        self.packages.append(package)
        if flag_for_print:
            print(f"The order №{package.order_id} has been added to the delivery point {self.address}")

    def remove_package(self, package):
        if package in self.packages:
            self.packages.remove(package)
            print(f"The order №{package.order_id} has been deleted from the delivery point {self.address}")
        else:
            print(f"The order №{package.order_id} not found at the delivery point {self.address}")

    def get_packages_id(self):
        list_of_id = []
        
        for pack in self.packages:
            list_of_id.append(str(pack.order_id))
        
        return list_of_id


    def display_packages(self):
        print(f"Orders at the delivery point {self.address}: {', '.join(self.get_packages_id())}")