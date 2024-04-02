
def merge_sort(list):
    size = len(list)
    if size > 1:
        mid = size // 2
        a = list[:mid]
        b = list[mid:]
        a = merge_sort(a)  # Recursively sort the first half
        b = merge_sort(b)  # Recursively sort the second half
        i = j = k = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                list[k] = a[i]
                i += 1
            else:
                list[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            list[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            list[k] = b[j]
            j += 1
            k += 1
    return list

list = [8, 6, 4, 7, 2, 6, 9, 1]
sorted_list = merge_sort(list)

#Print Answers
print(sorted_list)
