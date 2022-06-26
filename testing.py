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
#########
text="Lorem ipsum dolor sit amet consectetur adipisicing elit. \n" \
       "Officia, aperiam ipsa quo non. Tempore facere deleniti cupiditate quis aliquid quasi aut maiores laudantium!\n" \
       "Consequuntur cupiditate ea animi, quia praesentium voluptatem?"
with open("C:/Users\Admin/PythonStart/text.txt","w") as f:
    f.write(text)

class Redactor:

    def __init__(self,file):
        self.file=file

    def words_count(self):
        with open("C:/Users\Admin/PythonStart/text.txt", "r") as file:
            return len(file.read().split())

    def sentence_count(self):
        with open("C:/Users\Admin/PythonStart/text.txt", "r") as file:
            return file.read().count(".")

    def characters_count(self):
        with open("C:/Users\Admin/PythonStart/text.txt", "r") as file:
            return len(file.read())
    def symbols_count(self):
        count=0
        with open("C:/Users\Admin/PythonStart/text.txt", "r") as file:
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
