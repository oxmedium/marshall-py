# Lesson 12
angles = 0
while angles != 180:
    a = int(input("Enter the 3 angles of the triangle: "))
    b = int(input())
    c = int(input())
    angles = a + b + c
    if angles != 180:
        print("Angles need to add up to 180!")

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isoceles")
else:
    print("Scalene")