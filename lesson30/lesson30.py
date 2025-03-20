# Lesson 30
def line(num):
    text = ''
    for i in range(1,num+1):
        if i % 2 == 0:
            text += '0'
        else:
            text += '1'
    return text
def output(num):
    for i in range (1,num+1):
        print(line(i))
ber = output(5)
print(ber)