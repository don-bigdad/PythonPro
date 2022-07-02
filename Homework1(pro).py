class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def __str__(self):
        return f'{self.name},{self.price}'


class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def __str__(self):
        return f'{self.name} {self.surname} {self.number}'


person1 = Person("Ivan", "Ivanov", "123456789")
person2 = Person("Ivan", "Ivanov", "123456789")
product1 = Product(20, "Apple")
product2 = Product(30, "banana")
product3 = Product(35, "cherry")


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

    def to_pay(self):
        sum = 0
        for elem in self.quantyties:
            sum += self.quantyties[elem]
        return sum

    def __str__(self):
        return f'Person {self.person} ordered {self.quantyties}.Total price:{self.to_pay()}'


order1 = Order(person1)
order1.append(product1, 5)
order1.append(product1, 2)
order1.append(product2, 3)
print(order1)
