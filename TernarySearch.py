def ternary_search(array, key):
  low = 0
  high = len(array) - 1

  while low <= high:
    mid1 = (low + high) // 3
    mid2 = (2 * low + high) // 3

    if array[mid1] == key:
      return mid1
    elif array[mid2] == key:
      return mid2
    elif key < array[mid1]:
      high = mid1 - 1
    elif key < array[mid2]:
      low = mid1 + 1
    else:
      high = mid2 - 1

  return -1

array = [1, 3, 5, 7, 9]
key = 5

index = ternary_search(array, key)

if index >= 0:
  print("The key is found at index:", index)
