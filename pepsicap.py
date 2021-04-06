from cap import Cap
class PepsiCap(Cap):
    def __init__(self):
        super().__init__("Pepsi")
    def copy(self):
        return PepsiCap()