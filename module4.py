"""
Module4.py is the homework for module 4 Assignment 4.2.

This module contains the following program:

The program asks the user for input N (positive integer) and reads it. Then the program
asks the user to provide N numbers (one by one) and reads all of them (again, one by one).
In the end, the program asks the user for input X (integer) and outputs: "-1" if there
were no such X among N read numbers, or the index (from 1 to N) of this X if the user
inputed it before.

Author:  Wei Du
Date:   10/28/2023
"""

# Ask the user for input N (positive integer)
N = int(input("Enter the number of elements: "))
numbers = []

# Read N numbers from the user and store them in a list
for i in range(N):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

# Ask the user for input X (integer)
X = int(input("Enter the number X to search for: "))

# Check if X exists among the entered numbers
found = False
for i in range(N):
    if numbers[i] == X:
        print("Index of {} is: {}".format(X, i + 1))
        found = True
        break

# If X is not found, output -1
if not found:
    print("-1")

