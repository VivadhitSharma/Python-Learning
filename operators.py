#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:47:16 2023

@author: anusharma
"""

a = int(input("Enter first number"))
b = int(input("Enter second number"))
o = str(input("which operation you want to perform"))
if (o == "+"):
    print(a+b)
elif (o == "-"):
    print(a-b)
elif (o == "*"):
    print(a*b)
elif (o == "/"):
    if b != 0:
        print(a/b)
    else:
        print("division by zero is not allowed")
else:
    print("invalid operator")
    
    