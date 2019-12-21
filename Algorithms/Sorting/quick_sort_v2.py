# last element as pivot
def quick_sort(array, low, high):
    #if high == low
    if low >= high:
        return
    pivot = partition(array, low, high)
    quick_sort(array, low, pivot)
    quick_sort(array, pivot+1, high)
    


def partition(array, low, high):
    # i - bound between elements less than pivot and elements greater than pivot
    pivot = array[high-1]
    i = low
    # j - bound between checked and unchecked elements
    for j in range(low, high):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i = i+1
    array[high-1], array[i] = array[i], array[high-1]
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
