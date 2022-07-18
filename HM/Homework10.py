#1
class_list=[]
def class_register(cls):
    class_list.append(cls)
    return cls

@class_register
class One:
    pass
@class_register
class Two:
    pass
@class_register
class Three:
    pass
@class_register
class Four:
    pass
# print(class_list)
#2
def parametr(string):
    def str_to_class(cls):
        def final_str():
            return string+cls().__str__()
        return final_str
    return str_to_class

@parametr("`appended text` ")
class Five:
    def __str__(self):
        return "five from class Five"
# x=Five()
# print(x)
#3
class Box:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    @staticmethod
    def volume(box1,box2):
        return box1.x*box1.y*box1.z+box2.x*box2.y*box2.z

box_1=Box(2,2,3)
box_2=Box(3,3,2)
print(Box.volume(box_1,box_2))