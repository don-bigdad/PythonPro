import datetime
import os
#This code for domino game to save all results of the game
#At the first line total score
#This code have two functions :
#new()Which create a new day to more detail score cheked and who has more wins exactly at this day
#sum() function which calculate score,they calculate total score(exactly first line of .txt file) and last line :)
table={}
new_day={}
if not os.path.isfile("test.txt"):
    with open("test.txt","w",encoding="UTF-8") as f:
        f.write("Олег:0 Сергей:0 Богдан:0")
        f.write(f'\n----------{datetime.date.today()}-----------\n')
        f.write("Олег:0 Сергей:0 Богдан:0")
        f.write("\n")


with open("test.txt","r",encoding="UTF-8") as f:
    for elem in f.readlines()[:1]:
        for item in elem.split():
            table[item.split(":")[0]]=int(item.split(":")[1])

with open("test.txt", "r", encoding="UTF-8") as f:
    for elem in f.readlines()[-1:]:
        for item in elem.split():
            new_day[item.split(":")[0]]=int(item.split(":")[1])

def sum():
    enter=int(input("Кто Выиграл? Олег-1,Сергей-2,Богдан-3:"))
    if enter==1:
        new_day['Сергей'] += 1
        new_day['Богдан'] += 1
        table['Сергей'] += 1
        table['Богдан'] += 1
    elif enter==2:
        new_day['Олег'] += 1
        new_day['Богдан'] += 1
        table['Олег'] += 1
        table['Богдан'] += 1
    else:
        new_day['Олег'] += 1
        new_day['Сергей'] += 1
        table['Олег'] += 1
        table['Сергей'] += 1

    with open("test.txt", "r+", encoding="UTF-8") as f:
        for name, value in table.items():
            f.write(f'{name}:{value} ')
        f.write("\n")
    with open("test.txt", "r+", encoding="UTF-8") as f:
        f.write("\n")
        for elem in f.readlines()[-1:]:
            for name, value in new_day.items():
                f.write(f'{name}:{value} ')

def new():
    with open("test.txt","a",encoding="UTF-8") as f:
        f.write(f'\n----------{datetime.date.today()}-----------\n')
        for name,value in new_day.items():
            f.write(f'{name}:{0} ')
