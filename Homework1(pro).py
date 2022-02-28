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
product4=Product("Samsung","safety glass",500)
product5=Product("Xiaomi","phone case",300)
product6=Product("Apple","wireless headphones",6000)
Product7=Product("Apple","wireless charging",3000)
# print(product1,product2,product3,sep="\n")
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

# print(buyer1,buyer2,sep="\n")
# Создайте класс «Заказ». Заказ может содержать несколько
# товаров. Заказ должен содержать данные о пользователе, который
# его осуществил. Реализуйте метод вычисления суммарной
# стоимости заказа. Определите метод __str__() для корректного
# вывода информации о этом заказе
class Order:
    def __init__(self, buyer: Buyer):
        self.buyer = buyer
        self.product= []
        self.count = []
    def add_product(self, product:Product, count:int):
        self.product.append(product)
        self.count.append(count)
        return product
    def summ(self):
        summ=0
        for i in range (len(self.product)):
            summ+=self.product[i].price*self.count[i]
        return summ
    def __str__(self):
       return  f' Buyer {self.buyer},total summ {self.summ()}'

order_1=Order(buyer1)
print(order_1)
order_1.add_product(product2,2)
print(order_1)

