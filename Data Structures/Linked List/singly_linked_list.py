# Singlу linked list
import gc

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def setValue(self, value):
        self._value = value

    def getValue(self):
        return self._value

    def setNext(self, next):
        self._next = next

    def getNext(self):
        return self._next
    def __str__(self):
        return str(self._value)

class LinkedList:
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

    
    def printList(self):
        node = self._head
        while node:
            print(node)
            node = node.getNext()

    def pushAtHead(self, value):
        # create new node
        node = Node(value)
        # set new node's next node
        node.setNext(self.getHead())
        # set head (new node)
        self.setHead(node)

    def insertAfterNode(self, prevNode, value):
        if prevNode is None:
            print("The given node is None.  Operation forbidden")
            return
        nextNode = prevNode.getNext()
        node = Node(value)
        prevNode.setNext(node)
        node.setNext(nextNode)

    def pushAtTail(self, value):
        node = Node(value)        
        if self.getHead() is None:
            self.setHead(node)
            return
        last = self.getHead()
        while last.getNext():
            last = last.getNext()
        last.setNext(node)
        
    def pushAtTail2(self, value):
        node = Node(value)        
        if self.getHead() is None:
            self.setHead(node)
            self.setTail(node)
        else:
            tail = self.getTail()
            tail.setNext(node)
            self.setTail(node)

    # without tail reference version
    def removeNode(self, value):
        temp = self.getHead()
        # head node case
        if temp.getValue() == value:
            self.setHead(temp.getNext())
            temp = None
            return
        while temp is not None:
            if temp.getValue() == value:
                break
            prev = temp
            temp = temp.getNext()

        if temp is None:
            print('Value was not found')
            return
        prev.setNext(temp.getNext())
        if temp is self.getTail():
            self.setTail(prev)
        temp = None
        gc.collect()
      
    
    
        

ll = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.setNext(n2)
n2.setNext(n3)
ll.setHead(n1)
ll.setTail(n3)
print()
ll.printList()
ll.pushAtHead(20)
print()
print(ll.getHead())
print()
ll.printList()
ll.insertAfterNode(n2, 50)
print()
ll.printList()
ll.pushAtTail(1000)
print()
ll.printList()
ll.pushAtTail2(2000)
print()
ll.printList()
print()
ll.removeNode(20)
ll.printList()
ll.removeNode(1000)
print()
ll.printList()
ll.removeNode(2000)
print()
print(ll.getTail())
