print("\n")
numbers = [10, 30, 40]
numbers.insert(1, 20)
print(numbers)

print("\n")

numbers = [1, 3, 5]
even_numbers = [4, 6, 8]
numbers.extend(even_numbers)
print("List after append : ", numbers)

print("\n")


numbers = [21, 34, 54, 12]
print("Before Append : ", numbers)
numbers.append(32)
print("After Append : ", numbers)

print("\n")


def add_nums(a, b):
    x = a + b
    print("sum is", x)


add_nums(9, 10)

# OR


def add_nums(a, b):
    x = a + b
    return x


value = add_nums(8, 9)
print("sum is", value)

print("\n")


def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print("unique list", unique_list([1, 2, 2, 3, 3, 4, 3, 3, 4, 5]))

print("\n")
