#Insertion sort (O(n^2))

def insertion_sort(array):
    for i in range(len(array)):
        temp = array[i]
        j = i
        while j > 0 and temp < array[j-1]:
            array[j] = array[j-1]
            j = j - 1
        array[j] = temp

import random
a = [random.randint(1,100) for i in range(10)]
print(a)
insertion_sort(a)
print(a)
