# Lesson 34 prt1
def tonum(text):
    splited = text.split(',')
    a_list = []
    for num in splited:
        a_list.append(int(num))
    return a_list
print(tonum("1,2,3,4,5"))
#random number
from random import randrange
def rand_list(start, end, frequency):
    if start < end and frequency > 0:
        a_list = []
        for _ in range(frequency):
            a_list.append(randrange(start, end+1))
        return a_list
    else:
        return []
print(rand_list(1,10,4))