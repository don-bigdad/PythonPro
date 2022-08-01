import re

# valid card number function
def valid_card(card_number):
    pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    check1 = re.search(pattern, my_card)
    return card_number if check1 else 'Invalid card number'
my_card = "1233-5213-9990-7622"
print(valid_card(my_card))
# Напишите регулярное выражение, которое будет находить в тексте фрагменты,
# состоящие из одной буквы R, за которой следует одна или более букв b,
# за которой одна r. Учитывать верхний и нижний регистр.
in_string = r'\w[Rb+r]'
my_string = "asdRbbbbrlsk"
match = re.search(in_string, my_string)
print(match.string) if match else print("Something wrong")
# Напишите функцию, принимающую строковые данные и выполняющую проверку на их соответствие мейлу.
# Требования:
# -цифры (0-9).
# -только латинские буквы в большом (A-Z) и малом (a-z) регистрах.
# -в теле мейла допустимы только символы “_” и “-”. Но они не могут быть первым символом мейла.
# -символ “-” не может повторяться.
def valid_mail(mail):
    valid=r''
    compare=re.search(valid,mail)
    return mail if compare else 'Invalid mail'
# Напишите функцию, проверяющую правильность логина.
# Правильный логин – строка от 2 до 10 символов, содержащая только буквы и цифры.
def valid_log(login):
    valid_login = r'^(\w|\d){2,10}$'
    compare = re.search(valid_login, login)
    return login if compare else 'Invalid login'

print(valid_log("adD32xFx"))
