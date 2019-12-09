# Merge sort - O(nlog(n))

def merge_sort(array):
    if len(array) <= 1:
        return array
    left_half = merge_sort(array[:len(array)//2])
    right_half = merge_sort(array[len(array)//2:])
    return merge(left_half, right_half)


def merge(array_a, array_b):
    merged_array = []
    i = j = 0
    while i < len(array_a) and j < len(array_b):
        if array_a[i] <= array_b[j]:
            merged_array.append(array_a[i])
            i += 1
        else:
            merged_array.append(array_b[j])
            j += 1
    while i < len(array_a):
        merged_array.append(array_a[i])
        i += 1

    while j < len(array_b):
        merged_array.append(array_b[j])
        j += 1

    return merged_array


def merge_sort_2(array):
    if len(array) <= 1:
        return array
    left_half = merge_sort_2(array[:len(array)//2])
    right_half = merge_sort_2(array[len(array)//2:])
    return merge_2(left_half, right_half)


def merge_2(array_a, array_b):
    len_a = len(array_a)
    len_b = len(array_b)
    total_len = len_a + len_b
    merged_array = []
    i = j = 0
    a_flag = b_flag = False
    for k in range(total_len):
        if i >= len_a:
            b_flag = True
        if j >= len_b:
            a_flag = True
        if not b_flag and (a_flag or array_a[i] <= array_b[j]):
            merged_array.append(array_a[i])
            i += 1
        elif not a_flag and (b_flag or array_a[i] > array_b[j]):
            merged_array.append(array_b[j])
            j += 1
    return merged_array
    
# version 1
print("Version 1")
print(merge_sort([10,9,8,7,6,5,4,3,2,1]))
print(merge_sort([1] * 10))
print(merge_sort([1,3,5,7,9,2,4,6,8,10]))

print("Version 2")
# version 2
print(merge_sort_2([10,9,8,7,6,5,4,3,2,1]))
print(merge_sort_2([1] * 10))
print(merge_sort_2([1,3,5,7,9,2,4,6,8,10]))
            
