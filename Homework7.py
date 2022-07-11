#2
def my_range(start,stop=None,step=1):
    if stop == None:
        raise IndexError
    step = -step if stop < 0 else step
    while start != stop:
        yield start
        start += step
        if start<stop and stop<0:
            return None
    return None


# x=my_range(1,-10,2)
# for elem in x:
#     print(elem)

#3
def simpe_number(number):
    for item in my_range(2,number):
        for elem in my_range(2,item):
            if item%elem==0:
                break
        else:
            yield item
    return None
# x=simpe_number(100)
#
# for elem in x:
#     print(elem)

#4
# x=list(elem**3 for elem in range(0,int(input())))
# print(x)

#1
def geometr_progression(start,factor,limit=None):
    if limit == None:
        while not bool(limit):
            limit = yield start
            start *= factor
    else:
        while start<limit:
            yield start
            start *= factor
    return None


some=geometr_progression(3,-2)
print((some.__next__()))
print((some.__next__()))
print((some.__next__()))
print((some.__next__()))
print((some.__next__()))
print((some.__next__()))
some.send(1)
print((some.__next__()))
