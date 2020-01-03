# O((n+b)log_b(maxx))
# b - radix of digits
# maxx - maximum element of an array

RANGE = 10
def count_sort(array, place):
    n = len(array)
    output = [0] * n
    freq = [0] * RANGE
    for i in range(n):
        digit = (array[i]//place) % RANGE
        freq[digit] += 1
    for i in range(1,RANGE):
        freq[i] += freq[i-1]

    for i in range(n-1, -1, -1):
        digit = (array[i]//place) % RANGE
        output[freq[digit]-1] = array[i]
        freq[digit] -= 1

    for i in range(n):
        array[i] = output[i]
        

def radix_sort(array):
    maxx = max(array)
    mul = 1
    while maxx:
        count_sort(arr, mul)
        mul *= 10
        maxx //= 10

    #return array

arr = [10, 21, 17, 34, 44,11, 654, 123]
radix_sort(arr)
print(arr)
from random import randint
arr = [randint(1,10000) for i in range(1000)]
radix_sort(arr)
print(arr)
