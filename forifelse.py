#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:50:36 2023

@author: anusharma
"""
#break
for i in range (1, 4): 
    if i==3:
        break;
    print(i)
else:
    print("inside else")
#for else 
for i in range (1, 4): 
    if i==3:
        print(i)
else:




    print("inside else",)   
#if else
for i in range (1, 4): 
    if i==3:
        print(i)
    else:
        print("inside else",i)
print("\n")

name=("university",(1,2,3),('a','b'))
print(tuple(name))      

print("\n")

name=("university")
print(tuple(name)) 
