from bottle import Bottle
class PepsiBottle(Bottle):
    def __init__(self,):
        super().__init__("Pepsi")
    def close(self,cap):
        super().close(cap)
    def fill(self,drink):
        super().fill(drink)
    def applylabel(self,label):
        super().applylabel(label)
    def copy(self):
        CopyBottle = PepsiBottle()
        CopyBottle.label = self.label.copy()
        CopyBottle.cap = self.cap.copy()
        CopyBottle.drink = self.drink.copy()
        return CopyBottle
    