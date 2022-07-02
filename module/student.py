from person import Person


class Student(Person):
    def __init__(self,name,surname,mail):
        super().__init__(surname,name)
        self.mail=mail
    def __str__(self):
        return f'{self.surname} {self.name[0]} {self.mail}'

student1=Student("Ivanov1","Ivan","somemail1@gmail.com")
print(student1)