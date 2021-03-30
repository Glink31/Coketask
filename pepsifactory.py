from factory import DrinkFactoty
from pepsibottle import PepsiBottle
from pepsidrink import PepsiDrink
from pepsicap import PepsiCap
from pepsilabel import PepsiLabel
class PepsiFactory(DrinkFactoty):
    def createbottle(self):
        b = PepsiBottle()
        return b
    def createcap(self):
        c = PepsiCap()
        return c
    def createlabel(self):
        l = PepsiLabel()
        return l
    def createdrink(self):
        d = PepsiDrink()
        return d