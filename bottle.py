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
            print(f"закрыли бутылку {self.brand} крышкой {cap.brand}")
    @abstractmethod
    def fill(self,drink):
        if self.cap is None:
            if self.drink is None:
                self.drink = drink
                print(f"залили {drink.brand} в бутылку {self.brand}")
        else:
            print("нельзя залить напиток, потому что бутылка закрыта")     
    @abstractmethod
    def applylabel(self,label):
        if self.label is None:
            self.label = label
            print(f"наклеили этикетку {label.brand} на бутылку {self.brand}")