
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip()) 
    for i in range(1, 11): # 1 to 10 times table. Here 11 is the number of rows.
        print(n, 'x', i, '=', n*i)