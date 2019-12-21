# Quicksort(O(nlog(n))

# version 1 - pivot = the first element
    
def quick_sort(array, low, high):
    #if high == low
    if low >= high:
        return 
    pivot = partition(array, low, high)
    quick_sort(array, low, pivot-1)
    quick_sort(array, pivot, high)
    


def partition(array, low, high):
    # i - bound between elements less than pivot and elements greater than pivot
    pivot = array[low]
    #pivot = array[high]
    i = low+1
    # j - bound between checked and unchecked elements
    for j in range(low+1, high):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i = i+1
    array[low], array[i-1] = array[i-1], array[low]
    #array[high], array[i-1] = array[i-1], array[high]
    return i




arr = [10,9,8,7,6,5,4,3,2,1]
arr_b = [3,8,2,5,1,4,7,6]

quick_sort(arr, 0, len(arr))
quick_sort(arr_b, 0, len(arr_b))
print(arr)
print(arr_b)

arrx = list(range(1,11))
quick_sort(arrx, 0, len(arrx))
print(arrx)

import random

list_rnd = [random.randint(1, 10001) for i in range(100)]
#print(list_rnd)
quick_sort(list_rnd, 0, len(list_rnd))
print(list_rnd)

