
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
quantyties={}
class Order:
    def __init__(self,person:Person,product:Product):
        self.person=person
        self.product=product
    def append(self,product_name,count):
        quantyties[product_name]=count
        return quantyties
    def to_pay(self):
        sum=0
        for element in quantyties:
            for item in product_list:
                if item[0]==element:
                    sum+=quantyties[element]*item[1]
        return sum
    def __str__(self):
        return f'Person {self.person} has order {" and ".join([elem for elem in quantyties])}.Total price:{self.to_pay()}'
order1=Order(person1,product1)
order1.append("cherry",3)
order1.append("Apple",5)
print(order1)
