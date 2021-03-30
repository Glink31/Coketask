from bottle import Bottle
class ColaBottle(Bottle):
    def __init__(self):
        super().__init__("Coca-Cola")
    def close(self):
        super.close()
    def fill(self):
        super.fill()
    def applylabel(self):
        super.applylabel()
    