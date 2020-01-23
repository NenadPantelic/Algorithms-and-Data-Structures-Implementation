# Circular linked list

class Node:
    def __init__(self, value):
        self._next = None
        self._value = value

    def setNext(self, next):
        self._next = next

    def getNext(self):
        return self._next

    def setValue(self, value):
        self._value = value

    def getValue(self):
        return self._value

    def __str__(self):
        return str(self.getValue())

class CircularLinkedList:
    def __init__(self):
        self._last = None


    def setLast(self, node):
        self._last = node

    def getLast(self):
        return self._last
    
    def addToEmpty(self, value):
        node = Node(value)
        self.setLast(node)
        self.getLast().setNext(self.getLast())

    def addToBegin(self, value):
        node = Node(value)
        if self.getLast() is None:
            self.addToEmpty(value)
        else:
            node.setNext(self.getLast().getNext())
            self.getLast().setNext(node)

    def addToEnd(self, value):
        node = Node(value)
        if self.getLast() is None:
            self.addToEmpty(value)
        else:
            node.setNext(self.getLast().getNext())
            self.getLast().setNext(node)
            self.setLast(node)

    def addAfter(self, data, value):
        newNode = Node(value)
        current = self.getLast().getNext()
        while current.getValue() != data:
            current = current.getNext()
            if current == self.getLast():
                print("Value not found")
                return
        # insertion at tail
        if current == self.getLast():
            self.addToEnd(value)
        else:
            newNode.setNext(current.getNext())
            current.setNext(newNode)

    def removeNode(self, data):
        if self.getLast() is None:
            print("Operation not allowed! List is empty")
            return
        start = self.getLast().getNext()
        while start.getNext().getValue() != data:
            start = start.getNext()
            if start == self.getLast():
                start = None
                break
        if start is None:
            print("Value not found")
            return
        prev = start
        node = prev.getNext()
        next = node.getNext()
        # list contains only one node
        if prev is node:
            self.setLast(None)
            return
        prev.setNext(next)
        if node == self.getLast():
            self.setLast(prev)      
        node = None
        
    def printList(self):
        if self.getLast() is not None:
            current = self.getLast().getNext()
            first = current
            while True:
                print(current)
                current = current.getNext()
                if current == first:
                    break
        print()
        
            

cll = CircularLinkedList()
n1 = Node(1)
cll.addToEmpty(1)
cll.printList()
cll.removeNode(1)
cll.printList()

cll.addToBegin(2)
cll.printList()
cll.addToEnd(3)
cll.printList()
cll.addAfter(2, 4)
cll.printList()
print(cll.getLast())
print()
cll.removeNode(3)
print(cll.getLast())
print()
cll.printList()
cll.addAfter(2,5)
cll.printList()
