from drink import Drink
class ColaDrink(Drink):
    def __init__(self):
        super().__init__("Coca-Cola")
    def copy(self):
        return ColaDrink()