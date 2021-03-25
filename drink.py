from abc import ABCMeta, abstractmethod
class Drink(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,brand):
        self.brand = brand