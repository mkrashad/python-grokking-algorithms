def binary_search(myList, item):
  low = 0
  high = len(myList) - 1
  
  while low <= high:
    mid = (low + high) / 2
    guess = myList[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid  + 1
  return None


example = [1, 3, 5, 7, 9]
print(binary_search(example, 9))

  