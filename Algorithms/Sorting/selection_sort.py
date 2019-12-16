# Selection Sort (O(n^2))

def selection_sort(array):

    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                # swap
                array[i], array[j] = array[j], array[i]
    return array



arr = list(range(10, 0, -1))
arr2 = [23, -4, 2, 6, 0, -11, 76, -299, 86, 31]


print(selection_sort(arr))
print(selection_sort(arr2))
