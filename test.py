#Vector adding

class Vector:
    def __init__(self,vector):
       self.vector=vector

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, index):
        if index<len(self.vector):
            return self.vector[index]
        return IndexError

    def equals(self,vector2):
        for elem in self.vector:
            for item in vector2:
                if item != elem:
                    return False
                break
        return True

    def add(self,vector2):
        new = []
        iter = 0
        if len(self.vector)!=len(vector2):
            raise Exception("Different lenght")
        for elem in vector2:
            try:
               new.append(self.vector[iter]+elem)
               iter += 1
            except TypeError:
                return Vector(new)
            except IndexError:
                return Vector(new)

    def substract(self,vector2):
        new = []
        iter = 0
        for elem in vector2:
            try:
                new.append(self.vector[iter] - elem)
                iter += 1
            except TypeError:
                return Vector(new)
            except IndexError:
                return Vector(new)

    def dot(self,vector2):
        new = []
        iter = 0
        for elem in vector2:
            try:
                new.append(self.vector[iter] * elem)
                iter += 1
            except TypeError:
                return sum(new)**0.5
            except IndexError:
                return sum(new)**0.5


    def norm(self):
        res=1
        for elem in self.vector:
            res+=elem**2
        return res


    def __str__(self):
        return  " ".join(map(str,self.vector))

x=Vector([1,2,3])
y=Vector([3,4,5])

print(x.add(y))
print(x.norm())
print(x.equals(y))