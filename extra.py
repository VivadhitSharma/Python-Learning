print("\n")

import copy

list1 = [1, 2]
list2 = [3, 4, list1]
list3 = [list1, 5, 6]
list4 = copy.copy(list1)
list1.append([30, 40])
print("list1 : ", list1)
print("list2 : ", list2)
print("list3 : ", list3)
print("list4 : ", list4)

print("\n")

prime_number = [2,3,5,7]
removed_element = prime_number.pop(5)
print("pop : ", prime_number)
