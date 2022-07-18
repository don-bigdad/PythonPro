import datetime
import time
#1
def decorator(func):
    def another_func():
        with open("decorator_count.txt","a") as file:
            file.write(f'Decorated function worked in:{datetime.datetime.now()}\n')
        with open("decorator_count.txt", "r") as file:
            return len(file.readlines())
    return another_func

@decorator
def some():
    return 1

# print(some())

#2
list_of_func=[]
def to_list(func):
    list_of_func.append(func)
    return func
@to_list
def sum(a,b):
    return a+b
@to_list
def mul(a,b):
    return a*b

# print(list_of_func)
#3
def from_str_to_txt_file(func):
    def to_file(self):
        with open(f'{self.__class__.__name__}', "a") as file:
                file.write(f'{func(self)}\n')
        return func(self)
    return to_file

class Say_hello:
    @from_str_to_txt_file
    def __str__(self):
        return f'Hello from class {self.__class__.__name__}'

class Say_hello_2:
    @from_str_to_txt_file
    def __str__(self):
        return f'Hello from class {self.__class__.__name__}'


# x=Say_hello()
# y=Say_hello_2()
# print(y)
# print(x)

#4
def parameters(count,filename):
    start = time.time()
    while count!=0:
        def hard_decorator(func):
            def dec():
                return func
            return dec
        count -= 1
    end=time.time()
    with open(f'{filename}.txt', "a") as f:
        f.write(f'function start at {start} \n')
        f.write(f'function stop at {end}\n')
        f.write(f'Total time for all tests:{end-start} sec \n')
    return hard_decorator

@parameters(10000000,"test")
def recur_fibo(n=10000):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

