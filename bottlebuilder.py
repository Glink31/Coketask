class BottleBuilder():
    def __init__(self,factory):
        self.bottle = None
        self.factory = factory
    def takebottle(self):
        self.bottle = self.factory.createbottle()
        print(f"Взяли бутылку {self.bottle.brand}")
    def fillbottle(self):
        if self.bottle is not None:
            drink = self.factory.createdrink()
            self.bottle.fill(drink)
    def closebottle(self):
        if self.bottle is not None:
            cap = self.factory.createcap()
            self.bottle.close(cap)
    def applylabelonbottle(self):
        if self.bottle is not None:
            label = self.factory.createlabel()
            self.bottle.applylabel(label)
    def BuildProduct(self):
        Product = self.bottle.copy()
        return Product
