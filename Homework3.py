class MyException(Exception):
    def __init__(self,count):
        self.count=count
    def error(self):
         return  "Must take int or float,but find string" if type(self.count)==str else "Check the variables,price or count less than zero"

    def __str__(self):
        return self.error()


class Person:
    def __init__(self, surname: str, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name}.Phone {self.phone}'


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} {self.price}'


class Order:
    def __init__(self, person: Person):
        self.person = person
        self.order = {}
    def product_with_price(self,price:int|float):
        try:
            price=int(price)
        except ValueError:
            return "Value of price must be integer of float"
        prod_with_price=[elem.name for elem in dict_prod if elem.price==price]
        return f'All product with price {price}.\n{",".join([elem for elem in prod_with_price])}'\
            if prod_with_price else -1
    def append_prod(self, product, count: int | float):
        if not type(count) == int or count <= 0 or product.price <= 0:
            raise MyException(count)
        if product.name in self.order:
            self.order[product.name] = self.order[product.name] + product.price * count
        else:
            self.order[product.name] = product.price * count

    def sum(self):
        total=sum({self.order[elem] for elem in self.order})
        return total

    def __str__(self):
        return f'{self.person} \nOrdered {" and ".join(elem for elem in self.order)}.\nTotal to pay {self.sum()}'


pers1 = Person("Ivanov", "Ivan", "12345689")
prod1 = Product("Cherry", 15)
prod4=Product("Green Apple", 15)
prod5=Product("Orange",27)
prod2 = Product("Apple", -25)
prod3 = Product("Banana", 27)
ord1 = Order(pers1)

try:
    ord1.append_prod(prod2,"asd")
except MyException:
    if prod2.price < 0:
        prod2.price=abs(prod2.price)
    ord1.append_prod(prod2, 1)
print(ord1)
dict_prod={prod1,prod2,prod3,prod4}
print(ord1.product_with_price(input("Input number of price=")))
#####################################################

class GroupException(Exception):
    def __init__(self):
        self.message="This group can have a maximum of 10 people."
    def __str__(self):
        return self.message

class Person:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def __str__(self):
        return f'{self.surname} {self.name}'
class Student(Person):
    def __init__(self,name,surname,mail):
        super().__init__(surname,name)
        self.mail=mail
    def __str__(self):
        return f'{self.surname} {self.name[0]} {self.mail}'

some=[Student(f'Ivanov{i}',f'Ivan',f'somemail{i}@gmail.com').__str__() for i in range(1,15)]

class Group():
    student_list=[]
    def append_student(self,student):
        if len(self.student_list)>10:
            raise GroupException
        self.student_list.append(student)
        return f'Student appended,your list now,{self.student_list}'
    def remove_from_list(self,student):
        self.student_list.remove(student)
    def find_for_surname(self,surname):
        same_surname=[]
        for elem in self.student_list:
            if elem.split()[0]==surname:
                same_surname.append(elem)
        return f'Find some: {same_surname}' if same_surname else None
    def __str__(self):
        n="\n"
        return f'{n.join(self.student_list)}'


gr1 = Group()
gr1.append_student(some[0])
gr1.append_student(some[1])
gr1.append_student(some[2])
gr1.append_student(some[3])
gr1.append_student(some[4])
gr1.append_student(some[5])
gr1.append_student(some[6])
gr1.append_student(some[7])
gr1.append_student(some[8])
gr1.append_student(some[9])
gr1.append_student(some[9])
try:
    gr1.append_student(some[10])
except GroupException:
    gr1.remove_from_list(some[9])
    gr1.append_student(some[10])
print(gr1)
