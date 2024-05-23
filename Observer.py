from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, *args) -> None:
        pass

#склад
class Observable(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.observers = []     # инициализация списка наблюдателей

    def register(self, observer: Observer) -> None:
        """
        Регистрация нового наблюдателя на подписку
        """
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        pass
