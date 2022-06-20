
class Product:
    def __init__(self,price,name) -> None:
        self.price=price
        self.name=name
    def __str__(self) -> None:
        return f'{self.name},{self.price}'
class Person:
    def __init__(self,name,surname,number) -> None:
        self.name=name
        self.surname=surname
        self.number=number
    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.number}'
person1=Person("Ivan","Ivanov","123456789")
person2=Person("Ivan","Ivanov","123456789")
product1=Product(20,"Apple")
product2=Product(30,"banana")
product3=Product(35,"cherry")
product_list=[(product1.name,product1.price),(product2.name,product2.price),(product3.name,product3.price)]

class Order:
    
    def __init__(self,person:Person):
        self.person=person
        self.quantyties={}
    def append(self,product_name,count):
        self.quantyties[product_name]=count
        return self.quantyties
    def to_pay(self):
        sum=0
        for element in self.quantyties:
            for item in product_list:
                if item[0]==element:
                    sum+=self.quantyties[element]*item[1]
        return sum
    def __str__(self):
        return f'Person {self.person} ordered {" and ".join([elem for elem in self.quantyties])}.Total price:{self.to_pay()}'
order1=Order(person1)
order1.append("cherry",3)
order1.append("Apple",5)
order1.append("banana",2)
print(order1)
