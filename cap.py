from abc import ABCMeta, abstractmethod
class Cap(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,brand):
        self.brand = brand