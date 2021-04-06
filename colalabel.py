from label import Label
class ColaLabel(Label):
    def __init__(self):
        super().__init__("Coca-Cola")
    def copy(self):
        return ColaLabel()