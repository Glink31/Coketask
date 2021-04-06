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
        if self.label is not None:
            CopyBottle.label = self.label.copy()
        if self.cap is not None:
            CopyBottle.cap = self.cap.copy()
        if self.drink is not None:
            CopyBottle.drink = self.drink.copy()
        return CopyBottle
    