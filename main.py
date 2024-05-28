from Product import Product
from Catalog import Product_Catalog 
from Shop import Product_Shop
from Store import Store
from Cart import Cart
from Order import Order
from Marketplace import MarketplaceFacade

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

    root = Product_Catalog('Root')

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
    shop.add_product_to_catalog('T-shirts', tshirt_anapa)
    
    #list_of_products = [Product('Майка_Анапа_2007', 3, 100, '', 1, 'Та самая))')]
    store = Store(list())
    store.add_product(tshirt_anapa)
    store.add_product(accessories_chain)
    store.add_product(accessories_chain2)
    store.add_product(tshirt_blkc)
    
    cart = Cart()
    order = Order()
    
    facade = MarketplaceFacade(shop, store, cart, order)
    
    #facade.place_order()
    facade.product_shop.catalog.display(0)
    facade.remove_category_from_marketplace()
    facade.product_shop.catalog.display(0)
    #print(facade.order.destination)

    # shop.add_category_to_catalog('root', 'T-shirts')
    # shop.add_product_to_catalog('T-shirts', tshirt_anapa)

    # shop.catalog.display(0)
    
    
    
    
    

    # while True:

    #     print('Выберите действие:')
    #     print('1) Добавить товар в каталог')
    #     print('2) Добавить категорию в каталог')
    #     print('3) Вывести каталог')
    #     print('4) Закрыть программу')

    #     choice = int(input())

    #     match choice:
    #         case 1:
    #             print('Выберите категорию для добавления')
    #             category = input()
    #             print('')
    #         case 2:
    #         case 3:
    #         case 4:


    # root = Product_Catalog('Root')

    # list_of_products = [Product('Майка_Анапа_2007', 3, 100, '', 1, 'Та самая))')]
    # store = Store(list_of_products)

    # leaf_tshirt_anapa = Product_Catalog('TShirt_Anapa', Product('Майка_Анапа_2007', 3, 100, '', 1, 'Та самая))'))
    # root.add(leaf_tshirt_anapa)

    # store.register(shop)

    # store.change_product(list_of_products[0], -2)
    # print(leaf_tshirt_anapa.product.stock_quantity)


    '''
    store = Store(list())
    store.add_product(tshirt_anapa)
    store.add_product(accessories_chain)
    store.add_product(accessories_chain2)
    store.add_product(tshirt_blkc)

    cart = Cart()
    cart.add_to_cart('Майка_Анапа_2007', 1)
    cart.add_to_cart('Цепочка_Вин_Дозатор', 2)
    cart.add_to_cart('Цепочка_Вин_Дозатор_2', 10)

    order = Order('Заказ1', 5, 'Крамсякин', 'Br', cart, store)
    order.complete_order()

    print(order.user_cart.cart_dictionary)    
    '''
    
    
    # hash()

if __name__ == '__main__':
    main()
