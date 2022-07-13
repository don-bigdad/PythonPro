import datetime


table={}
new_day={}

with open("C:/Users/Admin/OneDrive/Рабочий стол/total.txt","r",encoding="UTF-8") as f:
    for elem in f.readlines()[:1]:
        for item in elem.split():
            table[item.split(":")[0]]=int(item.split(":")[1])

with open("C:/Users/Admin/OneDrive/Рабочий стол/total.txt", "r", encoding="UTF-8") as f:
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
    with open("C:/Users/Admin/OneDrive/Рабочий стол/total.txt", "r+", encoding="UTF-8") as f:
        for name, value in table.items():
            f.write(f'{name}:{value} ')
    with open("C:/Users/Admin/OneDrive/Рабочий стол/total.txt", "r+", encoding="UTF-8") as f:
        f.write("\n")
        for elem in f.readlines()[-1:]:
            del elem
            for name,value in new_day.items():
                f.write(f'{name}:{value} ')


def new():
    with open("C:/Users/Admin/OneDrive/Рабочий стол/total.txt","a",encoding="UTF-8") as f:
        f.write(f'\n----------{datetime.date.today()}-----------\n')
        for name,value in new_day.items():
            f.write(f'{name}:{0} ')