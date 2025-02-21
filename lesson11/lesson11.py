# Lesson 11
point = input("Input a point: ")

point = point.split(' ')#turns 1 1 -> ('1', '1')

point = list(map(int, point))
print(point)

x, y = point
print(f"The x coordinate is: {x}")
print(f"The y coordinate is: {y}")

if x > 0:
    if y > 0:
        print("Quadrant 1")
    else:
        print("Quadrant 4")
else:
    if y > 0:
        print("Quadrant 2")
    else:
        print("Quadrant 3")