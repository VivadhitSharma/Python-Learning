# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:52:22 2023

@author: Asus
"""

"""
The difference between the two is that we cannot
 change the 
elements of a tuple once it is assigned whereas
 we can 
change the elements of a list.

A tuple can have any number of items and they 
may be of 
different types (integer, float, list, string, 
                 etc.).
"""
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)



name="universe is huge"
t=tuple(name)
print(t)


# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

print(my_tuple[0])
my_tuple[0]=100
# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

print(my_tuple[1])
print(my_tuple[1][0])


my_tuple = 1, 2, 3
my_tuple = 1, "Hello", 3.4
print(my_tuple)

#following code results in TypeError

my_tuple[0]="silky"
print(my_tuple[1])
print(my_tuple[1][0])

"""
Find the size of a Tuple in Python
"""
import sys

# sample Tuples
Tuple1 = ("A", 1, "B", 2, "C", 3)

Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

s1=sys.getsizeof(Tuple3[1][1])
print("Size of Tuple1: ",s1)
# print the sizes of sample Tuples
print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")

print("Size of Tuple3: " + str(sys.getsizeof(Tuple3[0][1])) + "bytes")



print(len(Tuple1))
print(len(Tuple3))

"""
Create a Python Tuple With one Element
"""



var1 = ("Hello") # string
var2 = ("Hello",) # tuple


"""
Accessing tuple elements
"""

t1=([1,2,3],["apple","banana"])
t1[0][0]=9
print(t1)

t1=([1,2,3],["apple","banana"])
t1[0]=[9,9,9]
print(t1)

t=(10,20,30)
for a in t:
    print (a)
    
    
records=(('priyanka',12),('neha',22),('Tina',200))

for n, a in records:
    print(n,a)

for n in records:
    print(n)



records=(['priyanka',12],['neha',22],['Tina',200])

for x,y in records:
    print(x,y)

"""
negative indexing
"""
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-1])   # prints 'z' 
print(letters[-3])   # prints 'm'

# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')

# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')

# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')


a = ("MNNIT Allahabad", 5000, "Engineering") 

(college, student, type_ofcollege) = a 

print(college)

print(student)

print(type_ofcollege)

"""
tuple methods
In Python ,methods that add items or remove items
 are not available with tuple. Only the following 
 two methods are available.


"""
my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3


# Tuple packing and unpacking
person = ('John', 25, 'New York')
name, age, city = person
print(name)  # Output: 'John'
print(age)   # Output: 25
print(city)  # Output: 'New York'



# Concatenating tuples
fruits1 = ('apple', 'banana')
fruits2 = ('cherry', 'date')
all_fruits = fruits1 + fruits2
print(all_fruits)

languages = ('Python', 'Swift', 'C++')

# iterating through the tuple
for language in languages:
    print(language)
    


languages = ('Python', 'Swift', 'C++')

print('C' in languages)    # False
print('Python' in languages)    # True


t1=(100,200,300)
print(max(t1))

print(sum(t1))

"""
when strings are elements of tuples
The max() and min() functions can be used with 
tuples, and they operate based on 
lexicographical order. 
"""
t2=("welcome","to","amity")
print(max(t2))
print(min(t2))

print(sum(t2))

t3=("100","2","10")
print(max(t3))
print(min(t3))




"""
zip function
The zip() function takes iterables
 (can be zero or more), aggregates them in a 
 tuple, and returns it.
"""
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)

combined = zip(tuple1, tuple2, tuple3)
result = tuple(map(sum, combined))
print(result) 


result = map(sum, combined)
print(tuple(result)) 



list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined = zip(list1, list2, list3)
result = tuple(map(sum, combined))
print(result) 

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
	return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(tuple(result))


l1=[1,2,3]
l2=[4,5]
l3=zip(l1,l2)


for x in l3:
    print(x)
print(list(l3))