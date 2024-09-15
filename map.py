print("\n")
# square using map

def square(number):
    return number**2


number = [1, 2, 3, 4, 5]
squared = map(square, number)
print(list(squared))
print("\n")

# Squaring Elements:

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
print("\n")

# Doubling Strings:

words = ["apple", "banana", "cherry", "date"]
doubled_words = list(map(lambda x: x * 2, words))
print(doubled_words)
print("\n")

# Converting Celsius to Fahrenheit:

temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, temperatures_celsius))
print(temperatures_fahrenheit)
print("\n")

# Checking Even or Odd:

numbers = [1, 2, 3, 4, 5]
is_even = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))
print(is_even)
print("\n")

# Finding Length of Words:

words = ["apple", "banana", "cherry", "date"]
word_lengths = list(map(len, words))
print("Finding Length of Words:", word_lengths)
print("\n")

# Adding Two Lists Element-wise:

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print("Adding Two Lists Element-wise", sum_lists)
print("\n")

# Extracting First Character from a List of Strings:

words = ["apple", "banana", "cherry", "date"]
first_chars = list(map(lambda x: x[0], words))
print("Extracting First Character from a List of Strings", first_chars)

# if we want to ask user to the value in the lists.
print("\n")

list = []
n = int(input("enter number of element: "))
for i in range(0, n):
    ele = int(input())
    list.append(ele)
print(list)

print("\n")
