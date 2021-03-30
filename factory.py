from abc import ABCMeta,abstractmethod
class DrinkFactoty(metaclass=ABCMeta):
    @abstractmethod
    def createbottle(self):
        pass
    @abstractmethod
    def createdrink(self):
        pass
    @abstractmethod
    def createcap(self):
        pass
    @abstractmethod
    def createlabel(self):
        pass