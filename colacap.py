from cap import Cap
class ColaCap(Cap):
    def __init__(self):
        super().__init__("Coca-Cola")
    def copy(self):
        return ColaCap()