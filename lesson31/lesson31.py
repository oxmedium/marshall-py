# Lesson 31
#method 1
def anagram(word1, word2):
    list1 = sorted(word1)
    list2 = sorted(word2)
    if list1 == list2:
        return True
    else:
        return False
print(anagram("mike", "ekim"))

#method 2

def anagram1(word3, word4):
    if len(word3) != len(word4):
        return False
    else:
        for char in word3:
            if word3.count(char) != word4.count(char):
                return False
    return True
print(anagram1("mike", "ekim"))
print(anagram1("michael", 'mikey'))