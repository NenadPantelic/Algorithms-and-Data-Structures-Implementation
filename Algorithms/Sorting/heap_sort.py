# Heap sort O(nlog(n))
# O(n)
def max_heapify(array, length, i):
    '''
    array : list of numbers
    i : position of the element where we start heapification
    '''

    left = 2 * i + 1
    right = 2 * i + 2

    largest = i
    if left < length and array[left] > array[i]:
        largest = left
        
    if right < length and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        max_heapify(array, length, largest)

# O(n)
def build_max_heap(array):
    half = (len(array) - 1) //2
    for i in range(half, -1, -1):
        max_heapify(array, len(array), i)
    
def heap_sort(array):
    #heap_size = len(array)
    build_max_heap(array)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        #heap_size = heap_size - 1
        max_heapify(array, i, 0)

array = [4,3,7,1,8,5]
heap_sort(array)
print(array)
