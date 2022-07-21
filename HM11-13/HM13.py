from abc import ABC, abstractmethod


class Abstract(ABC):

    @abstractmethod
    def simple_number(self, number):
        pass


class SimpleNumber(Abstract):

    def simple_number(self,number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

x=SimpleNumber()
print(x.simple_number(13))


###
class AnotherNumber:
    def __init__(self, number):
        self.number = number

    def simple_number(self, number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

Abstract.register(AnotherNumber)


x = AnotherNumber(12)
print(isinstance(x, Abstract))
