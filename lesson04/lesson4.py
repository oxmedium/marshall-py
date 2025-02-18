# Lesson 4
import math

fence1 = input()
fence2 = input()
fence3 = input()
length = len(fence1) + len(fence2) + len(fence3)
extra = length % 12
paint = math.ceil(length / 12)
cost = paint * 14.95
print(length)
print(extra)
print(cost)