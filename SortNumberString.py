import re

def sort_expression(expression):
    # Find all numbers in the expression
    numbers = re.findall(r'\d+', expression)
    
    # Sort the numbers
    sorted_numbers = sorted(map(int, numbers))
    
    # Replace the original numbers in the expression with sorted numbers
    sorted_expression = re.sub(r'\d+', lambda x: str(sorted_numbers.pop(0)), expression)
    
    return sorted_expression

input_expression = input()
sorted_expression = sort_expression(input_expression)
print(sorted_expression)

# Input: "1+3+2"
# Output: "1+2+3"