#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 05:54:05 2023

@author: anusharma
"""

# Calculate Simple Interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"The Simple Interest is: {simple_interest}")

#print("The Simple Interest is:",simple_interest)