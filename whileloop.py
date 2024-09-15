#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:31:47 2023

@author: anusharma
"""

i = 1
while i <= 10:
    print('6 *',i,'=',6*i)
    if i >= 5:
        break
    i = i+1
print("\n")
    
for i in range(5):
    if i <= 3:
        continue
    print(i)
    print("\n")
    
num = 0
while num<10:
    num += 1
    if(num%2)==0:
        continue
    print(num)