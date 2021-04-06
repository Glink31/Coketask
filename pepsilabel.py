from label import Label
class PepsiLabel(Label):
    def __init__(self):
        super().__init__("Pepsi")
    def copy(self):
        return PepsiLabel()