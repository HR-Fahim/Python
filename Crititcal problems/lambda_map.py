# Define a function called lambdaMap that takes in an argument called arr
def lambdaMap(arr):
    # Use the map function to apply a lambda function to each element in arr
    # The lambda function takes an element i and returns a list of squares of positive numbers in i
    # If i is not a list, the lambda function returns i itself
    ans = map(lambda i: [n**2 for n in i if n > 0] if isinstance(i, list) else i, arr)

    # Return the result of the map function
    return ans

# If this module is run directly
if __name__ == '__main__':
    # Read an integer from input and assign it to variable n
    n = int(raw_input())

    # Initialize an empty list called arr
    arr = []

    # Repeat the following steps n times
    for _ in range(n):
        # Read a space-separated list of integers from input, convert each element to int, and append the resulting list to arr
        arr.append(list(map(int, raw_input().split())))

    # Call the lambdaMap function with arr as the argument and assign the result to variable ans
    ans = lambdaMap(arr)

    # For each row in ans
    for row in ans:
        # Print the elements of row separated by a space
        print(' '.join(map(str, row)))
