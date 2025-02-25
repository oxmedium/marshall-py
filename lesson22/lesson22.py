# Lesson 22
n = int(input("What Nth sequence of the Fibonacci sequence do you want: "))
one = 0
two = 1
three = 0

for i in range (2, n+1):
    three = one + two
    one = two
    two = three
if n == 1:
    print(two)
else:
    print(three)