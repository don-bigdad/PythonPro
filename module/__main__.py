from student import Student
from group import Group



some=[Student(f'Ivanov{i}',f'Ivan',f'somemail{i}@gmail.com').__str__() for i in range(1,15)]
if __name__=="__main__":
    gr1=Group()
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
    print(gr1)