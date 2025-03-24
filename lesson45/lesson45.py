# Lesson 45
def dictionary(a_list):
    return {key: len(key) for key in a_list}

test = ('apple', 'banana', 'cherry', 'date')
print(dictionary(test))

#Fibonnaci
def fib(num):
    sequence = {0:0, 1:1}
    if num in sequence:
        return sequence
    else:
        for i in range(2,num+1):
            sequence[i] = sequence[i-1] + sequence[i-2]
        return sequence

print(fib(10))