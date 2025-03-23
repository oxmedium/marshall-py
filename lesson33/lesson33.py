# Lesson 33
def mean(nums):
    avg = 0
    if str(sum(nums)).isnumeric():
        avg = sum(nums) / len(nums)
        return avg
    else:
        return avg
def median(nums):
    bers = sorted(nums)
    mid = 0
    if len(bers) % 2 == 0:
        right = bers[len(nums) // 2]
        left = bers[len(nums) // 2 - 1]
        mid = (right + left) / 2
        return mid
    else:
        mid = bers[len(nums) // 2]
        return mid
num = [2,2,3,10,6,7]
print(f"Mean: {mean(num)}")
print(f"Median: {median(num)}")