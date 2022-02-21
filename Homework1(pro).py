# Создайте пользовательский класс для описания товара
# (предположим, это задел для интернет-магазина). В качестве
# полей товара можете использовать значение цены, описание,
# габариты товара. Создайте пару экземпляров вашего класса и
# протестируйте их работу.
class Product:
    def __init__(self,manufacturer,model,price):
        self.manufacturer=manufacturer
        self.model=model
        self.price=price
    def __str__(self):
        return f'{self.manufacturer} {self.model} {self.price}'
product1=Product("Apple","Iphone12",27.499)
product2=Product("OnePlus","OnePlus 9 pro",25.999)
product3=Product("Samsung","Samsung S21",22.999)

print(product1,product2,product3,sep="\n")
# Создайте класс «Покупатель». В качестве полей можете
# использовать фамилию, имя, отчество, мобильный телефон и т. д
class Buyer:
    def __init__(self,name,surname,mail):
        self.name=name
        self.surname=surname
        self.mail=mail

    def __str__(self):
        return f'{self.name} {self.surname} {self.mail}'
buyer1=Buyer("Ivan","Ivanov","somemail1.@gmail.com")
buyer2=Buyer("Petr","Petrov","somemail2.@gmail.com")

print(buyer1,buyer2,sep="\n")
# Создайте класс «Заказ». Заказ может содержать несколько
# товаров. Заказ должен содержать данные о пользователе, который
# его осуществил. Реализуйте метод вычисления суммарной
# стоимости заказа. Определите метод __str__() для корректного
# вывода информации о этом заказе
class Order:
    def __init__(self,name,surname,mail):
        self.name=name
        self.surname=surname
        self.mail=mail

    def fullprice(self,product1,product2):
        summ = {}
        suma=0
        product1[1] = int(product1[1])
        product2[1] = int(product2[1])
        summ["price1"] = product1[1]
        summ["price2"] = product2[1]
        for element in summ:
            suma += summ[element]
        return suma
    def __str__(self):
        return f'Заказчик:{self.name} {self.surname} {self.mail}\n' \
               f'заказ:{product1[0]} {product2[0]} на сумму {self.fullprice(product1,product2)}\n'

persona1=Order("ivan","ivanov","someivan.@gmailcom")
product1="cheese,70".split(",")
product2="pizza,250".split(",")
print(persona1)