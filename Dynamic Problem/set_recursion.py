def count_sets(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return 8
    
    # Initialize the dp array to store results
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    f[2] = 2
    f[3] = 4
    f[4] = 8

    # Compute the values for all widths from 5 to n
    for i in range(5, n + 1):
        f[i] = f[i-1] + f[i-2] + f[i-3] + f[i-4]

    return f[n]

# Example: Calculate for width 5
width = 9
result = count_sets(width)
print(f"The number of sets for width {width} is {result}")
