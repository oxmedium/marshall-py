# Lesson 47
def sum(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + sum(num-1)
    
print(sum(5))