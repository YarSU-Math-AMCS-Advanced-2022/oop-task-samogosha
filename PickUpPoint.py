from Product import Product
from Store import Store
from Cart import Cart

class PickUpPoint:
    def __init__(self, address):
        self.address = address
        self.packages = []  # список посылок, принятых на пункт выдачи

    def add_package(self, package):
        self.packages.append(package)
        print(f"Посылка №{package} добавлена на пункт выдачи {self.address}")

    def remove_package(self, package):
        if package in self.packages:
            self.packages.remove(package)
            print(f"Посылка №{package} удалена с пункта выдачи {self.address}")
        else:
            print(f"Посылка №{package} не найдена на пункте выдачи {self.address}")

    def display_packages(self):
        print(f"Посылки на пункте выдачи {self.address}: {', '.join(self.packages)}")