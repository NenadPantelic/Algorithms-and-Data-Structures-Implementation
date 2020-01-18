# Heap data structure

# O(n)
def max_heapify(array, i):
    '''
    array : list of numbers
    i : position of the element where we start heapification
    '''

    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array)

    largest = i
    if left < length and array[left] > array[i]:
        largest = left
        
    if right < length and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        max_heapify(array, largest)

# O(n)
def build_max_heap(array):
    half = (len(array) - 1) //2
    for i in range(half, -1, -1):
        max_heapify(array, i)
    

array = [1, 4, 3, 7, 8, 9, 10]
array2 = [4, 7, 8, 3, 2, 5, 6]

build_max_heap(array)
build_max_heap(array2)
#print(array)
#print(array2)

