# Python program to interchange first and last elements in a list.

print("\n")


def interchangeFirstLast(l):
    l[0], l[-1] = l[-1], l[0]
    return l


print("1 : interchange first and last elements", interchangeFirstLast([1, 2, 3, 4, 5]))

# OR


def interchangeFirstLast(l):
    a = l[0]
    l[0] = l[-1]
    l[-1] = a
    return l


print("1 : interchange first and last elements", interchangeFirstLast([1, 2, 3, 4, 5]))

print("\n")


# Python program to swap two elements in a list.


def swapTwoElement(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
    return l


print("2 : swap two elements", swapTwoElement([1, 2, 3, 4, 9, 6, 7, 8, 5, 10], 4, 8))

print("\n")


# Python – Swap elements in String list. j = h and a = o


def swapStringElement(l):
    result = []
    for string in l:
        swap = string.replace("j", "h").replace("a", "o")
        result.append(swap)
    return result


print(
    "3 : Swap elements in String list",
    swapStringElement(["jella", "ja", "jaw", "janey"]),
)

print("\n")


# Python | Ways to find length of list.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
length = len(l)
print("4 : the length if list is : ", length)

# OR

test_list = [1, 4, 5, 7, 8]
print("    The list is : " + str(test_list))
counter = 0
for i in test_list:
    counter = counter + 1
print("4 : Length of list using naive method is : " + str(counter))

print("\n")

# Maximum of two numbers in Python.

maxNumber = [1, 23, 45, 6, 45, 67, 87, 54, 322, 4455, 33, 2, 2, 3, 4, 4, 4, 98]
print("5 : Maximum of two numbers", max(maxNumber))

# OR

maxNumber = [1, 23, 45, 6, 45, 67, 87, 54, 322, 4455, 33, 2, 2, 3, 4, 4, 4, 98]
print("5 : Maximum or largest of two numbers", sorted(maxNumber)[-1])

print("\n")

# Python program to find largest number in a list

list1 = [10, 20, 4, 45, 99]
list1.sort(reverse=False)
print("12 : largest or maximum element is : ", list1[-1])

print("\n")

# Minimum of two numbers in Python.

minNumber = [1, 23, 45, 6, 45, 67, 87, 54, 322, 4455, 33, 2, 2, 3, 4, 4, 4, 98]
print("6 : Minimum of two numbers", min(minNumber))

# OR

minNumber = [1, 23, 45, 6, 45, 67, 87, 54, 322, 4455, 33, 2, 2, 3, 4, 4, 4, 98]
print("6 : Minimum or smallest of two numbers", sorted(minNumber)[0])

print("\n")

# Python program to find smallest number in a list.

list1 = [10, 20, 4, 45, 99]
list1.sort(reverse=True)
print("11 : Smallest or minimum element is : ", list1[-1])


print("\n")

# Python | Ways to check if element exists in list. // doubt remake

l = [1, 2, 3, 7, 5, 68, 5, 4, 3, 7, 5, 7, 8, 4, 3]
i = 10
if i in l:
    print("7 : This element is exist in list")
else:
    print("7 : This element is exist not in list")


# or

elementExists = [1, 2, 3, 7, 5, 68, 5, 4, 3, 7, 5, 7, 8, 4, 3]
result = any(i in elementExists for i in elementExists)
print("7 : Does string contain any list element: " + str(bool(elementExists)))

print("\n")

# Different ways to clear a list in Python.

l = [1, 2, 3, 7, 5, 68, 5, 4, 3, 7, 5, 7, 8, 4, 3]
del l[:]
print("8 : clear a list : ", l)

print("\n")

# Python | Reversing a List.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = l[::-1]
print("9 : Reversing a List", new_list)

print("\n")

# Python | Cloning or Copying a list.


def clonOrCopy(l):
    new_item = l[:]
    return new_item


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = clonOrCopy(l)
print("10 : orignal list", l)
print("     after cloning", l2)
print("\n")

# Python program to find second largest number in a list.

l = [1, 2, 23, 45, 6, 4, 34, 5, 6, 87]
l.sort()
print("13 : second largest number : ", l[-2])

# or

# Python program to find second largest number in a list.

l = [0, 10, 10, 20, 15, 20, 45, 99]
max = 0
preMax = 0

for num in l:
    if num > max:
        preMax = max
        max = num

    elif num > preMax and max != num:
        preMax = num

print("13 : Second highest number is : ", str(preMax))


print("\n")


# Python | Sum of number digits in List.

list = [12, 43, 456]
res = []
for number in list:
    x = 0
    for new in str(number):
        x += int(new)
    res.append(x)
print("14 : Sum of number digits : ", res)

print("\n")

# Python | Multiply all numbers in the list.

list1 = [2, 2, 2, 2, 2]
result = 0
for number in list1:
    result = result + number
print("15 : Multiply all numbers : ", result)

print("\n")

# Remove multiple elements from a list in Python.

l = [12, 33, 556, 3, 4, 61]
del l[2:4]
print("16 : Remove multiple elements : ", l)

# or

l = [12, 33, 556, 3, 4, 61]
for ele in l:
    if ele % 2 == 0:
        removeElement = l.remove(ele)
print("16 : Remove multiple elements : ", l)

print("\n")

# Python program to print even numbers in a list.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for number in list:
    if number % 2 == 0:
        print(" 17 : print even numbers : ", number, end=",")
print("\n")

# list of unique element or set elements # doubt

list1 = [10, 20, 4, 4, 45, 99, 99]
print(list1)
new_list = set(list1)
print(" 18 : unique element or set elements : ", new_list)
