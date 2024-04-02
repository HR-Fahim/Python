# Define a function that takes another function `f` as an argument
def reversed_args(f):
    # Return a new function that accepts any number of arguments
    return lambda *args : f(*args[::-1])

from typing import Dict, Any, Callable, Tuple

# Define a dictionary that maps function names to built-in functions
int_func_map: Dict[str, Callable[..., Any]] = {
    'pow': pow,
    'cmp': cmp,
}

# Define a dictionary that maps function names to lambda functions
string_func_map: Dict[str, Callable[..., Any]] = {
    'join_with': lambda separator, *args: separator.join(args),
    'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
}

# Read the number of queries from the user
queries: int = int(input())

# Iterate over the range of queries
for _ in range(queries):
    # Read a line of input and split it into a list of strings
    line: List[str] = input().split()
    # Extract the function name and arguments from the line
    func_name: str = line[0]
    args: Tuple[str] = tuple(line[1:])

    # Check if the function name is in the int_func_map dictionary
    if func_name in int_func_map:
        # Convert the arguments to integers
        args = tuple(map(int, args))
        # Call the reversed function with the corresponding built-in function from the int_func_map dictionary,
        # passing in the reversed arguments, and print the result
        print(reversed(int_func_map[func_name])(*args))
    else:
        # Call the reversed function with the corresponding lambda function from the string_func_map dictionary,
        # passing in the reversed arguments, and print the result
        print(reversed(string_func_map[func_name])(*args))

