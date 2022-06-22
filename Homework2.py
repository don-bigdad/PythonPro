
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
            self.group.append(student)
        else:
            return None
    def remove_student(self,student:Student):
        self.group.remove(student)
    def search_by_surname(self,surname):
        for student in self.group:
            if student.surname==surname:
                return student

    def __str__(self): 
        n="\n"
        return f'{n.join(map(str,self.group))}'

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
gr_1.remove_student(student3)
print(gr_1.search_by_surname("Ivanov4"))