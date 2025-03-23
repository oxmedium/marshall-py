# Lesson 35
def remove_dupes(a_list):
    new_list = []
    for item in a_list:
        if item not in new_list:
            new_list.append(item)
    return new_list
test = ['a', 'b', 'c', 'c', 'b', 'c', 'a', 'a', 'd']
print(test)
print(remove_dupes(test))
