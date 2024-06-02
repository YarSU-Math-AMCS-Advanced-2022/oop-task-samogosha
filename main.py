from Marketplace.Marketplace import MarketplaceFacade
from Menu import Menu


def main(): 
    Marketplace = MarketplaceFacade()
    menu = Menu(Marketplace)
    menu.work_start()


if __name__ == '__main__':
    main()