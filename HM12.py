class Meta(type):
    def __new__(cls, *args):
        fields=[]
        for elem in args[2:]:
            for item in elem:
                fields.append(item)
        with open("Metaclass.txt","a") as file:
            file.write(f'Сreating new class!-{list(args)[0]}. Fields {fields}\n')
        return type.__new__(cls,*args)

class Human(metaclass=Meta):
    def __init__(self,gender,name,surname):
        self.gender=gender
        self.name=name
        self.surname=surname

    def __str__(self):
        return f'{self.surname}{self.name[0]}-{self.gender}'

class Triange(metaclass=Meta):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return f'{self.a}{self.b}-{self.c}'