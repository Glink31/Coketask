from abc import ABCMeta, abstractmethod
class Cap(metaclass=ABCMeta):
    def __init__(self,brand):
        self.brand = brand