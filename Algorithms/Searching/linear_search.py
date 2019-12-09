# Linear search (O(n))

def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1

print(linear_search([1,2,3,4,5,6,7,8,9,10], 6))
print(linear_search([1,2,3,4,5,6,7,8,9,10], -6))
print(linear_search([1,2,3,4,5,6,7,8,9,10], 0))
print(linear_search([1,2,3,4,5,6,7,8,9,10], 10))
