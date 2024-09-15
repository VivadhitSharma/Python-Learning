#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:32:20 2023

@author: anusharma
"""
a = int(input("Enter first number"))
if(a>=0 and a<=33):
    print("fail")
elif(a>=33 and a<=60):
        print("third grade")
elif(a>=60 and a<=80):
    print("second grade")
elif(a>=80 and a<=100):
    print("first grade")
else:
    print("invalid")
