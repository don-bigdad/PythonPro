#piza
import datetime
class Ingredient:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return f'{self.name}:{self.price} UAH'
prod1=Ingredient("mushrooms",25)
prod2=Ingredient("Parmesan",15)
prod3=Ingredient("Tomato",10)
prod4=Ingredient("Special sauce",30)
prod5=Ingredient("Sausages",25)
class Pizza:
    total=[]
    to_pay=0
    pizza_toppings = []
    today=datetime.datetime.today().weekday()
    pizza_day = {0: "Calzone:250", 1: "Pizza al taglio:240", 2: "Pizza fritta:310",
                     3: "Pizza al metro :450", 4: "Pizza Romana:370",
                     5: "Pizza Gourmet:230", 6: "Сhef's pizza:330"}
    def pizza_of_day(self):
        self.total.append(self.pizza_day[self.today])
        return f'The pizza of the day "{self.pizza_day[self.today]}" appended to order'
    def another_pizza(self,input:str):
        for elem in input.split():
            self.total.append(self.pizza_day[int(elem)])
        return "Another pizza appended"
    def ingredient_on_pizza(self,ingredient:Ingredient):
        self.pizza_toppings.append(ingredient.__str__())
        self.to_pay += ingredient.price
    def check(self):
        for elem in self.total:
            self.to_pay += int(elem.split(":")[1])
    def __str__(self):
        return f'You order is "{",".join(self.total)}" with {",".join(self.pizza_toppings)}.\nTotal to pay {self.to_pay}'


# ord1 = Pizza()
# print(ord1.pizza_of_day())
# print(ord1.another_pizza(input("Enter what you want with a space:")))
# ord1.ingredient_on_pizza(prod5)
# ord1.check()
# print(ord1)
######### text redactor
text="Lorem ipsum dolor sit amet consectetur adipisicing elit. \n" \
       "Officia, aperiam ipsa quo non. Tempore facere deleniti cupiditate quis aliquid quasi aut maiores laudantium!\n" \
       "Consequuntur cupiditate ea animi, quia praesentium voluptatem?"
with open("text.txt","w") as f:
    f.write(text)

class Redactor:

    def __init__(self,file):
        self.file=file

    def words_count(self):
        with open("text.txt", "r") as file:
            return len(file.read().split())

    def sentence_count(self):
        with open("text.txt", "r") as file:
            return file.read().count(".")

    def characters_count(self):
        with open("text.txt", "r") as file:
            return len(file.read().replace(" ",""))
    def symbols_count(self):
        count=0
        with open("text.txt", "r") as file:
            symbols=[",","!","@",";",".","№","#","^","&","*"]
            for elem in file.read():
                if elem in symbols:
                    count+=1
        return count


test=Redactor("text.txt")
print(test.symbols_count())
print(test.words_count())
print(test.characters_count())
print(test.sentence_count())
#### ticket Доделать
class Ticket:
    list_of_ticket=[0]
    ivent = datetime.date(2022, 9, 30)
    price=1500
    total = 0
    def to_pay(self,variables):
        if variables == "+" or variables.title() == "Yes":
            self.total = self.price*0.5
        elif self.ivent.day-datetime.date.today().day<10 and self.ivent.month-datetime.date.today().month==0:
            self.total = self.total+(self.total*0.1)
        elif self.ivent.month-datetime.date.today().month>2:
            self.total = self.price*0.6
        else:
            self.total = self.price
        self.list_of_ticket.append(self.total)
        return self.total

    def whats_price(self,ticket_number):
        return f'Ticket with number {ticket_number} have price {self.list_of_ticket[ticket_number]} UAH'

    def print_my_ticket(self,ticket_number):
        return f'Ticket number {ticket_number} : {self.list_of_ticket[ticket_number]} UAH'


tick1 = Ticket()
tick2=Ticket()
print(tick1.to_pay("yes"))
print(tick1.to_pay("-"))

print(tick1.whats_price(2))
print(tick1.print_my_ticket(1))

