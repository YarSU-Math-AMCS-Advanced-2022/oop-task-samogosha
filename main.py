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

    tshirt_anapa = Product('Майка_Анапа_2007', 
                           3,
                           100,
                           '',
                           1,
                           'Та самая))')
    
    accessories_chain = Product('Цепочка_Вин_Дозатор',
                                2,
                                1e8, 
                                '',
                                2,
                                'Оригинал, отвечаю, лично из рук Вин Дизеля брал))')
    
    accessories_chain2 = Product('Цепочка_Вин_Дозатор_2',
                                2,
                                10, 
                                '',
                                1,
                                'НеОригинал, отвечаю, лично из рук Вин Дизеля не брал))')

    tshirt_blkc = Product('Футблока_Чёрная', 
                          1,
                          50,
                          '', 
                          2, 
                          'Классная брат, ещё не помялась')

    # root = Product_Catalog('Root')

    # branch_tshirts = Product_Catalog('TShirts')
    # branch_accessories = Product_Catalog('Accessories')

    # leaf_tshirt_anapa = Product_Catalog('TShirt_Anapa', tshirt_anapa)
    # leaf_tshirt_blck = Product_Catalog('TShirt_Blck', tshirt_blkc)
    # leaf_accessories_chain = Product_Catalog('Accessories_Chain', accessories_chain)
    # leaf_accessories_chain2 = Product_Catalog('Accessories_Chain2', accessories_chain2)

    # branch_tshirts.add(leaf_tshirt_anapa)
    # branch_tshirts.add(leaf_tshirt_blck)
    # branch_accessories.add(leaf_accessories_chain)
    # branch_accessories.add(leaf_accessories_chain2)

    # root.add(branch_tshirts)
    # root.add(branch_accessories)

    # branch_accessories.sort_by_price()
    
    shop = Product_Shop()
    shop.add_category_to_catalog('root', 'T-shirts')
    shop.add_category_to_catalog('root', 'Shtani')
    shop.add_category_to_catalog('Shtani', 'Shorti')
    shop.add_category_to_catalog('Shtani', 'Pantsu')
    shop.add_product_to_catalog('Shorti', tshirt_anapa)
    shop.add_product_to_catalog('Shorti', tshirt_blkc)
    shop.add_product_to_catalog('Pantsu', tshirt_anapa)
    shop.add_product_to_catalog('Shtani', tshirt_anapa)
    shop.add_product_to_catalog('T-shirts', tshirt_anapa)

    store = Store(list())
    store.add_product(tshirt_anapa)
    store.add_product(accessories_chain)
    store.add_product(accessories_chain2)
    store.add_product(tshirt_blkc)

    cart = Cart()
    cart.add_to_cart('Майка_Анапа_2007', 1)
    cart.add_to_cart('Цепочка_Вин_Дозатор', 2)
    cart.add_to_cart('Цепочка_Вин_Дозатор_2', 10)

    pick_up_point = PickUpPoint("Королево 27/5")

    order = Order(5, 'Крамсякин', 'Br', cart, store)
    order.complete_order(pick_up_point)
    order.complete_order(pick_up_point)
    print(order.user_cart.cart_dictionary)    
    
    
    
    # hash()

    Marketplace = MarketplaceFacade(shop, store, cart, order)

    menu = Menu(Marketplace)

    menu.work_start()

if __name__ == '__main__':
    main()