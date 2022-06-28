class Zerro(Exception):
    def __str__(self):
        return f'Price can`t be less then 0,Change value of price'

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} {self.price}'

try:
    product1 = Product("Apple",int(input("Input price:")))
except ValueError:
    print("Value must be int or float")
if product1.price<0:
    raise Zerro


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
print(gr1.append_student(some[0]))
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
