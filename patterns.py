#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 00:12:22 2023

@author: anusharma
"""
# Trangle
size = 6
m = (size * 2) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=(" "))
    m = m - 1
    for j in range(0, i + 1):
        print("*", end=(" "))
    print(" ")
print("\n")

# down to up
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=(" "))
    print("")
print("\n")

# square
for i in range(5):
    for j in range(9):
        print("*", end=" ")
    print("")
print("\n")

# up to down
for i in range(1, 5):
    for j in range(i):
        print("*", end=(" "))
    print("")


''' WAP to print the following star pattern.
      *
    *** 
  *****
******* '''

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        
        # Move to the next line after each row
        print()

# Set the number of rows for the pattern
rows = 4  # You can adjust this value to change the size of the pattern

# Call the function to print the star pattern
print_star_pattern(rows)

