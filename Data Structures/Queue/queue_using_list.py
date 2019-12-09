# Queue implementation

class QueueOverflow(Exception):
    pass

class QueueUnderflow(Exception):
    pass

class Queue:

    def __init__(self, capacity = 10):
        self._capacity = capacity
        self._queue = [None] * self._capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    def isFull(self):
        return self._size == self._capacity

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, element):
        if not self.isFull():
            self._queue[self._rear] = element
            self._rear = (self._rear + 1) % 10
            self._size = self._size + 1
        else:
            raise QueueOverflow("Queue is already full")

    def dequeue(self):
        if not self.isEmpty():
            self._queue[self._front] = None
            self._front = (self._front + 1) % self._capacity
            self._size = self._size - 1
        else:
            raise QueueUnderflow("Queue is empty")

    def size(self):
        return self._size
    
    def front(self):
        return self._queue[self._front]
    def rear(self):
        return self._queue[self._rear-1]



q = Queue(10)
print(q.front())
print(q.rear())
print(q.isFull())
print(q.isEmpty())
print(q.size())

for val in (3, 32, 424, 5242, 1, 5):
    q.enqueue(val)

print(q.front())
print(q.rear())
print(q.size())

for val in [1, 2, 3, 4]:
    q.enqueue(val)

print(q.rear())
print("Size = " + str(q.size()))
#q.enqueue(100)
while(not q.isEmpty()):
    print(q.front())
    q.dequeue()
#q.dequeue()
print(q.size())
print(q.front())
print(q.rear())

        
