# Stack version 2

class EmptyStack(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        return self._data.pop(-1)
    
    def top(self):
        if self.is_empty():
            raise EmptyStack('Stack is empty')
        return self._data[-1]



S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
print(S.top())
