# Lesson 5
money = float(input("How much money are you starting with? "))
cookies = input("Input the cookies ")
profit = 0
b_count = 0
c_count = 0
for character in cookies:
    if character == "b":
        b_count += 1
    elif character == "c":
        c_count += 1
    else:
        print(f"{character}  is not a cookie")
total_cookies = b_count + c_count
profit = 2 * b_count + 1.25 * c_count
money = money - 0.5 * c_count - 0.75 * b_count
total_money = money + profit
print(f"Total number of cookies sold: {total_cookies}")
print(f"Total profit: {profit}")
print(f"Total money: {total_money}")
