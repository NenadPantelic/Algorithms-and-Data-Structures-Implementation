# Counting sort (O(N+max(A)) -> N = len(A)

def counting_sort(array):
    max_el = max(array)
    aux_array = [0 for i in range(max_el+1)]
    for i in range(len(array)):
        aux_array[array[i]] += 1
    sorted_array = []
    for i in range(max_el+1):
        tmp = aux_array[i]
        for j in range(tmp):
            sorted_array.append(i)
    return sorted_array

def counting_sort_v2(array):
    max_el = max(array)
    freq = [0] * (max_el+1)
    n = len(array)
    sorted_array = [0] * n
    for i in range(n):
        freq[array[i]] += 1

    for i in range(1, max_el+1):
        freq[i] += freq[i-1]

    for i in range(n):
        sorted_array[freq[array[i]]-1] = array[i]
        freq[array[i]] -= 1

    for i in range(n):
        array[i] = sorted_array[i]
    #return array
    
a = [5,2,9,5,2,3,5]
print(counting_sort(a))
counting_sort_v2(a)
print(a)

from random import randint
arr = [randint(1,10000) for i in range(1000)]
print(counting_sort(arr))
counting_sort_v2(arr)
print(arr)
