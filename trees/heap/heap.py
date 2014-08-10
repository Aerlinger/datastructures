heap_array = [16, 15, 10, 8, 7, 9, 3, 2, 4, 1]

def parent(index):
  return index/2


def left(index):
  return 2 * index

def right(index):
  return 2 * index + 1

def max_heapify(array, i):
  l  = left(i)
  r = right(i)

  # Guard
  if l <= len(array) and array[l] > array[i]:
    largest = l
  else:
    largest = i

  if r <= len(array) and array[r] > array[largest]:
    largest = r

  if largest != i:
    print("Index " + str(i) + " is out of order!")
    temp = array[largest]
    array[largest] = array[i]
    array[i] = temp
    max_heapify(array, i)


oo_array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

max_heapify(oo_array, 1)

print oo_array

