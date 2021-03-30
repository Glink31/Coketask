from factory import DrinkFactoty
from colabottle import ColaBottle
from coladrink import ColaDrink
from colacap import ColaCap
from colalabel import ColaLabel
class ColaFactory(DrinkFactoty):
    def createbottle(self):
        b = ColaBottle()
        return b
    def createcap(self):
        c = ColaCap()
        return c
    def createlabel(self):
        l = ColaLabel()
        return l
    def createdrink(self):
        d = ColaDrink()
        return d