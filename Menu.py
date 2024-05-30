from Marketplace import MarketplaceFacade
import sys


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
        print('0) Change user')
        print('1) Show catalog')
        print('2) Add product to cart')
        print('3) Edit cart')
        print('4) Show cart')
        print('5) Place an order')
        print('6) Show menu again')
        print('7) Exit programm')

    
    def show_admin_menu(self):
        print('0) Change user')
        print('1) Show catalog')
        print('2) Add product to catalog')
        print('3) Remove product from catalog')
        print('4) Add category to catalog')
        print('5) Remove category from catalog')
        print('6) Show menu again')
        print('7) Exit programm')


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
                self.show_admin_menu()
            case 7:
                sys.exit()
            case _:
                print('Unknown command')
                
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
                self.show_customer_menu()
            case 7:
                sys.exit()
            case _:
                print('Unknown command')

    
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