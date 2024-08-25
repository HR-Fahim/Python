#!/bin/python3

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    MOD = 10**9 + 7
    
    # Special case: if height is 1, return 0 if width > 4, otherwise return 1
    if n == 1:
        return 0 if m > 4 else 1

    # Array to store number of ways to build a row of width i
    row_ways = [0, 1, 2, 4, 8]

    # Calculate number of ways to build a row of width up to m
    for _ in range(5, m + 1):
        row_ways.append((row_ways[-1] + row_ways[-2] + row_ways[-3] + row_ways[-4]) % MOD)

    print(row_ways) # Debugging

    # Compute pn values: number of ways to build n rows with width k
    pn = [pow(width, n, MOD) for width in row_ways]

    # Compute gn values: number of ways to build a solid wall of width k
    good_configurations = [0, 1]
    for width in range(2, m + 1):
        # Compute sum of bad configurations
        bad_sum = sum(good_configurations[i] * pn[width - i] for i in range(1, width)) % MOD
        # Compute the number of good configurations
        good_configurations.append((pn[width] - bad_sum + MOD) % MOD)

    return good_configurations[m]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

    #     fptr.write(str(result) + '\n')

        print(result)

    # fptr.close()
