class Rectangle:

    def __init__(self,width,height):
        if  type(width)!=(int or float) and type(height)!=(int or float) :
            raise ValueError
        self.width=width
        self.height=height

    def square(self):
        return self.width*self.height

    def __gt__(self, other):
        return self.width*self.height>other.width*other.height

    def __mul__(self, other):
        if isinstance(other,(int or float)):
            return self.square()*other
        raise ValueError
    def __add__(self, other):
        return Rectangle(self.width+other.width,self.height+other.height)
    def __iadd__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f'Your rectangle have height {self.height},width {self.width} and square of this rectanlge {self.square()}'


rect1=Rectangle(12,8)
rect2=Rectangle(12,4)
new_rect1=rect1*3
rect3=Rectangle(12,6)
rect3+=rect2+rect1
print(rect1>rect2,new_rect1,rect3)
