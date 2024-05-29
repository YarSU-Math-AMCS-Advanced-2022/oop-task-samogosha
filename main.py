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
    shop = Product_Shop()

    shop.add_category_from_file('category_data.txt')
    shop.add_products_from_file('data_of_products.txt')

    store = Store(list()) 

    cart = Cart()
    # cart.add_to_cart('Майка_Анапа_2007', 1)
    # cart.add_to_cart('Цепочка_Вин_Дозатор', 2)
    # cart.add_to_cart('Цепочка_Вин_Дозатор_2', 10)

    # pick_up_point = PickUpPoint("Королево 27/5")

    order = Order()
    # order = Order(5, 'Крамсякин', 'Br', cart, store)
    # order.complete_order(pick_up_point)
    # order.complete_order(pick_up_point)
    # print(order.user_cart.cart_dictionary)    
    

    Marketplace = MarketplaceFacade(shop, store, cart, order)
    Marketplace.add_prod_from_shop_to_store()

    menu = Menu(Marketplace)

    menu.work_start()

if __name__ == '__main__':
    main()