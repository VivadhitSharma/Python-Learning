#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 04:08:35 2023

@author: anusharma
"""

# Calculate profit percentage
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print(f"The profit earned is: {profit}")
    print(f"The profit percentage is: {profit_percentage}%")
else:
    print("No profit earned.")