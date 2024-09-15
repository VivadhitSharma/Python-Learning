# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""

The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and stops before a specified number.

range(start, stop, step)

start: Optional. An integer number specifying at which position to start. 
Default is 0

stop: Required. An integer number specifying at which position to stop 
(not included).

step: Optional. An integer number specifying the incrementation. Default is 1




"""

"""

Python while loop is used to run a block code until a certain condition is met

while condition:
    # body of while loop
    
A while loop evaluates the condition
If the condition evaluates to True, the code inside the while loop is executed.
condition is evaluated again.
This process continues until the condition is False.
When condition evaluates to False, the loop stops.


"""



i = 1
n = 5

while i <= n:
    print(i)
    i = i + 1


"""
INPUT A NUMBER AND FIND THE SUM OF NUMBERS TILL USER INPUTS 0

"""


total = 0

number = int(input('Enter a number: '))


while number != 0:
    total = total+ number    
    
    
    number = int(input('Enter a number: '))
    

print('total =', total)

"""

In Python, a while loop may have an optional else block.

Here, the else part is executed after the condition of the loop evaluates to False

"""

counter = 0

while counter < 3:
    print('Inside loop')
    #counter = counter + 1
else:
    print('Inside else')




count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1


"""
for val in sequence:
    # statement(s)
    
Python for Loop with Python range()

"""
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)

for i in range(6):
    print(i)

for i in range(2,6):
    print(i)

for i in range(1,20,3):
    #if i%2==0:
        print(i)

"""
Python for loop with else

A for loop can have an optional else block. 
The else part is executed when the loop is exhausted 
(after the loop iterates through every item of a sequence). 
The else block will not execute if the for loop is stopped by a break statement.
"""


num=int(input("enter a num"))

for i in range(1,num):
    p=2*i
    print(p)
    
"""
For loop programs:
To print sum of all even numbers in the given range
To print sum of all odd numbers in the given range
To count number of digits in a number

"""
count=0
num=str(988)
for i in num:
    count=count+1
print(count)


"""Check if given string is palindrome"""

s="madam"
rev=""
for i in s:
    rev=i+rev

print("reverse is",rev)

if(rev==s):
    print("its a palindrome")
else:
    print("its not")

"""Program to print reverse of a string"""


num = 153
num = str(num)
l = len(num)
 
# initialize a sum variable with
# 0 value to store the sum of the product of
# each digit
s = 0
 
# iterate through the given string
for i in num:
    s =s +  int(i)**l
 
if s == int(num):
    print("is an Amstrong number")
 
else:
    print("The given numberis Not an Amstrong number.")





"""
FACTORIAL OF a number using  loop
"""


number = int(input("Enter a number"))


fact = 1


if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        fact = fact*i

print(f"The factorial of {number} is {fact}")









""" validity of password"""




password = input("enter password")
 
has_valid_length = False
has_lower_case = False
has_upper_case = False
has_digits = False
has_special_characters = False
 
 
if (len(password) >= 8) and (len(password)<=16):
 
    has_valid_length = True
 
    for i in password:
 
        # check if there are lowercase alphabets
        if (i.islower()):
                has_lower_case = True                   
 
        # check if there are uppercase alphabets
        if (i.isupper()):
                has_upper_case = True                   
 
        # check if the password has digits
        if (i.isdigit()):
                has_digits = True                       
 
        
        if(i=="@" or i=="$" or i=="_"or i=="#" or i=="^" or i=="&" or i=="*"):
                has_special_characters = True           
 
 
if (has_valid_length==True and has_lower_case ==True and has_upper_case == True and has_digits == True and has_special_characters == True):
    print("Valid Password")
else:
        print("Invalid Password")

"""
sum of squares of a given number
"""

a=3
sos=0
for i in range(2,6):
    s=i*i
    sos=sos+s

print("sum of sq is",sos)


"""
display factors of a given number
"""
for i in range(1,10):
    if 10%i==0:
        print("the factor is ",i)

"""
alphabets:
    
ord() Python ord() function returns the Unicode code from a given character. 
This function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument.

print(ord('s'))
print(ord('2'))

The chr() method returns a string representing a character whose Unicode code point is an integer.

"""


"""

Random Module in Python:
Python Random module is an in-built module of Python that is used to 
generate random numbers in Python.

seed()	Initialize the random number generator

randrange()	Returns a random number within the range (exclusive of the endpoint)
randint()	Returns a random integer within the range ((inclusive of both endpoints))

"""

import random
#random.seed(3)
r1=random.randint(5,10)
print("random no between 1 and 5 is",r1)

r2=random.randint(10,17)
print("random no between 10 and 12 is",r2)

x=random.randrange(10,20)
print("random range is",x)


for a in range(65,91):
    print(chr(a), end=",")
    
    
B = '1101'
I = 0
while B != '':
     I = I * 2 + (ord(B[0]) - ord('0'))
     B = B[1:] 
print(I)
 

"""
Sum of digits using for loop
"""

number = int(input("Enter a positive integer: "))


if number < 0:
    print("Please enter a positive integer.")
else:
    
    dsum = 0

    # Convert the number to a string to iterate through its digits
    number_str = str(number)


    for i in number_str:
        digit = int(i)
        dsum += digit

    print(f"The sum of the digits of {number} is {dsum}")

   
"""

password guessing game
"""

correct_password = "password123"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    
    guess = input("Enter the password: ")

    if guess == correct_password:
        print("Congratulations! You've guessed the correct password.")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1

if attempts == max_attempts:
    print("Sorry, you've reached the maximum number of attempts. The correct password was:", correct_password)





"""
BREAK STATEMENT

The break statement in Python is used to terminate the loop or statement 
in which it is present. 
After that, the control will pass to the statements that are present after the 
break statement, if available. 
If the break statement is present in the nested loop, then it terminates only 
those loops which contain the break statement. 

for / while loop:
    # statement(s)
    if condition:
        break
    # statement(s)
# loop end
"""

for i in range(5):
    if i == 3:
        break
    print(i)


# program to find first 5 multiples of 6

i = 1

while i <= 10:
    print('6 * ', i , '=',6 * i)

    if i >= 5:
        break
    
    i = i + 1


i = 1

while i <= 10:
    

    if i >= 5:
        break
    print('6 * ', i , '=',6 * i)
    i = i + 1


"""
The continue statement is used to skip the current iteration of the loop and 
the control flow of the program goes to 
the next iteration.

"""
for i in range(5):
    print(i)
    if i == 3:
        continue
    
    
"""
PRINT odd NUUMBERS USING WHILE AND CONTINUE
"""
num = 0

while num < 10:
    
    
    if (num % 2) == 0:
        continue

    num+=1
    print(num)
    

"""
In Python programming, the pass statement 
is a null statement which can be used as a placeholder 
for future code.
"""
n = 9

# use pass inside if statement
if n > 10:
    pass

print('Hello')

"""
However, nothing happens when the pass is executed. 
It results in no operation (NOP).
Suppose we didn't use pass or just put a comment as:
    Here, we will get an error message: 
        IndentationError: expected an indented block

The difference between a comment and a pass statement in Python is 
that while the interpreter ignores a comment entirely
, pass is not ignored.
"""

n = 10

if n > 10:
    # write code later
    pass
print('Hello')


"""
For loop with else
else is Not executed when there is a break
"""

for i in range(1, 4): 
    if i==3:
         
        break
    print(i)
else:  
	print("No Break") 

#in case there is no break
for i in range(1, 4): 
    
        print(i)
else:  
	print("No Break") 




"""
unique combinations of 1 2 3
"""

i=1
while i<=3:
    j=1
    while j<=3:
        k=1
        while k<=3:
            if i==1 or j==k or k==i:
                k=k+1
                continue
            else:
                print(i,j,k)
            k=k+1
        j=j+1
    i=i+1
    



"""
pattern

1
22
333
4444
55555
"""
rows = 6
for num in range(6):
    
    for i in range(num):
        
        print(num, end=" ") 
    print(" ")

"""
11111
2222
333
44
5
"""
rows = 5
b = 0
for i in range(5, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(i, end=' ')
    print('\r')


    
for i in range(0,5,1):
    print(i)

for i in range(5,0,-1):
    print(i)
    
for i in range(-5,0,1):
    print(i)

for i in range(0,-5,-1):
    print(i)
    
"""
Full pyramid
        *
      * * *
    * * * * *
  * * * * * * *

"""
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(65 + k), end='')
    print()
    
"""
reverse pyramid pattern
"""    

n = 5

for i in range(n):
    
    for j in range(i):
        print(' ', end='')
    
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()    
    
  
"""
1
2 3
4 5 6
7 8 9 10
"""
rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()

"""
Nested loops
"""


for sec in range(60):
    print(sec)


for minutes in range(60):
    for sec in range(60):
        print(minutes," : ",sec)


for hours in range(24):
    for minutes in range(60):
        for sec in range(60):
            print(hours, " : ", minutes," : ",sec)


size = 5

for i in range(5):
    for j in range(i):
        print(chr(64 + i), end=" ")
    print()

for i in range(5):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()



"""
1. Print sum of every 5th number from 0 to 20 using loops.
2. print pattern
3. Ask user for password. If it user types the correct password i.e "Python", display
welcome else display "incorrect password"
4.  using loop find the sum of following series:(Hint: input x and number of terms from user)
    1+x+x^2+x^3+.....

5. what is the error in following:


count=0
s=0
while count<10:
s+=count
    count=count+1
    print(s)
    
    
predict the output/detect the error
count=0
for i in range(10,0,-1):
    print(i)
"""

start = 0
end = 20
step = 5
sum_of_every_5th = 0

while start <= end:
    sum_of_every_5th += start
    start += step

print("Sum of every 5th number from 0 to 20:", sum_of_every_5th)
 
    
 
x = float(input("Enter the value of x: "))
terms = int(input("Enter the number of terms to sum: "))

sum_series = 0
term = 1
count = 0

while count < terms:
    sum_series += term
    term *= x
    count += 1

print(f"The sum of the series 1 + x + x^2 + x^3 + ... for {terms} terms is {sum_series}")


