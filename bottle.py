from abc import ABCMeta
class Bottle(metaclass=ABCMeta):
    def __init__(self,brand):
        self.brand = brand
        self.cap = None
        self.drink = None
        self.label = None
    def close(self,cap):
        if self.cap is None: 
            self.cap = cap
            print(f"закрыли бутылку {self.brand} крышкой {cap.brand}")
    def fill(self,drink):
        if self.cap is None:
            if self.drink is None:
                self.drink = drink
                print(f"залили {drink.brand} в бутылку {self.brand}")
        else:
            print("нельзя залить напиток, потому что бутылка закрыта")          
    def applylabel(self,label):
        if self.label is None:
            self.label = label
            print(f"наклеили этикетку {label.brand} на бутылку {self.brand}")