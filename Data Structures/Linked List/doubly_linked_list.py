# Doubly Linked list
from gc import collect

class Node:
    def __init__(self, value):
        self._value = value
        self._previous = None
        self._next = None

    def setValue(self, value):
        self._value = value

    def getValue(self):
        return self._value

    def setPrevious(self, previous):
        self._previous = previous

    def getPrevious(self):
        return self._previous

    def setNext(self, next):
        self._next = next

    def getNext(self):
        return self._next

    def addToRight(self, node):
        self._next = node
        node.setPrevious(self)

    def __str__(self):
        return str(self.getValue())

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def setHead(self, head):
        self._head = head

    def getHead(self):
        return self._head

    def setTail(self, tail):
        self._tail = tail

    def getTail(self):
        return self._tail

    def pushAtHead(self, value):
        node = Node(value)
        currentHead = self.getHead()
        node.addToRight(currentHead)
        self.setHead(node)

    def insertAfterNode(self, prevNode, value):
        newNode = Node(value)
        nextNode = prevNode.getNext()
        prevNode.addToRight(newNode)
        # if prevNode is not tail
        if nextNode is not None:
            newNode.addToRight(nextNode)
        else:
            self.setTail(newNode)

    def insertBeforeNode(self, nextNode, value):
        if nextNode is None:
            print("Operation not allowed")
            return
        
        node = Node(value)
        prevNode = nextNode.getPrevious()
        if prevNode is None:
            self.setHead(node)
        else:
            prevNode.addToRight(node)
        node.addToRight(nextNode)

    # without tail version
    def pushAtTail(self, value):
        node = Node(value)
        last = self.getHead()
        if last is None:
            self.setHead(node)
        while last.getNext() is not None:
            last = last.getNext()
        last.addToRight(node)

    def pushAtTail2(self, value):
        node = Node(value)
        if self.getHead() is None:
            self.setHead(node)
        else:
            tail = self.getTail()
            tail.addToRight(node)
        self.setTail(node)

    def removeNode(self, delNode):
        # delNode is Node by type
        # head case
        if self.getHead() == delNode:
            newHead = delNode.getNext()
            self.setHead(newHead)
            newHead.setPrevious(None)
            return
        # tail case
        if self.getTail() == delNode:
            newTail = self.getTail().getPrevious()
            self.setTail(newTail)
            newTail.setNext(None)
            return
        # otherwise
        prev = delNode.getPrevious()
        next = delNode.getNext()
        prev.addToRight(next)
        collect()
            
            

    def traverseToTail(self):
        node = self.getHead()
        while node:
            print(node)
            node = node.getNext()

    def traverseToHead(self):
        node = self.getTail()
        while node:
            print(node)
            node = node.getPrevious()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.addToRight(n2)
n2.addToRight(n3)
dll = DoublyLinkedList()
dll.setHead(n1)
dll.setTail(n3)
dll.traverseToTail()
print()
dll.traverseToHead()
dll.pushAtHead(0)
print()
dll.traverseToTail()
dll.insertAfterNode(dll.getHead(), Node(5))
dll.insertAfterNode(dll.getTail(), Node(6))
print()
dll.traverseToTail()
dll.insertBeforeNode(dll.getHead(), 20)
dll.insertBeforeNode(n2, 200)
print()
dll.traverseToTail()
dll.pushAtTail(4000)
print()
dll.traverseToTail()
dll.pushAtTail2(400)
print()
dll.traverseToHead()
dll.removeNode(dll.getHead())
dll.removeNode(dll.getTail())
dll.removeNode(n3)
print()
dll.traverseToTail()
