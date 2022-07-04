class Zerro(Exception):
    def __str__(self):
        return f'Check the value of price,probably uncorrect value'


class Product:
    def __init__(self, price, name):
        if not isinstance(price, int | float):
            raise ValueError
        if price <= 0:
            raise Zerro
        self.price = price
        self.name = name

    def __mul__(self, other):
        if isinstance(other, int):
            return Product(self.price * other, self.name)

    def __str__(self):
        return f'{self.name},{self.price}'


class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.number}'


person1 = Person("Ivan", "Ivanov", "123456789")
person2 = Person("Petr", "Petrov", "987654321")
product1 = Product(20, "Apple")
product2 = Product(30, "Banana")
product3 = Product(35, "Cherry")


class Order:

    def __init__(self, person: Person):
        self.person = person
        self.quantyties = {}

    def append(self, product: Product, count):
        if product.name in self.quantyties:
            self.quantyties[product.name] = self.quantyties[product.name] + count * product.price
        else:
            self.quantyties[product.name] = count * product.price
        return self.quantyties

    def __add__(self, other):
        if other.name in self.quantyties:
            self.quantyties[other.name] = self.quantyties[other.name] + other.price
            return self
        else:
            self.quantyties[other.name] = other.price
            return self

    def __isub__(self, other):
        if self.quantyties[other.name]<=0:
            raise Zerro
        if other.name in self.quantyties:
            self.quantyties[other.name] = self.quantyties[other.name] - other.price
            return self
        raise KeyError


    def to_pay(self):
        sum = 0
        for elem in self.quantyties:
            sum += self.quantyties[elem]
        return sum

    def __str__(self):
        return f'Person {self.person} ordered {self.quantyties}.Total price:{self.to_pay()}'

order1 = Order(person1)
order2 = Order(person2)
order1.append(product2, 3)
order1 += product3
order2 += product1 * 2
order2-=product1
order2-=product1
order2-=product1



print(order1, order2, sep="\n")
