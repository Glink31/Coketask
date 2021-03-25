from abc import ABCMeta, abstractmethod
class Bottle(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,brand):
        self.brand = brand
        self.closed = False
        self.filled = False
        self.labeled = False
    @abstractmethod
    def close(self):
        if not self.closed: 
            self.closed = True
    @abstractmethod
    def fill(self):
        if not self.closed:
            if not self.filled:
                self.filled = True
    @abstractmethod
    def applylabel(self):
        if not self.labeled:
            self.labeled = True