#!/bin/python3

# Import necessary modules
import math
import os
import random
import re
import sys

# Define a decorator function called log
def log(descriptor):
    # Implement the decorator here
    def decorator(func):
        # Define a wrapper function that logs function name and input arguments
        def wrapper(*args, **kwargs):
            # Convert input arguments to string without spaces
            args_str = ', '.join(str(arg) for arg in args)
            args_str = args_str.replace(", ", ",")

            # Write log message to the descriptor
            descriptor.write(f"LOG: {func.__name__}({args_str})\n")

            # Call the original function and return its result
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Check if this script is being executed as the main script
if __name__ == '__main__':
    # Open a file for writing the output
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Decorate the my_max function with the log decorator
    @log(fptr)
    def my_max(a, b, c):
        return max(a, b, c)

    # Decorate the my_min function with the log decorator
    @log(fptr)
    def my_min(a, b):
        return min(a, b)

    # Decorate the my_sum function with the log decorator
    @log(fptr)
    def my_sum(*args):
        return sum(args)

    # Read the number of queries
    q = int(input())

    # Process each query
    for _ in range(q):
        # Read the query line
        line = input().split()
        f_name, params = line[0], map(int, line[1:])

        # Check the function name and call the corresponding function
        if f_name == "my_min":
            res = my_min(*params)
            fptr.write(f"{res}\n")
        elif f_name == "my_max":
            res = my_max(*params)
            fptr.write(f"{res}\n")
        elif f_name == "my_sum":
            res = my_sum(*params)
            fptr.write(f"{res}\n")
        else:
            raise ValueError("Unknown function name %s" % f_name)

    # Close the output file
    fptr.close()
