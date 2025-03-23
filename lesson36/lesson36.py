# Lesson 36
def factor(num):
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors
def primechecker(num):
    prime = False
    if len(factor(num)) == 2:
        prime = True
    return prime

print(f"factors of 13: {factor(13)}")
print(f"factors of 26: {factor(26)}")
print(f"is 13 prime: {primechecker(13)}")
print(f"is 26 prime: {primechecker(26)}")
