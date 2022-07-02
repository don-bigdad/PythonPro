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


gr1 = Group()

gr1.append_student(some[1])
gr1 += some[2]
gr1 -= some[1]
print(gr1)