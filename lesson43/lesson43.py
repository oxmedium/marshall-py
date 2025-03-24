# Lesson 43
def r_duplicates(a_list):
    new = []
    for value in a_list:
        if value not in new:
            new.append(value)
    return new
'''
def r_duplicates(a_list):
    return list(set(a_list))
'''
a_list = [1,2,2,3,3,3,4,4,4,4]
print(r_duplicates(a_list))

#Unique letters in a string
def unique(a_list):
    new_set = set()
    for word in a_list:
        temp = set(word)
        new_set = new_set | temp
    return new_set

test = ['hello', 'goodbye', 'world', 'mr. park!']

print(unique(test))

#Set interactions
def intersect_count(a_list):
    if a_list:
        new = a_list[0]
        for other in a_list[1:]:
            new = new & other
    return len(new)

testing = [{1,2,3,7}, {3,4,5,7}, {5,6,7,8}]
print(intersect_count(testing))