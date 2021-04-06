from abc import ABCMeta, abstractmethod
class Drink(metaclass=ABCMeta):
    def __init__(self,brand):
        self.brand = brand