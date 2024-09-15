#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 02:29:27 2023

@author: anusharma
"""

height = float(input("enter height in meter"))
weight = float(input("enter weight in kgs"))
bmi = weight/(height**2)
print(f"{bmi} is bmi")
if(bmi<16):
    print("underweight")
elif(bmi>=16 and bmi<=25):
    print("normal")
elif(bmi>=25):
    print("obese")
else:
    print("invalid")