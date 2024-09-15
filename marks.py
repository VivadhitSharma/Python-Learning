#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:40:29 2023

@author: anusharma
"""

#write a program to get a number of students in the class also input the number of subjects per students. calculate average marks for each students.
def calculate_average_marks(num_students, num_subjects):
    for student in range(1, num_students + 1):
        total_marks = 0

        for subject in range(1, num_subjects + 1):
            marks = float(input(f"Enter marks for Student {student}, Subject {subject}: "))
            total_marks += marks

        average_marks = total_marks / num_subjects
        print(f"Average marks for Student {student}: {average_marks:.2f}")

if __name__ == "__main__":
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects per student: "))

    calculate_average_marks(num_students, num_subjects)