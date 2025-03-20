# Lesson 28
''' Solution 1
def palindrome(word):
    return word == word[::-1]

print(palindrome('tacocat'))
'''#Solution 2
def palindrome(word):
    if not word:
        return True
    elif len(word) < 4:
        return word[0] == word[-1]
    else:
        mid = len(word) // 2
        for i in range(0, mid):
            l = i
            r = -1*i -1
            if word[l] != word[r]:
                return False
        return True
print(palindrome('tacocat'))