import re

# valid card number function
def valid_card(card_number):
    return card_number if re.search(r'^\d{4}-\d{4}-\d{4}-\d{4}$', my_card) else 'Invalid card number'
my_card = "1233-5213-9990-7622"
print(valid_card(my_card))
# Напишите регулярное выражение, которое будет находить в тексте фрагменты,
# состоящие из одной буквы R, за которой следует одна или более букв b,
# за которой одна r. Учитывать верхний и нижний регистр.
in_string = r'\w[Rb+r]$'
my_string = "asRbbbr"
match = re.search(in_string, my_string)
print(match.string) if match else print("Something wrong")
# Напишите функцию, принимающую строковые данные и выполняющую проверку на их соответствие мейлу.
# Требования:
# -цифры (0-9).
# -только латинские буквы в большом (A-Z) и малом (a-z) регистрах.
# -в теле мейла допустимы только символы “_” и “-”. Но они не могут быть первым символом мейла.
# -символ “-” не может повторяться.
def valid_mail(mail):
    return mail if re.search(r'^[^-|_]\w*[-{0,1}]?\w*?[@]?\w*(.com)?$',mail) else 'Invalid mail'
print(valid_mail("mymail31-2@gmail.com"))
# Напишите функцию, проверяющую правильность логина.
# Правильный логин – строка от 2 до 10 символов, содержащая только буквы и цифры.
def valid_log(login):
    return login if re.search(r'^(\w|\d){2,10}$', login) else 'Invalid login'
print(valid_log("adDa2xFx"))
