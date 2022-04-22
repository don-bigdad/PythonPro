class Student:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
    def __str__(self):
       return f'{self.surname} {self.name}'
student1=Student("Ivanov","ivan")
print(student1)
class group:
    def __init__(self,student:Student):
        self.student=student
        self.list=[]
    def add_student(self, student):
        if len(self.list) < 5:
            self.list.append(student)
        else:
            print("the group is full")
    def find_student(self,student):
        for element in self.list:
            if element==self.student.surname:
                self.list.remove(element)
            else:
                print("Not found")
    def __str__(self):
         return f'{self.student} {self.list}'
group1=group(student1)
group1.add_student(student1)
print(group1)
group1.find_student("Ivanov")
print(group1)

