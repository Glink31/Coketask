from drink import Drink
class PepsiDrink(Drink):
    def __init__(self):
        super().__init__("Pepsi")
    def copy(self):
        return PepsiDrink()