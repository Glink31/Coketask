from abc import ABCMeta, abstractmethod
class Label(metaclass=ABCMeta):
    def __init__(self,brand):
        self.brand = brand
    