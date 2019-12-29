# Bubble sort(O(n^2))

def bubble_sort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(length-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]



import random
a = [random.randint(1,10) for i in range(10)]
print(a)
bubble_sort(a)
print(a)
