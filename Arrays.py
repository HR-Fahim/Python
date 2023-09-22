#!/bin/python3

# Importing necessary modules
import math
import os
import random
import re
import sys

# Main function
if __name__ == '__main__':
    # Getting input from the user and storing it in 'n'
    n = int(input().strip())

    # Getting input from the user, splitting it into a list of integers, and storing it in 'arr'
    
    arr = list(map(int, input().rstrip().split())) # Splitting the input into a list of integers

    # Defining the delimiter for joining the reversed 'arr'
    delimiter = " "

    # Reversing the 'arr', converting each integer to a string, joining them with the delimiter, and printing the result
    print(delimiter.join(map(str, arr[::-1])))


# Input: 4
#        1 4 3 2
# Output: 2 3 4 1