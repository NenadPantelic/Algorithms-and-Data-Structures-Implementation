# Bucket Sort - O(n)

def insertion_sort(array):
    for i in range(len(array)):
        temp = array[i]
        j = i
        while j > 0 and temp < array[j-1]:
            array[j] = array[j-1]
            j = j - 1
        array[j] = temp

def bucket_sort(array, n):
    '''
        array : list of uniformly distributed numbers
        n : num of buckets
    '''
    # create  n empty buckets
    buckets = [[] for i in range(n)]

    # insert elements to appropriate bucket
    for val in array:
        buckets[int(n * val)].append(val)
    # sort every bucket
    for i in range(n):
        insertion_sort(buckets[i])

    k = 0
    # merge sorted buckets
    for bucket in buckets:
        for i in range(len(bucket)):
            array[k] = bucket[i]
            k += 1
    # other way
    # result = []
    #for bucket in buckets: result.extend(bucket)


        
arr = [0.897, 0.565, 0.656,0.1234, 0.665, 0.3434]  
bucket_sort(arr, 10)
print(arr)
    
    
