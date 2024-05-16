from Product import Product
from Catalog import Product_Catalog 
from Shop import Product_Shop

def main():
    # Магазин товаров
    # Shop = Shop()
    lst = [Product('Футболка', 
                    1, 500, '', 
                    2, 
                    'Охуенна брат, ещё не помялась'),
            Product('Личный_Кирилл',
                    3,
                    0,
                    '',
                    1,
                    'Общажник, норм типок, готов в банке РАБотать'),
            Product('ЕБАТЬ_МАКСОН',
                    2,
                    1e8, 
                    '',
                    1,
                    'Любитель сортировок удалением')]
    Cat = Product_Catalog(lst)
    Sp = Product_Shop(Cat)
    Sp.sort_by_price()
    Sp.show_catalog()
    '''
    Cat
        
    print()
    print('Стало после сортировки')
    
    Cat.sort_by_price()
    new_x = Cat.get_products_list()
    for i in new_x:
        i.Product_print()
        print()
        '''

if __name__ == '__main__':
    main()