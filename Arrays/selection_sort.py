def selection_sort(array):
  for i in range(len(array) - 1):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]
  return array

array=[2,13,4,1,3,6,28]
print(selection_sort(array))