# Lesson 44
def dictionary(text):
    word = sorted(text.lower())
    answer = {}
    for letter in word:
        if letter not in answer:
            answer[letter] = 1
        else:
            answer[letter] += 1
    return answer
test = "hello"
print(dictionary(test))