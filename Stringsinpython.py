# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:36:45 2023

@author: Asus
"""

name="Bill Clinton"
for ch in name:
    print(ch,end="")
    

"""
In the below example: ch variable references 
a copy of character from the given string
as loop iterates.if we change the value that ch references to 
in the loop
it has no effect on the name string.


Note: Python does not have a separate character type. 
Instead an expression like s[8] returns a 
string-length-1 containing the character. 
"""    
name="Bill Clinton"
for ch in name:
    ch="X"
    
print(name)


"""
STRING IN PYTHON IS IMMUTABLE
"""
name="USA"
print(name[0])

name[0]="P" #'str' object does not support item assignment 
#which shows that String is immutable





"""
count t in given string
"""
name ="Tommy clinton"
count=0
for ch in name:
    if ch=='t' or ch=='T':
        count=count+1
print("number of t is", count)



"""
String comparison using <, >, == , !=, >=, <=
Python compares strings by comparing the characters
"""
x="abc"
y="ABCD"
print(x<y) 

x="tiger"
y="Tiger"
print(x==y)


"""
string indexing
"""
name="Bill Clinton"
print(name[9])
print(name[len(name)-2])
print(name[-1])

"""
len function
"""
language="Python"

# compute the length of languages
length = len(language)
print(length)

city="Boston in USA"
i=0
while i<len(city):
    print(city[i],end="")
    i+=1

# built in functions min and max

print(min("string"))
print(max("string"))



"""
TRAVERSAL USING for AND WHILE loop
"""
S="Maldives"
for ch in S:
    print(ch, end="")

#To print every second character
for ch in range(0,len(S),2):
    print(S[ch], end="")
    



"""
String concatenation using + and +=
Since Python string is immutable, the 
concatenation always results in a new string.
can be proved using id function on the variable
"""


name="carmen"+"brown"
print(name)

name="carmen"
name+="brown"
print(name)

name="carmen"
print((name))
name+="brown"
print(id(name))
print(name)


s = 'hi'
print(s[1])          
print(len(s))        
print(s + ' there')  
print(s)

pi = 3.14

text = 'The value of pi is '  + str(pi) 

text = 'The value of pi is '  + pi 
print(text)
"""
string concatenation using 
String objects have the built-in % operator that allows 
you to format strings. 
Also, you can use it to concatenate strings. For example
"""
s1, s2, s3 = 'Python', 'String', 'Concatenation'
a = '%s %s %s' % (s1, s2, s3)
print(a)


s1, s2, s3 = 'Python', 'String', 'Concatenation'
s = '{} {} {}'.format(s1, s2, s3)
print(s)

s1, s2, s3 = 'Python', 'String', 'Concatenation'
s = f'{s1} {s2} {s3}'
print(s)



"""
string formatting
1. using % operator
"""
name = "John"
print("Hello, %s!" % name)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

print("%s is %d years old." % (age, name))


x = 'looked'

print("Misha %s and %s around"%('walked',x))


"""
Floating-point numbers use the format %a.bf. 
Here, a would be the minimum number of digits to be present in the string; 
these might be padded with white space if the whole number doesn’t have this 
many digits. 
bf represents how many digits are to be displayed after the decimal point. 
"""
print('The value of pi is: %5.4f' %(3.141522))

print('The value of pi is: %6.4f' %(3.141552))

print('The value of pi is: %5.f' %(3.14))

variable = 12
string = "Variable as integer = %d Variable as float = %f" %(variable, variable)
print (string)

"""
2. using format method()

Formatters work by putting in one or more replacement fields and 
placeholders defined by a pair of curly braces { } into a string and 
calling the str.format().

"""
print('We {} all are .'.format('equal'))

print('We all are {} and {}.'.format('equal','same'))

print('We all are {} and {}.'.format('equal'))

#INDEXED PLACEHOLDERS
print('{2} {1} {0}'.format('directions', 'the', 'Read'))

#NAMED PLACEHOLDERS
print('a: {a}, b: {b}, c: {c}'.format(a = 1,b = 'Two',c = 12.3))

print('The first {p} was alright, but the {p} {p} was tough.'.format(p='second'))

print('The first {p} was alright, but the {q} was tough.'.format(p='second',q='third'))



print('The valueof pi is: %1.5f' %3.141592)
print('The valueof pi is: {0:1.5f}'.format(3.141592))


"""
3. python fstring

Literal String Interpolation or more commonly as F-strings 
(because of the leading f character preceding the string literal). 
The idea behind f-String in Python is to make string 
interpolation simpler
"""
name = 'payal'
print(f"My name is {name}.")

a = 5
b = 10
print(f"He said his age is {2 * (a + b)}.")

#lambda function in fstring
print(f"He said his age is {(lambda x: x*2)(3)}")

num = 3.14159
#Syntax: {value:{width}.{precision}}
print(f"The valueof pi is: {num:{6}.{5}}")

"""
f-strings are faster and better than both %-formatting 
and str.format(). 
f-strings expressions are evaluated at runtime, 
and we can also embed expressions inside f-string, 
using a very simple and easy syntax. 
The expressions inside the braces are evaluated in runtime and 
then 
put together with the string part of the f-string and then 
the final string is returned.
"""


"""
raw string

The "print" function normally prints out one or more python 
items followed by a newline. 
A "raw" string literal is prefixed by an 'r' and passes 
all the chars through 
without special treatment of backslashes, 
so r'x\nx' evaluates to the length-4

"""
raw = r'this\t and that'
print(raw)

not_raw='this\t and that'
print(not_raw)



"""
String methods:

s.lower(), s.upper() -- returns the lowercase or uppercase 
version of the string

s.strip() -- returns a string with whitespace removed from the start 
and end

s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes

s.startswith('other'), s.endswith('other') -- tests if the string starts 
or ends with the given other string

s.find('other') -- searches for the given 
other string (not a regular expression) within s, 
and returns the first index where it begins or -1 if not found

s.replace('old', 'new') -- returns a string where all occurrences of 'old'
 have been replaced by 'new'

s.split('delim') -- returns a list of substrings separated by the 
given delimiter. The delimiter is not a regular expression, 
it's just text. 

'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. 
As a convenient special case s.split() (with no arguments) 
splits on all whitespace chars    
"""


"""
isalpha()

True if all characters in the string are alphabets 
(can be both lowercase and uppercase).
False if at least one character is not alphabet.
"""

print("silky sachar".isalpha())

print("silky17".isalpha())

name = "MonicaGeller"

if name.isalpha() == True:
   print("All characters are alphabets")
else:
    print("All characters are not alphabets.")
    
    
"""
The isdigit() method returns True if all characters in a string 
are digits. 
If not, it returns False.
note: digit can also be decimal
"""    

str1 = '342'
print(str1.isdigit())

str2 = 'python 3'
print(str2.isdigit())

str3='3.5000'
print(str3.isdigit()) #false

"""
The isalnum() method returns True if all characters in the 
string are alphanumeric (either alphabets or numbers). 
If not, it returns False.
"""
# string contains either alphabet or number 
name1 = "Python3"

print(name1.isalnum()) 

name2 = "Python 3"

print(name2.isalnum()) #False

name3="7777"
print(name3.isalnum())

name4='inthisuniverse'
print(name4.isalnum())

name5="@mit"
print(name5.isalnum())





"""

"""


"""
String slicing

we can use the : (colon) operator in Python to access the 
substring from the given string.

Slicing can be achieved in two basic forms.

SEQUENCE [START: STOP]
The first form is to provide start and stop index parameters 
of a sequence. 
By doing so, the sequence would return all possible items 
between the start of the sequence and the 
stop [end -1] of the sequence.


SEQUENCE [START: STOP: STEP]
The second method is to provide the sequence’s start and stop 
index parameters along with the step. 
A step enables the return of specific or selected items 
within a range of items between the start and stop.

"""
s="HELLO"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])


print(s[0:2]) #HE

print(s[1:2]) #E

print(s[:3]) #HEL

print(s[2:]) #HELLO

print(s[:]) #HELLO

print(s[::2])
print(s[::3])

print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])

print(s[-1:-3]) #LL

print(s[-4:])

print(s[::-1]) ## reversing the given string


S="IIT-MADRAS"
print(S[-1::-1])

print(S[-1:0:-1])

print(S[-1:2:-1])

print(S[-1:2:1])

"""
deleting the string
"""
s="moon and stars"

del s[0]
print(s) #'str' object doesn't support item deletion

#deletes entire string
s="moon and stars"
del s
print(s)

"""
string operations

operators:
+, *, [], [:], in, not in, r/R,  %
"""
s1 = "Hello"     
s2 = " world"

"""
It is known as repetition operator. It concatenates the multiple copies of the same string.
"""    
print(s1*3)  

print('w' in s1)     

print('wo' not in s2)    
 
print("The string str : %s"%(s1)) 

"""
string formatting
"""
print("what's going on")

print('they said, "what\'s up"')

#\newline escape sequence that ignores the new line
print("Python1 \
Python2 \
Python3")


# \\ backslash

print("\\")

print("C:\user\dev\local")
print("C:\\users\\dev\\local")


"""
some more python methods
"""

  
S="IIT-MADRAS"
print(S[-1::-1])


"""
given 2 words. print all letters common to both
"""
word1="USA south america"
word2="USA north america"

for l in word1:
    if l in word2:
        print(l,end="")


"""
accept multiple inputs in a line and print them individually

The split() method splits a string into a list.

You can specify the separator, default separator is any whitespace.
"""
a, b= input("Enter full name ").split(".")
print("Enter Your First Name: ", a)
print("Enter Your Last Name: ", b)

print()

nums=[100,200,300]
print(min(nums))

nums=[100,200,300]
print(max(nums))

nums=[100,200,300]
print(sum(nums))

nums=[100,200,300]
print(len(nums))

names=["app","zenia","canada"]
print(min(names))

nums=[100,200,300]
print(max(nums))

nums=[100,200,300]
print(sum(nums))


i=2
j=3,2
add=i+j
print(add)