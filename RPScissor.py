#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 01:16:36 2023

@author: anusharma
"""
a = input("Enter player one")
b = input("Enter player two")
if(a==b):
    print("tie")
elif(a=="rock" and b=="scissor") or (a=="paper" and b=="rock") or (a=="scissor" and b=="paper"):
        print("{0} wins ".format(a))
elif(a=="rock" and b=="paper") or (a=="paper" and b=="scissor") or (a=="scissor" and b=="rock"):
        print("{0} wins".format(b))
else:
    print("Invalid")