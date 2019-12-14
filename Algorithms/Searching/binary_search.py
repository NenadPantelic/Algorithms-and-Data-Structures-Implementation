# Binary search(O(log(n))

def binary_search(array, element, start, end):
    mid = (start + end) // 2
    mid = start + (end - start) // 2

    if end < start:
        return -1
    if array[mid] == element:
        return mid
    if element < array[mid]:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(array, element, start, end)


def binary_search_iter(array, element, start, end):

    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == element:
            return mid
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
        
# array must be sorted

a = [1,2,3,4,5,6,7]
b = [5, 67, 231, 455, 789, 2000]
c = [3]
d = []


# Recursive
print(binary_search(a, 2, 0, len(a)-1)) # 1
print(binary_search(a, 12, 0, len(a)-1)) # -1
print(binary_search(b, 789, 0, len(b)-1)) #4
print(binary_search(b, 111, 0, len(b)-1)) #-1
print(binary_search(c, 3, 0, len(c)-1)) # 0
print(binary_search(c, 4, 0, len(c)-1)) # -1
print(binary_search(d, 111, 0, len(d)-1)) # -1


# Iterative
print(binary_search_iter(a, 2, 0, len(a)-1)) # 1
print(binary_search_iter(a, 12, 0, len(a)-1)) # -1
print(binary_search_iter(b, 789, 0, len(b)-1)) #4
print(binary_search_iter(b, 111, 0, len(b)-1)) #-1
print(binary_search_iter(c, 3, 0, len(c)-1)) # 0
print(binary_search_iter(c, 4, 0, len(c)-1)) # -1
print(binary_search_iter(d, 111, 0, len(d)-1)) # -1



    
