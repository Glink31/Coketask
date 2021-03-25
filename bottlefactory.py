from abc import ABCMeta, abstractmethod
class BottleFactory(metaclass=ABCMeta):
    def __init__(self,bottle,drink,cap,label):
        self.bottle = bottle
        self.drink = drink
        self.cap = cap
        self.label = label
    def takebottle(self,bottle):
        print(f"Взяли пустую бутылку {self.bottle.brand}")
    def fillbottle(self,drink):
        self.bottle.fill(drink)
    def closebottle(self,cap):
        self.bottle.close(cap)
    def applylabelonbottle(self,label):
        self.bottle.applylabel(label)
