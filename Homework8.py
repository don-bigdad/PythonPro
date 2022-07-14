import random

seq=[random.randint(0,10) for elem in range(3)]

#3
def sum_my_list(seq,rule):
    return rule(seq)

def rule(seq):
    res_list=[]
    for elem in seq:
        for item in seq:
            res_list.append(elem+item)
    return res_list

# print(sum_my_list(seq,rule))


#1
def gen(start,limit,sequence):
     return sequence(start,limit)

def sequance_mul(start,limit):
    while limit!=0:
        start *= 2
        limit -= 1
        yield start

def increment(start,limit):
    i=1
    while limit != 0:
        start+=i
        limit-=1
        i+=1
        yield start

def square(start,limit):
    while limit != 0:
        limit -= 1
        start = start**(1/2)
        yield start

# for elem in gen(2,10,sequance_mul):
#     print(elem)
#
# for elem in gen(20,5,increment):
#     print(elem)
#
# for elem in gen(2048,7,square):
#     print(elem)

#2
def fib(n):
    memory=[0,1]
    def calculate():
        last_number=memory[-1]
        pre_last=memory[-2]
        if n<len(memory):
            return memory[n]
        while len(memory)!=n+1:
            last_number,pre_last=pre_last+last_number,last_number
            memory.append(last_number)
        return memory[n]
    return calculate

for elem in range(10):
    print(fib(elem)())
