
class Human:
    def __init__(self, name, surname, patronymic, age):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age

    def __str__(self):
        return f'{self.name} {self.surname[0]}.{self.patronymic[0]}. {self.age}'


student_1 = Human("Ivanov", "Ivan", "Ivanich", 18)
print(student_1)


class Student(Human):
    def __init__(self, surname, name, patronomyc, mail,age):
        super().__init__(surname, name, patronomyc,age)
        self.mail = mail

    def __str__(self):
        return f'ФИО :{self.name} {self.surname} {self.patronymic[0]}. Mail: ' \
               f'{self.mail},age {self.age}'


student1 = Student("Ivanov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student2 = Student("Petrov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student3 = Student("Sergeyev", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student4 = Student("Bogdanov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student5 = Student("Danilov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
student6 = Student("Rodionov", "Ivan", "Ivanich", "somemail1@gmail.com",18)
print(student1)
class Group():
    student_list = []

    def add_student(self, student):
        if len(self.student_list)<5:
            self.student_list.append(student.name)
        else:
            print( 'the group is full')
    def del_student(self, student):
        if len(self.student_list)>2:
            self.student_list.remove(student)
        else:
            print("Group must have at least one student")
    def search_student(self, surname):
        for element in self.student_list:
            if element in self.student_list:
                print("Student in list")
                break
            else:
                print("Not found")
                break
    def __str__(self):
       return f'{self.student_list} '
group1=Group()
group1.add_student(student3)
group1.add_student(student2)
group1.add_student(student5)
group1.add_student(student4)
group1.add_student(student2)
group1.add_student(student1)
group1.search_student(student2.surname)
print(group1)