
class Human:
    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}. {self.age}'


student_1 = Human("Ivanov", "Ivan", "Ivanich", 18)
print(student_1)


class Student(Human):
    def __init__(self, surname, name, patronomyc, mail,age):
        super().__init__(surname, name, patronomyc,age)
        self.mail = mail

    def __str__(self):
        return f'ФИО :{self.surname} {self.name} {self.patronymic[0]}. Mail: ' \
               f'{self.mail},age {self.age}'


student1 = Student("Ivanov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student2 = Student("Petrov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student3 = Student("Sergeyev", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student4 = Student("Bogdanov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student5 = Student("Danilov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student6 = Student("Rodionov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
print(student1)

class Group:
    def __init__(self):
        self.list = []
    def add_student(self, student):
        if len(self.list)<5:
            self.list.append(student)
        else:
            print("the group is full")
    def del_student(self, student):
        if len(self.list)>=1:
            self.list.remove(student)
        else:
            print("Group must have at least one student")
    def search_student(self, surname):
        for student in self.list:
            if student.surname ==surname:
                print("Student in list")
            else:
                print("Not found") 
    def __str__(self):
       return f'{self.list}  '  #Не могу отобразить строку,работаю с object
group1=Group()
group1.add_student(student3)
group1.add_student(student2)
print(group1)
group1.del_student(student2)
print(group1)
group1.search_student("some")
