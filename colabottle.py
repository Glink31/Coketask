from bottle import Bottle
class ColaBottle(Bottle):
    def __init__(self):
        super().__init__("Coca-Cola")
    def close(self,cap):
        super().close(cap)
    def fill(self,drink):
        super().fill(drink)
    def applylabel(self,label):
        super().applylabel(label)
    def copy(self):
        CopyBottle = ColaBottle()
        if self.label is not None:
            CopyBottle.label = self.label.copy()
        if self.cap is not None:
            CopyBottle.cap = self.cap.copy()
        if self.drink is not None:
            CopyBottle.drink = self.drink.copy()
        return CopyBottle
    