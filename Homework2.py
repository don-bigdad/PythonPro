
class Person:
    def __init__(self,surname:str,name:str):
        self.surname=surname
        self.name=name
    def __str__(self):
        return f'{self.surname} {self.name}'
class Student(Person):
    def __init__(self,surname:str,name:str,age:int,number:str):
        super().__init__(surname,name)
        self.age=age
        self.number=number
    def __str__(self):
        return f'{super().__str__()} {self.age} {self.number}'
person1=Person("Ivanov1","Ivan")

student1=Student("Ivanov1","Ivan",18,"123456789")
student2=Student("Ivanov2","Ivan",18,"123456789")
student3=Student("Ivanov3","Ivan",18,"123456789")
student4=Student("Ivanov4","Ivan",18,"123456789")
student5=Student("Ivanov5","Ivan",18,"123456789")
student6=Student("Ivanov6","Ivan",18,"123456789")
student7=Student("Ivanov7","Ivan",18,"123456789")
student8=Student("Ivanov8","Ivan",18,"123456789")
student9=Student("Ivanov9","Ivan",18,"123456789")
student10=Student("Ivanov10","Ivan",18,"123456789")
student11=Student("Ivanov11","Ivan",18,"123456789")

class Group:
    group=[]
    def add_student(self,student:Student):
        if len(self.group)<10:
            self.group.append(student.surname+" "+student.name)
        else:
            return "Group is full"
    def remove_student(self,student:Student):
        for element in self.group:
            if element.split()[0]==student.surname:
                self.group.remove(element)
    def search_by_surname(self,student:Student):
        for elem in self.group:
            if elem.split()[0]==student.surname:
                print(elem + " in group")

    def __str__(self):
        return f'{self.group}' # Чтобы без принта работало,но не знаю какой аргумент передавать в скобки {self.search_by_surname(????)}
gr_1=Group()
gr_1.add_student(student1)
gr_1.add_student(student2)
gr_1.add_student(student3)
gr_1.add_student(student4)
gr_1.add_student(student5)
gr_1.add_student(student6)
gr_1.add_student(student7)
gr_1.add_student(student8)
gr_1.add_student(student9)
gr_1.add_student(student10)
gr_1.add_student(student11)
gr_1.remove_student(student1)
gr_1.remove_student(student2)
gr_1.search_by_surname(student4)
print(gr_1)
