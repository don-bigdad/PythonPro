class Order:
    def __init__(self, buyer: Buyer):
        self.buyer = buyer
        self.product=[]
        self.summ=0
    def summa(self,product,count):
        self.summ+=product.price*count
        return self.summ
    def __str__(self):
       return  f'Buyer {self.buyer} , total {self.summ} '

order_1=Order(buyer1)
print(order_1)
order_1.summa(product3,2)
order_1.summa(product4,4)
print(order_1)
