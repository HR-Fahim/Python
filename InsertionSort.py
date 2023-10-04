
value = [8,5,7,3,4,2,1]

for i in range(1, len(value)):
    key = value[i]
    j = i-1
    while j >= 0 and value[j] > key:
        value[j+1] = value[j]
        j -= 1
    value[j+1] = key
    print(value)