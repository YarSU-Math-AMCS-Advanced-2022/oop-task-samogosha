from Marketplace.Marketplace import MarketplaceFacade
import sys
import os


class Menu():

    def __init__(self, Marketplace: MarketplaceFacade | None = None, user: str | None = None):
        self.Marketplace = Marketplace
        self.user = user
        self.admin_password = '1234'

    
    def log_in(self):
        user = input('Select user profile(Admin|Customer): ')
        if(user.lower() == 'admin' or user.lower() == 'a'):
            password = input('Enter the password: ')
            if password == self.admin_password:
                print('You have successfully logged in as admin!')
                self.user = 'Admin'
            else:
                print('Incorrect password!')
        elif (user.lower() == 'customer' or user.lower() == 'c'):
            self.user = 'Customer'
            print('You have successfully logged in as customer!')
            print('Welcome to marketplace!')


    def show_customer_menu(self):
        print('-----------------------------')
        print('0) Change user')
        print('1) Show catalog')
        print('2) Add product to cart')
        print('3) Edit cart')
        print('4) Show cart')
        print('5) Place an order')
        print('6) Show orders at the pickup point')
        print('7) Show menu again')
        print('8) Exit programm')
        print('-----------------------------')

    
    def show_admin_menu(self):
        print('-----------------------------')
        print('0) Change user')
        print('1) Show catalog')
        print('2) Add product to catalog')
        print('3) Remove product from catalog')
        print('4) Add category to catalog')
        print('5) Remove category from catalog')
        print('6) Show orders at the pickup point')
        print('7) Create pickup point')
        print('8) Show menu again')
        print('9) Exit programm')
        print('-----------------------------')


    def change_user(self):
        self.user = None
        self.work_start()

    def action_select_admin(self):
        action_num = int(input('Select an action from the menu: '))
        
        match action_num:
            case 0:
                self.change_user()
            case 1:
                self.Marketplace.product_shop.catalog.display(0)
            case 2:
                self.Marketplace.add_product_to_catalog()
            case 3:
                self.Marketplace.remove_product_from_catalog()
            case 4:
                self.Marketplace.add_category_to_catalog()
            case 5:
                self.Marketplace.remove_category_from_catalog()
            case 6:
                self.Marketplace.show_orders_at_the_pickup_point()
            case 7:
                self.Marketplace.create_pickup_point()
            case 8:
                self.show_admin_menu()
            case 8:
                sys.exit()
            case _:
                os.system('cls')
                print('Unknown command')
                self.show_admin_menu()
                
    def action_select_customer(self):
        action_num = int(input('Select an action from the menu: '))
        
        match action_num:
            case 0:
                self.change_user()
            case 1:
                self.Marketplace.product_shop.catalog.display(0)
            case 2:
                self.Marketplace.add_to_cart()
            case 3:
                self.Marketplace.edit_cart()
            case 4:
                self.Marketplace.show_cart()
            case 5:
                self.Marketplace.place_order()
            case 6:
                self.Marketplace.show_orders_at_the_pickup_point()
            case 7:
                self.show_customer_menu()
            case 8:
                sys.exit()
            case _:
                os.system('cls')
                print('Unknown command')
                self.show_customer_menu()

    
    def show_menu(self, user):
        match user:
            case 'Admin':
                self.show_admin_menu()
            case 'Customer':
                self.show_customer_menu()

    
    def work_start(self):
        while self.user == None:
            self.log_in()

        self.show_menu(self.user)

        while True:
            if self.user == 'Admin':
                self.action_select_admin()
            else:
                self.action_select_customer()