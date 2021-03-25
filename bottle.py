from abc import ABCMeta, abstractmethod
class Bottle(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,brand):
        self.brand = brand
        self.cap = None
        self.drink = None
        self.label = None
    @abstractmethod
    def close(self,cap):
        if self.cap is None: 
            self.cap = cap
    @abstractmethod
    def fill(self,drink):
        if self.cap is None:
            if self.drink is None:
                self.drink = drink     
    @abstractmethod
    def applylabel(self,label):
        if self.label is None:
            self.label = label