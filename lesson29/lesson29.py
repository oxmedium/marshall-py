# Lesson 29
def consonent(text, vowel=False):
    total = 0
    for character in text:   
        if character.lower().isalpha and character not in {"a", "e", "i", "o", "u"}:
            total += 1
    if not vowel:
        return total
    else:
        total = 0
        for character in text:
            if character.lower().isalpha and character in {"a", "e", "i", "o", "u"}:
                total += 1
        return total
print(f"Count of {consonent("hello")}")
print(f"Count of {consonent("hello,", True)}")