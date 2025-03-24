# Lesson 40
def factors_list(num):
    divider_list = []
    for divider in range(1,num+1):
        if num % divider == 0:
            divider_list.append(divider)
    return divider_list

def prime(num):
    return len(factors_list(num)) == 2

def prime_list(upper):
    primes = []
    for ber in range(1, upper+1):
        if prime(ber):
            primes.append(ber)
    return primes

print(prime_list(100))
