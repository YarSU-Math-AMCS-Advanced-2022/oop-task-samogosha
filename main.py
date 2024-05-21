from Product import Product
from Catalog import Product_Catalog 
from Shop import Product_Shop

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
                                1,
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

    branch_tshirts = Product_Catalog('TShirts')
    branch_accessories = Product_Catalog('Accessories')

    leaf_tshirt_anapa = Product_Catalog('TShirt_Anapa', tshirt_anapa)
    leaf_tshirt_blck = Product_Catalog('TShirt_Blck', tshirt_blkc)
    leaf_accessories_chain = Product_Catalog('Accessories_Chain', accessories_chain)
    leaf_accessories_chain2 = Product_Catalog('Accessories_Chain2', accessories_chain2)

    branch_tshirts.add(leaf_tshirt_anapa)
    branch_tshirts.add(leaf_tshirt_blck)
    branch_accessories.add(leaf_accessories_chain)
    branch_accessories.add(leaf_accessories_chain2)

    root.add(branch_tshirts)
    root.add(branch_accessories)

    root.display(0)

    branch_accessories.sort_by_price()

    root.display(0)


if __name__ == '__main__':
    main()
