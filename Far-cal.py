#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 05:54:09 2023

@author: anusharma
"""

# Convert temperature from Fahrenheit to Celsius
fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
celsius_temperature = (fahrenheit_temperature - 32) * 5/9

print(f"{fahrenheit_temperature} Fahrenheit is equal to {celsius_temperature} Celsius")