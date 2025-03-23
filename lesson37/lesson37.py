# Lesson 37
def compress(text):
    new = ''
    count = 1
    for i in range(1,len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            new += text[i-1]
            new += str(count)
            count = 1
    new += text[-1] + str(count)
    if len(text) > len(new):
        return new
    else:
        return text
test = "aabcccccaaa"
test2 = "abcde"
print(test)
print(compress(test))
print(test2)
print(compress(test2))