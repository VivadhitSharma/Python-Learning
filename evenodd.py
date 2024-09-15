#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:59:50 2023

@author: anusharma
"""

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("it is Even", num)
else:
   print("{0} is Odd".format(num))

   #print(f"{num} is odd")
   #print("%s is odd"%(num))