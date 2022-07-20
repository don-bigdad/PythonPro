#1
class MyDescript:
    def __init__(self,another_side):
     self.another_side=another_side

    def __get__(self, instance, owner):
        return self.another_side

    def __set__(self, instance, owner):
        raise ValueError("Only for read")

    def __delete__(self):
        raise ValueError("Only for read")


class Square:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f'{self.a}X{self.b}'

    third_side=MyDescript(10)
    fourth_side=MyDescript(20)
# sq_1=Square(10,10)
# print(sq_1.third_side)
# print(sq_1.fourth_side)
# # sq_1.fourth_side=20
#2
class Box:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __setattr__(self, key, value):
        if type(value)!=int:
            raise ValueError
        self.__dict__[key] = value


    def __str__(self):
        return f'{self.a}X{self.b}X{self.c}'


# box_1=Box(1,2,3)
# box_1.a=4
# box_1.c="abc"
# print(box_1)

#3
import datetime
class Triangle:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def __setattr__(self, key, value):
        self.__dict__[key]=value
        with open("ChangedAttribute.txt","a") as file:
            file.write(f'{datetime.datetime.now()}.New attribute:{value} \n')


    def __str__(self):
        return f'{self.__a}X{self.__b}X{self.__c}'


tr_1=Triangle(1,2,3)

tr_1.a=14
tr_1.b=13
print(tr_1)
