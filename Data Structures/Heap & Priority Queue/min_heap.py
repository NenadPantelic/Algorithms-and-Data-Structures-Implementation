# Min heap

def min_heapify(array, i):
    '''
    array : list of numbers
    i : position of the element where we start heapification
    '''

    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array)

    smallest = i
    if left < length and array[left] < array[i]:
        largest = left
        
    if right < length and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[smallest], array[i] = array[i], array[smallest]
        min_heapify(array, smallest)

def build_min_heap(array):
    half = (len(array)-1)//2
    for i in range(half, -1, -1):
        min_heapify(array, i)
    

array = [4, 5, 1, 6, 7, 3, 2]
array2 = [4, 7, 8, 3, 2, 5, 6]

build_min_heap(array)
build_min_heap(array2)
print(array)
print(array2)

