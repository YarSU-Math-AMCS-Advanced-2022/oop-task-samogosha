from Product import Product
from Catalog import Product_Catalog 
from Shop import Product_Shop
from Store import Store
from Cart import Cart
from Order import Order
from Marketplace import MarketplaceFacade
from PickUpPoint import PickUpPoint
from Menu import Menu

def main(): 
    Marketplace = MarketplaceFacade()
    menu = Menu(Marketplace)
    menu.work_start()

if __name__ == '__main__':
    main()