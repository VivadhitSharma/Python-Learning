#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:37:06 2023

@author: anusharma
"""

a = (input("Enter any alphabet"))
if(a=="a" or a=="e" or a=="i" or a=="o" or a=="u"):
    print("{0} is vowel".format(a))
else:
    print(f"{a} is consonant")
    
'''
a = (input("Enter any alphabet"))
if i in 'AEIOUaeiou':
    print("{0} is vowel".format(a))
else:
    print("{0} is consonant".format(a))

'''