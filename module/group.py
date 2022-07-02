from settings import STUDENT_COUNT
from student import Student
from exeption import GroupException

class Group():
    student_list=[]
    def append_student(self,student:Student):
        if len(self.student_list) == STUDENT_COUNT:
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
