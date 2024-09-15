# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:37:53 2023

@author: Asus
"""

"""
In Python, a lambda function is a special type of function 
without the function name. For example,

lambda : print('Hello World')

Syntax: 
lambda argument(s) : expression 


argument(s) - any value passed to the lambda function
expression - expression is executed and returned


This function can have any number of arguments but only one 
expression, 
which is evaluated and returned.
One is free to use lambda functions wherever function objects 
are required.
You need to keep in your knowledge that lambda functions are 
syntactically 
restricted to a single expression.
It has various uses in particular fields of programming, 
besides other types of expressions in functions

"""
greet = lambda : print('Hello World')

greet()

"""
lambda function with arguments
"""
greet_user = lambda name : print('Hey there,', name)

# lambda call
name=input("enter your name")
greet_user(name)


s= lambda a,b: print("sum is",a+b)

s(2,3)


### Convert given string to upper case using lambda function
univ="amity university"

uc=lambda a:a.upper()

uc(univ)

univ="amity university"

capcase=lambda s:s.capitalize()
titlecase=lambda s:s.title()
capcase(univ)
titlecase(univ)


############## Lambda function with 2 arguments

m=lambda a,b: "true" if (a>b) else "not true"


m(7,4)



def sofnums(a,b):
    print(a+b)

sofnums(3,4)



def find_sq(num):
    result=num*num
    return result

s=find_sq(6)
print("square is",s)

"""
sum of numbers in list
"""
def sumnums(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

nums=[8,2,3,0,7]
print(sumnums(nums))

"""
Global keyword
keyword allows us to modify the variable outside 
of the current scope.

It is used to create a global variable and make 
changes to the variable in a local contex
"""
c=10 # c here is a global variable

def changec():
    print(c)

changec()

"""
How to change a global variable from inside a function
"""

d=10

def changed():
    d=d+100 # UnboundLocalError
    print(d)

changed()

"""
This is because we can only access the global 
variable but cannot modify it from inside the 
function
"""
d=100
def changed():
    global d
    d=d+100 
    print(d)

changed()



"""
in nested functions
"""
def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

outer_function()
print("Outside both function: ", num)
