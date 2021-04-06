from bottle import Bottle
class ColaBottle(Bottle):
    def __init__(self):
        super().__init__("Coca-Cola")
    def copy(self):
        CopyBottle = ColaBottle()
        if self.label is not None:
            CopyBottle.label = self.label.copy()
        if self.cap is not None:
            CopyBottle.cap = self.cap.copy()
        if self.drink is not None:
            CopyBottle.drink = self.drink.copy()
        return CopyBottle
    