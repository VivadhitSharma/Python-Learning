'''

# WAP to input 2 Integer Number as input from User and find the sum.
print("\n")

num1 = int(input("Enter first no. : "))
num2 = int(input("Enter Second no. : "))
sum = num1 + num2
print("sum of two number is : ", sum)


#WAP to input 2 Float Number as a Input from User and display the result of division and floor division.
print("\n")

num1 = float(input("Enter First no. : "))
num2 = float(input("Enter Second no. : "))
div_res = num1/num2
floor_res = num1//num2
print(f"Division of {num1} and {num2} is : ", div_res)
print(f"Floor Division of {num1} and {num2} is : ", floor_res)


# WAP to get Multiple inputs From a User in One Line
print("\n")

# WAP to format Output String by its positions
print("\n")

name = input("Enter your name : ")
print(f"Your name is {name}")


# WAP to access Output String Arguments by name
print("\n")

name = str(input("Enter Your Name : "))
print(name)


# 8 : WAP which accepts the user's first and last name and print  them in reverse order with a space between them
print("\n")

first_name = input("Enter your First Name : ")
last_name = input("Enter Your last Name : ")
full_name = last_name + " " + first_name
print("Reverse order name is : ", full_name)


# 9 : WAP which accepts the radius of a circle from the user and Compute the area.
print("\n")

import math
radius = float(input("Enter the radius of circle : "))
area = math.pi * radius ** 2
print("The area of circle with radius is : ", area)


# WAP to print the factorial of the number input by the user.
print("\n")

import math
num = int(input("Enter a number to calculate its factorial : "))
result = math.factorial(num)
print(f"The factorial of {num} is : ", result)


# 11 : WAP to implement arithmetic operators.
print("\n")

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
operator = input("which arthemetic operator you want to perfrom : ")
if operator == "+":
    print("Additon : ", num1 + num2)
elif operator == "-":
    print("Subtraction : ", num1 - num2)
elif operator == "/":
    if num2 != 0:
        print("Division : ", num1 / num2)
    else:
        print("Error : can't divide by zero : ")
elif operator == "*":
    print("Multiply : ", num1 * num2)
elif operator == "%":
    print("Modulus : ", num1 % num2)
elif operator == "**":
    print("Exponentiation : ", num1**num2)
elif operator == "//":
    print("Floor Division : ", num1 // num2)
else:
    print("This is not an arithmetic operator")


# 12 WAP to implement relational (comparison) operators
print("\n")

def relational_operators_example(a, b):
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"{a} <= {b}: {a <= b}")
num1 = 10
num2 = 5
relational_operators_example(num1, num2)


# WAP to implement logical, membership, identity operators.
print("\n")

# Logical operators example
def logical_operators_example():
    x = True
    y = False
    print(f"{x} and {y}: {x and y}")
    print(f"{x} or {y}: {x or y}")
    print(f"not {x}: {not x}")

# Membership operators example
def membership_operators_example():
    my_list = [1, 2, 3, 4, 5]
    print(f"8 is in {my_list}: {8 in my_list}")
    print(f"6 not in {my_list}: {6 not in my_list}")

# Identity operators example
def identity_operators_example():
    a = 10
    b = 12
    print(f"{a} is {b}: {a is b}")
    print(f"{a} is not {b}: {a is not b}")

# Call the functions
logical_operators_example()
membership_operators_example()
identity_operators_example()

# 14 : WAP to implement bitwise operators
print("\n")


# 15 :WAP to implement show Operators Precedence
print("\n")


def operator_precedence_example():
    a = 5
    b = 3
    c = 2

    result = a + b * c
    print(f"{a} + {b} * {c} = {result}")

    result = (a + b) * c
    print(f"({a} + {b}) * {c} = {result}")

    result = a ** b * c
    print(f"{a} ** {b} * {c} = {result}")

    result = a + b / c
    print(f"{a} + {b} / {c} = {result}")

    result = (a + b) / c
    print(f"({a} + {b}) / {c} = {result}")

    result = a % b + c
    print(f"{a} % {b} + {c} = {result}")

operator_precedence_example()

# 16 : Print even and odd numbers using loops
print("\n")

def print_even_and_odd_numbers(start, end):
    print("Even numbers:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")

    print("\nOdd numbers:")
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num, end=" ")

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print_even_and_odd_numbers(start_range, end_range)


# 17 : WAP to enter a number and print its multiplication table till 10
print("\n")

def multiplication_table():

    number = int(input("Enter a number: "))

    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

multiplication_table()


# 18 : WAP to count the currency note for the amount entered by the user. Number of notes are 100, 500, 1000.
print("\n")


# 19 : Program to print 4 digits and their sum
print("\n")

def print_digits_and_sum(number):

    digit_1 = number // 1000
    digit_2 = (number // 100) % 10
    digit_3 = (number // 10) % 10
    digit_4 = number % 10

    print(f"Digit 1: {digit_1}")
    print(f"Digit 2: {digit_2}")
    print(f"Digit 3: {digit_3}")
    print(f"Digit 4: {digit_4}")

    digit_sum = digit_1 + digit_2 + digit_3 + digit_4
    print(f"Sum of digits: {digit_sum}")

four_digit_number = int(input("Enter a 4-digit number: "))

if 1000 <= four_digit_number <= 9999:
    print_digits_and_sum(four_digit_number)
else:
    print("Please enter a valid 4-digit number.")



""" 20 : Using datetime module in python, display the following:
Current date and time
Format date and time
Year, month, day, hour
Difference between 2 dates
Check if a date is in past or future
Get the weekday of a given date. """

print("\n")

from datetime import datetime, timedelta
# Current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Format date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_datetime)

# Year, month, day, hour
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}")

# Difference between 2 dates
date1 = datetime(1999, 1, 1)
date2 = datetime(2000, 1, 1)
date_difference = date2 - date1
print("Difference between two dates:", date_difference)

# Check if a date is in past or future
check_date = datetime(2023, 1, 1)
if check_date > current_datetime:
    print("The given date is in the future.")
elif check_date < current_datetime:
    print("The given date is in the past.")
else:
    print("The given date is the current date.")

# Get the weekday of a given date
weekday = current_datetime.strftime("%A")
print("Weekday of the current date:", weekday)


# 21 : Using calendar module, print the calendar of a given month and year.
print("\n")

import calendar

def print_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    print(f"Calendar for {month_name} {year}:")
    print("Mo  Tu  We  Th  Fr  Sa  Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")  # Print empty space for days outside the month
            else:
                print(f"{day:2} ", end=" ")  # Adjust formatting for single-digit days
        print()

# Input: Year and Month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Call the function to print the calendar
print_calendar(year, month)


""" 22. WAP to print the following star pattern.
*
**
***
****
*****
"""
print("\n")

for i in range(6):
    for j in range(i):
        print("*", end="")
    print("")


""" 23. WAP to print the following star pattern.
*****
****
***
**
* """

print("\n")

for i in range(6):
    for j in range(i - 1,4):
        print("*", end="")
    print("")

""" 24 : WAP to print the following star pattern.
      *
     ***
    *****
   ******* """

print("\n")

for i in range(5):
    print(" " * (5-i), end="")
    print("*" * (2 * i - 1), end="")
    print() 
print("\n") 

""" 25 : WAP to print the following star pattern.
      *
     ***
    *****
   *******
    *****
     ***
      *
"""
for i in range(0,4,1):
    print(" " * (5 - i), end="")
    print("*" * (2 * i - 1), end="")
    print()
for i in range(4, 0, -1):
    print(" " * (5 - i), end="")
    print("*" * (2 * i - 1), end="")
    print()

'''

print("\n") 
''' WAP to print the following star pattern.
      *
    *** 
  *****
******* '''
'''
def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        
        for k in range(2 * i - 1):
            print("*", end="")
        print()

rows = 4
print_star_pattern(rows)

print("\n") 

#WAP to input number and find the sum of numbers till user enters zero.

def sum_of_numbers():
    sum_result = 0
    while True:
        user_input = float(input("Enter a number (enter 0 to exit): "))      
        if user_input == 0:
            break
        sum_result += user_input

    print("Sum of numbers entered:", sum_result)
sum_of_numbers() 

print("\n") 

# WAP to count odd and even numbers in a given range.

def count_odd_even_numbers(start, end):
    odd_count = 0
    even_count = 0

    for number in range(start, end + 1):
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Count of odd numbers:", odd_count)
    print("Count of even numbers:", even_count)

start_range = 1
end_range = 20

count_odd_even_numbers(start_range, end_range)

print("\n") 

# WAP for password validation.

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

user_password = input("Enter your password: ")

if is_valid_password(user_password):
    print("Password is valid!")
else:
    print("Invalid password. Please follow the password criteria.")

print("\n")

# WAP to check if the string is palindrome.

def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

print("\n")

# WAP for string reversal.

def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Enter a string: ")

reversed_string = reverse_string(user_input)

print("Reversed string:", reversed_string)

print("\n")

# WAP to show string formatting using different formatting techniques.

name = "Anu"
age = 25
height = 5.3

formatted_string_f = f"My name is {name}, I am {age} years old, and my height is {height:.2f}."
print("F-string formatting:", formatted_string_f)

formatted_string_format = "My name is {}, I am {} years old, and my height is {:.2f} feet.".format(name, age, height)
print("format() method formatting:", formatted_string_format)

formatted_string_percent = "My name is %s, I am %d years old, and my height is %.2f feet." % (name, age, height)
print("Percentage-formatting:", formatted_string_percent)


print("\n")

# WAP to implement following built-in functions:len(), capitalize(), count(), endswith(), find(), index(), isalnum(), isalpha(), isdigit(), islower(), isupper(), join(), split(), title(), upper(), strip().

def string_operations(input_string):
    # len()
    length = len(input_string)
    print("Length:", length)

    # capitalize()
    capitalized_string = input_string.capitalize()
    print("Capitalized:", capitalized_string)

    # count()
    count_of_char_a = input_string.count('a')
    print("Count of 'a':", count_of_char_a)

    # endswith()
    ends_with_anu = input_string.endswith('anu')
    print("Ends with 'anu':", ends_with_anu)

    # find()
    index_of_hi = input_string.find('Hi')
    print("Index of 'Hi':", index_of_hi)

    # index()
    index_of_anu = input_string.index('anu')
    print("Index of 'anu':", index_of_anu)

    # isalnum()
    is_alphanumeric = input_string.isalnum()
    print("Is alphanumeric:", is_alphanumeric)

    # isalpha()
    is_alpha = input_string.isalpha()
    print("Is alphabetic:", is_alpha)

    # isdigit()
    is_digit = input_string.isdigit()
    print("Is digit:", is_digit)

    # islower()
    is_lower = input_string.islower()
    print("Is lowercase:", is_lower)

    # isupper()
    is_upper = input_string.isupper()
    print("Is uppercase:", is_upper)

    # join()
    words_list = ['This', 'is', 'a', 'sample']
    joined_string = ' '.join(words_list)
    print("Joined string:", joined_string)

    # split()
    split_string = input_string.split(',')
    print("Split string:", split_string)

    # title()
    title_case_string = input_string.title()
    print("Title case:", title_case_string)

    # upper()
    uppercase_string = input_string.upper()
    print("Uppercase:", uppercase_string)

    # strip()
    stripped_string = input_string.strip()
    print("Stripped:", stripped_string)
user_input = "   Hi, anu!   "
string_operati(user_input)


print("\n")

#WAP to show negative indexing in Python using string.

def negative_indexing_example(input_string):
    last_char = input_string[-1]
    second_last_char = input_string[-2]
    third_last_char = input_string[-3]

    print("Original string:", input_string)
    print("Last character:", last_char)
    print("Second last character:", second_last_char)
    print("Third last character:", third_last_char)

user_input = "Python Negative Indexing Example"
negative_indexing_example(user_input)

print("\n")

# WAP count vowels in a given string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

user_input = input("Enter a string: ")
result = count_vowels(user_input)
print("Number of vowels in the given string:", result)

print("\n")

# WAP to sum all the items in a list.

def sum_of_list_items(input_list):
    return sum(input_list)

user_list = [1, 2, 3, 4, 5]
result = sum_of_list_items(user_list)
print("Sum of all items in the list:", result)

print("\n")

# WAP to multiply all the items in a list.

def multiply_list_items(input_list):
    result = 1
    for item in input_list:
        result *= item
    return result

user_list = [1, 2, 3, 4, 5]
result = multiply_list_items(user_list)
print("Product of all items in the list:", result)


print("\n")

# WAP to get the largest number from a list.

def find_largest_number(input_list):
    return max(input_list)

user_list = [12, 45, 78, 23, 56, 89]
result = find_largest_number(user_list)
print("The largest number in the list is:", result)


print("\n")

# WAP to remove all the occurrences of an element from a list.

def remove_all_occurrences(input_list, element):
    return [item for item in input_list if item != element]

user_list = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2
result_list = remove_all_occurrences(user_list, element_to_remove)
print(f"List after removing all occurrences of {element_to_remove}: {result_list}")


print('\n')

# WAP to find the sum, max, min element of a list.

def list_operations(input_list):
    list_sum = sum(input_list)
    max_element = max(input_list)
    min_element = min(input_list)
    return list_sum, max_element, min_element

user_list = [12, 45, 78, 23, 56, 89]
sum_result, max_result, min_result = list_operations(user_list)

print("Sum of the list:", sum_result)
print("Maximum element in the list:", max_result)
print("Minimum element in the list:", min_result)


print("\n")

# WAP to show list slicing.

def list_slicing_example(input_list):
    full_list = input_list[:]
    print("Full list:", full_list)

    sliced_list_1 = input_list[1:4]
    print("Sliced list from index 1 to 4 (exclusive):", sliced_list_1)

    sliced_list_2 = input_list[:3]
    print("Sliced list from the beginning to index 3 (exclusive):", sliced_list_2)

    sliced_list_3 = input_list[2:]
    print("Sliced list from index 2 to the end:", sliced_list_3)

user_list = [10, 20, 30, 40, 50, 60, 70]
list_slicing_example(user_list)

# WAP to convert string into a list of characters.

string_input = "Hello, World!"
char_list = list(string_input)

print(char_list)

# Using list comprehension square the number of a list, entered by the user.


input_numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in input_numbers]
squared_numbers = [num ** 2 for num in numbers]
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)


# Using list comprehension print “even”, “odd” depending upon the number in the range 1-20.


result = ["even" if num % 2 == 0 else "odd" for num in range(1, 21)]
print(result)


# Using list comprehension to print all the numbers which have 3 in them in the range 1-30.

result = [num for num in range(1, 31) if '3' in str(num)]
print(result)


# Using map function to convert a list = [‘4’, ‘8’, ‘6’, ‘5’] into integers [4,8,6,5].

string_list = ['4', '8', '6', '5']
integer_list = list(map(int, string_list))

print(integer_list)


""" Using map & lambda function add two lists.
Example:
List1 = [1, 2]
List2 = [3,4]
output = [4, 6] """

list1 = [1, 2]
list2 = [3, 4]

result = list(map(lambda x, y: x + y, list1, list2))

print(result)


# WAP to print the duplicate values from a list of integers.

numbers = [1, 2, 3, 4, 2, 7, 8, 3, 4, 9]
seen = set()
duplicates = set(x for x in numbers if x in seen or seen.add(x))

print("Duplicate values:", list(duplicates))


# Develop Rock Paper Scissor game against computer.

a = input("Enter player one: ")
b = input("Enter player two: ")

if a == b:
    print("Tie")
elif (a == "rock" and b == "scissor") or (a == "paper" and b == "rock") or (a == "scissor" and b == "paper"):
    print("{0} wins".format(a))
elif (a == "rock" and b == "paper") or (a == "paper" and b == "scissor") or (a == "scissor" and b == "rock"):
    print("{0} wins".format(b))
else:
    print("Invalid")


# Using lambda function convert °C to °F.

celsius_to_fahrenheit = lambda c: (9/5) * c + 32

celsius_temperature = 25
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

print(f"{celsius_temperature}°C is equal to {fahrenheit_temperature}°F")


# WAP to print current day.


from datetime import datetime

current_day = datetime.now().strftime("%A")
print("Current day:", current_day)


# WAP to show local and global variables in function.

global_variable = 10

def example_function():
    local_variable = 5
    print("Inside the function:")
    print("Local variable:", local_variable)
    print("Global variable:", global_variable)

example_function()

print("\nOutside the function:")
print("Global variable:", global_variable)


# WAP to show call by value and call by reference in python. 

def modify_value(x, y, lst):
    x = x + 1
    y.append(2)
    lst.append(4)

a = 5
b = [1, 2, 3]
c = [1, 2, 3]

print("Before function call:")
print("a:", a)
print("b:", b)
print("c:", c)

modify_value(a, b, c)

print("\nAfter function call:")
print("a:", a)
print("b:", b)
print("c:", c)


# Concatenate 3 dictionaries into a 4th one


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

concatenated_dict1 = dict1.copy()
concatenated_dict1.update(dict2)
concatenated_dict1.update(dict3)
print("Concatenated dictionary using update method:", concatenated_dict1)

concatenated_dict2 = {**dict1, **dict2, **dict3}
print("Concatenated dictionary using dictionary unpacking operator:", concatenated_dict2)


# WAP that involves 3 sets and performs various set operations such as union, intersection, symmetric difference, difference, super set & sub set.

a = {10, 20, 30, 40, 50, 60, 70}
b = {33, 44, 51, 10, 20, 50, 30, 33}
union_result = a.union(b)
print("A or B:", union_result)

intersection_result = a.intersection(b)
print("A and B:", intersection_result)

difference_result = a - b
print("A - B:", difference_result)

difference_result_b = b - a
print("B - A:", difference_result_b)

symmetric_difference_result = a.symmetric_difference(b)
print("A ^ B:", symmetric_difference_result)

is_subset = a.issuperset(b)
print("A >= B:", is_subset)

is_subset_b = a.issubset(b)
print("A <= B:", is_subset_b)


# 

print("Hello, World!")


#

num1 = 5
num2 = 3

bitwise_and_result = num1 & num2
print(f"Bitwise AND: {bitwise_and_result}")

bitwise_or_result = num1 | num2
print(f"Bitwise OR: {bitwise_or_result}")

bitwise_xor_result = num1 ^ num2
print(f"Bitwise XOR: {bitwise_xor_result}")

bitwise_not_num1 = ~num1
bitwise_not_num2 = ~num2
print(f"Bitwise NOT of {num1}: {bitwise_not_num1}")
print(f"Bitwise NOT of {num2}: {bitwise_not_num2}")

left_shift_result = num1 << 2
print(f"Left shift by 2 bits: {left_shift_result}")

right_shift_result = num2 >> 1
print(f"Right shift by 1 bit: {right_shift_result}")


#

amount = int(input("Enter the amount: "))

note1000 = note500 = note100 = 0

note1000 = amount // 1000
amount %= 1000

note500 = amount // 500
amount %= 500

note100 = amount // 100

print("Number of 1000 rupee notes:", note1000)
print("Number of 500 rupee notes:", note500)
print("Number of 100 rupee notes:", note100)

# 

import turtle
def draw_cell(x, y, text):
   turtle.penup()
   turtle.goto(x, y)
   turtle.pendown()
   turtle.write(text, align="center", font=("Arial", 12, "normal"))
def display_multiplication_table():
   turtle.speed(0.5)
   for i in range(1, 11):
       for j in range(1, 11):
           result = i * j
           x = j * 60 - 300
           y = 300 - i * 60
           draw_cell(x, y, result)
   turtle.done()
display_multiplication_table()


print("\n")

#

import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
cal = calendar.month(year, month)
print(f"Calendar for {calendar.month_name[month]} {year}:\n")
print(cal)
'''
#

# using Turtle Programming
# Star
import turtle 
for _ in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.done()

# square
import turtle
for i in range(4):
    turtle.back(50)
    turtle.left(90)
turtle.done()

# circle
import turtle
turtle.begin_fill()
turtle.color("blue")
turtle.circle(100)
turtle.end_fill()
turtle.done()

# display multiplication table from 1 to 10 using turtle in python
import turtle
def draw_cell(x, y, text):
   turtle.penup()
   turtle.goto(x, y)
   turtle.pendown()
   turtle.write(text, align="center", font=("Arial", 12, "normal"))
def display_multiplication_table():
   turtle.speed(0.5)
   for i in range(1, 11):
       for j in range(1, 11):
           result = i * j
           x = j * 60 - 300
           y = 300 - i * 60
           draw_cell(x, y, result)
   turtle.done()
display_multiplication_table()

# create bar chart
import turtle
def drawBar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
xs = [48, 117, 200, 240, 160, 260, 220]
maxheight = max(xs)
numbars = len(xs)
border = 10
wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
turtle.bgcolor("black")
tess = turtle.Turtle()
tess.color("white")
tess.fillcolor("green")
for a in xs:
    drawBar(tess, a)
wn.exitonclick()

# Create three sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

# Perform set operations
union_set = set1.union(set2, set3)
intersection_set = set1.intersection(set2, set3)
symmetric_difference_set = set1.symmetric_difference(set2).symmetric_difference(set3)
difference_set = set1.difference(set2).difference(set3)
super_set_check = set1.issuperset(set2) and set1.issuperset(set3)
sub_set_check = set1.issubset(set2) and set1.issubset(set3)

# Display results
print("\nSet 1:", set1)
print("Set 2:", set2)
print("Set 3:", set3)

print("\nUnion of Set 1, Set 2, and Set 3 :", union_set)
print("\nIntersection of Set 1, Set 2, and Set 3 :", intersection_set)
print("\nSymmetric Difference of Set 1, Set 2, and Set 3 :", symmetric_difference_set)
print("\nDifference of Set 1, Set 2, and Set 3 :", difference_set)

if super_set_check:
    print("Set 1 is a superset of Set 2 and Set 3")
else:
    print("\nSet 1 is not a superset of Set 2 and Set 3")

if sub_set_check:
    print("Set 1 is a subset of Set 2 and Set 3")
else:
    print("\nSet 1 is not a subset of Set 2 and Set 3")


print("\n")