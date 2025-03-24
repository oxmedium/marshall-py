# Lesson 39
def factor(num1,num2):
    for i in range(min(num1,num2),0,-1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1

print(factor(4,12))
print(factor(27,1080))

def e_gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return e_gcd(num2, num1 % num2)
    
print(e_gcd(8,12))
print(e_gcd(27,1080))
    