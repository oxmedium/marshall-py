# Lesson 27
def cleaner(text):
    result = ''
    for char in text:
        if char.isalpha():
            result += char
    return result

new = cleaner('mike_oxlong')
print(new)