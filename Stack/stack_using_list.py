# Stack implementation


class StackOverflowException(Exception):
    pass

class Stack:

    def __init__(self, capacity=10):
        self._stack = []
        # empty stack
        self._top = -1
        self._capacity = capacity
    
    def push(self, element):
        if not self.isFull():
            self._stack.append(element)
            self._top = self._top + 1
        else:
            raise StackOverflowException("Stack capacity overreached")

    def pop(self):
        if not self.isEmpty():
            self._top = self._top - 1
            return self._stack.pop()
        else:
            raise Exception("Stack is empty")

    def size(self):
        return self._top + 1

    def top(self):
        if not self.isEmpty():
            return self._stack[self._top]
        else:
            return None

    def isEmpty(self):
        return self._top == -1

    def isFull(self):
        return self._top == (self._capacity - 1)

    def capacity(self):
        return self._capacity

    def printStack(self):
        for i in range(self._top, -1, -1):
            print(self._stack[i])


stack = Stack(20)
print(stack.size())
print(stack.capacity())
print(stack.isFull())
print(stack.isEmpty())
print(stack.top())
#print(stack.pop())

for i in range(5):
    stack.push(i)
stack.printStack()
print(stack.size())

print(stack.pop())
print(stack.size())
print(stack.top())


            
