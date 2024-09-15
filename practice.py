# Python program to swap two elements in a list

print("\n")


def swapElement(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l


a = 2
b = 6
print(
    f"1 : swap two elements : {a} and {b} ",
    swapElement([1, 2, 7, 4, 5, 6, 3, 8, 9], 2, 6),
)

# Python | Reversing a List

print("\n")


def reverse(l):
    new_item = l[::-1]
    return new_item


print("2 : Reversing a List : ", reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("\n")

# Minimum of two numbers in Python.
l = [44, 55, 6, 654, 22, 2, 54332, 456, 76, 44, 98]
print("3 : Maximum of two numbers : ", max(l))

# or

l = [44, 55, 6, 654, 22, 2, 54332, 456, 76, 44, 98]
print("3 : Minimum of two numbers : ", sorted(l)[0])

print("\n")

# Different ways to clear a list in Python.


l = [44, 55, 6, 654, 22, 2, 54332, 456, 76, 44, 98]
del l[:]
print("4 : clear a list : ", l)

print("\n")


#  Copying a list
def copyingList(l1):
    l2 = l1
    print("5 : Copying a list2 :", l2)
    return l1


print("5 : Copying a list1 : ", copyingList([1, 2, 3, 4, 5, 6, 7]))

print("\n")

# Python – Swap elements in String list.


def swapStringElement(l1):
    new_list = []
    for i in l1:
        result = i.replace("a", "k").replace("v", "w")
        new_list.append(result)
    return new_list


print(
    "6 : Swap elements in String list : ",
    swapStringElement(["av", "va", "avav", "vaav"]),
)

print("\n")

# Python | Ways to find length of list.

l = [44, 55, 6, 654, 22, 2, 54332, 456, 76, 44, 98]
print(len(l))

# or

print("\n")

l = [44, 55, 6, 654, 22, 2, 54332, 456, 76, 44, 98]
counter = 0
for i in l:
    counter = counter + 1
print(counter)


print("\n")

l = [1, 2, 3, 7, 5, 68, 5, 4, 3, 7, 5, 7, 8, 4, 3]
i = 10
if i in l:
    print("This element is exist in list")
else:
    print("This element is exist not in list")

print("\n")


str_nums = ["4", "8", "6", "5", "3", "2"]
int_nums = map(int, str_nums)
list(int_nums)
[4, 8, 6, 5, 3, 2]


# nothing

numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
words = ["Welcome", "to", "real", "python"]


# square of elements.
def addition(n):
    return n + n


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print("square may be : ", list(result))

print("\n")

# one argument pass.

s = ""

