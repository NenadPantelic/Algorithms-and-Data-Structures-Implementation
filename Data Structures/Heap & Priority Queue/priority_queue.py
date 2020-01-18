# Priority queue
def max_heapify(array, i):
    '''
    array : list of numbers
    i : position of the element where we start heapification
    '''

    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array)

    largest = i
    if left < length and array[left] > array[i]:
        largest = left
        
    if right < length and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        max_heapify(array, largest)

# O(n)
def build_max_heap(array):
    half = len(array)//2
    for i in range(half, -1, -1):
        max_heapify(array, i)
class MaxPriorityQueue:
    def __init__(self, arr):
        self._pq = arr
        build_max_heap(self._pq)
        self._length = len(self._pq)

    def maximum(self):
        return self._pq[0]

    def extract_maximum(self):
        if self._length < 1:
            return -1
        maximum = self.maximum()
        self._pq[0] = self._pq[-1]
        self._length -= 1
        self._pq = self._pq[:self._length]
        max_heapify(self._pq, 0)
        return maximum


    def increase_value(self, i, value):
        if self._pq[i] > value:
            print('New value is less than old one')
            return
        self._pq[i] = value
        while(i > 0 and self._pq[(i-1)//2] < self._pq[i]):
            self._pq[i], self._pq[(i-1)//2] = self._pq[(i-1)//2], self._pq[i]
            i = i // 2

    def insert_value(self, value):
        self._length += 1
        self._pq.append(-1)
        self.increase_value(self._length-1, value)
    def print_pq(self):
        for i in range(self._length):
            if i % 2 == 0:
                end = '\n'
            else:
                end = ' '
            print(self._pq[i], end=end)
        print()
        

maxpq = MaxPriorityQueue([3,1,7,4,8])
maxpq.print_pq()
maxpq.insert_value(6)
maxpq.print_pq()
print(maxpq.extract_maximum())
maxpq.print_pq()

'''
from heapq import heappush, heappop, heapify  
  
# heappop - pop and return the smallest element from heap 
# heappush - push the value item onto the heap, maintaining 
#             heap invarient 
# heapify - transform list into heap, in place, in linear time
'''
