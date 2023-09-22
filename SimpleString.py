# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input().strip()) 
for i in range(1, n+1):
    s = input()
    print(s[::2], s[1::2])