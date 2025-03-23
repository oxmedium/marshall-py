# Lesson 32

def add(word1,word2):
    set1 = set(word1)
    set2 = set(word2)
    letters = []
    if not word1 and not word2:
        return []
    else:
        for character in set1:
            if character in set2:
                letters.append(character)
        return sorted(letters)
print(add("hello world", "goodbye world"))