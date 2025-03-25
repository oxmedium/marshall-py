# Lesson 46
def next(num):
    if num % 2 == 0:
        return num / 2
    else:
        return num*3 + 1

def euler(num, dictionary):
    if num in dictionary:
        return dictionary[num]
    else:
        sequence = [num]
        size = 1
        while sequence[-1] != 1 and sequence[-1] not in dictionary:
            new = next(sequence[-1])
            if new in dictionary:
                size += dictionary[new]
                break
            else:
                sequence.append(new)
                size += 1
        for i in range((len(sequence))):
            dictionary[sequence[i]] = size - i
    return size

memory = {1:1, 2:2}
for start in range(3,1000000):
    current_length = euler(start, memory)

answer = 0
length = 0
for key in range(1,1000000):
    if memory[key] > length:
        answer = key
        length = memory[key]

print(f'longer answer is {answer} with a chain {length} long')