def boyer_moore_majority_voting_algorithm(A):

  candidate = None
  count = 0
  for a in A:
    if count == 0:
      candidate = a
      count = 1
    elif a == candidate:
      count += 1
    else:
      count -= 1

  if count > 0 and candidate in A:
    return candidate
  else:
    return None

A = [1, 2, 2, 2, 3, 2]

majority_element = boyer_moore_majority_voting_algorithm(A)

print(majority_element)
