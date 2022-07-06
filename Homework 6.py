class GroupException(Exception):
    def __init__(self):
        self.message = "This group can have a maximum of 10 people."

    def __str__(self):
        return self.message


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name}'


class Student(Person):
    def __init__(self, name, surname, mail):
        super().__init__(surname, name)
        self.mail = mail

    def __str__(self):
        return f'{self.surname} {self.name[0]} {self.mail}'


some = [Student(f'Ivanov{i}', f'Ivan', f'somemail{i}@gmail.com').__str__() for i in range(1, 15)]
STUDENT_COUNT = 10


class Group():
    student_list = []

    def append_student(self, student):
        if len(self.student_list) == STUDENT_COUNT:
            raise GroupException
        self.student_list.append(student)
        return f'Student appended,your list now,{self.student_list}'

    def remove_from_list(self, student):
        self.student_list.remove(student)

    def find_for_surname(self, surname):
        same_surname = []
        for elem in self.student_list:
            if elem.split()[0] == surname:
                same_surname.append(elem)
        return f'Find some: {same_surname}' if same_surname else None

    def __iadd__(self, other):
        if len(self.student_list) == STUDENT_COUNT:
            raise GroupException
        self.student_list.append(other)
        return self

    def __isub__(self, other):
        if other in self.student_list:
            self.student_list.remove(other)
        return self

    def __str__(self):
        n = "\n"
        return f'{n.join(self.student_list)}'

    def __iter__(self):
        return GroupIteration(self.student_list)

class GroupIteration:

    def __init__(self,group_list):
        self.group_list=group_list
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.group_list):
            self.index+=1
            return self.group_list[self.index-1]

        raise StopIteration


# gr1 = Group()
#
# gr1.append_student(some[1])
# gr1 += some[2]
# gr1 += some[3]
# gr1 += some[4]
# gr1 += some[5]
# gr1 -= some[1]
#
# for elem in gr1:
#     print(elem)
##################################
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
        try:
            self.quantyties[other.name] = self.quantyties[other.name] - other.price
            return self
        except KeyError:
            return f'Can`t found this product'

    def to_pay(self):
        sum = 0
        for elem in self.quantyties:
            sum += self.quantyties[elem]
        return sum

    def __iter__(self):
        return OrderIter(self.quantyties)

    def __len__(self):
        return len(self.quantyties)

    def __getitem__(self, index):
        converted_list = list(self.quantyties.items())
        if index < len(converted_list):
            return converted_list[index]
        raise IndexError

    def __str__(self):
        return f'Person {self.person} ordered {self.quantyties}.Total price:{self.to_pay()}'


class OrderIter:

    def __init__(self, product_dict):
        self.converted_list = list(product_dict.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.converted_list):
            self.index += 1
            return self.converted_list[self.index - 1]
        raise StopIteration


order1 = Order(person1)
order2 = Order(person2)
order1.append(product2, 3)
order1 += product3
order2 += product1 * 2
order1 -= product2
order1 += product1
print(order1, order2, sep="\n")
print(order2[0])

for elem in order1:
    print(elem)

