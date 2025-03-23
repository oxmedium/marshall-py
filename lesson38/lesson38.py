# Lesson 38
def palindrome(text):
    return text[::-1] == text

palindromes = []

for num1 in range(999,99,-1):
    for num2 in range(999,99,-1):
        num = num1 * num2
        if palindrome(str(num)):
            palindromes.append(num)

print(max(palindromes))