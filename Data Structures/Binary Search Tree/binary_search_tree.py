# Binary search tree

class Node:
    # note: maybe to add reference to parrent node
    def __init__(self, value):
        # left child
        self._left = None
        # right child
        self._right = None
        # node value
        self._value = value

    def set_left(self, left):
        assert left is None or isinstance(left, Node)
        self._left = left

    def get_left(self):
        return self._left

    def set_right(self, right):
        assert right is None or isinstance(right, Node)
        self._right = right

    def get_right(self):
        return self._right
    
    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def __str__(self):
        return str(self.get_value())

class BinarySearchTree:
    def __init__(self, node = None):
        assert node is None or isinstance(node, Node)
        self._root = node

    def set_root(self, node):
        assert node is None or isinstance(node, Node)
        self._root = node
        
    def get_root(self):
        return self._root

    # insertion operation
    def insert_node(self, node):
        if self.get_root() is None:
            self.set_root(node)
        else:
            self._insert(self.get_root(), node)
            
    def _insert(self, root, node):
        assert node is None or isinstance(node, Node)
        if root is None:
            root = node
        elif root.get_value() > node.get_value():
            # go left
            if root.get_left() is None:
                root.set_left(node)
            else:
                self._insert(root.get_left(), node)
        else:
            # go right
            if root.get_right() is None:
                root.set_right(node)
            else:
                self._insert(root.get_right(), node)
    # Search
    def search(self, value):
        assert value is not None
        if self.get_root() is None:
            print('Tree is not formed!')
            return
        return self._search(self.get_root(), value)

    def _search(self, root, value):
        assert value is not None
        if root is None:
            print('Value is not present')
            return
        if root.get_value() == value:
            return root
        elif root.get_value() > value:
            return self._search(root.get_left(), value)
        else:
            return self._search(root.get_right(), value)
    # Remove
    # There are three cases:
    # 1) node has no children (leaf)
    # 2) node has one subtree successor (left or right)
    # 3) node has two successors

    def remove(self, value):
        assert value is not None
        if self.get_root() is None:
            print('Tree is not formed')
            return
        else:
            self._remove(self.get_root(), value)
    def _remove(self, node, value, predecessor = None):
        assert value is not None
        if node is None:
            print('Value cannot be found')
            return

        # value is in left subtree
        if node.get_value() > value:
            self._remove(node.get_left(), value, node)
        # value is in right subtree
        elif node.get_value() < value:
            self._remove(node.get_right(), value, node)
        else:
            # case 1)/2) - left or right subtree
            if node.get_left() is None:
                tmp = node.get_right()
                self._check_succ_and_set(predecessor, node, tmp)
                node = tmp
                
            elif node.get_right() is None:
                tmp = node.get_left()
                self._check_succ_and_set(predecessor, node, tmp)
                node = tmp
            # case 3) - both subtrees   
            else:
                # option 1 - replace node for deletion with the greatest value in the left subtree
                replacement_node, pred = self._get_max_value_in_subtree(node.get_left(), node)
                # option 2 - replace node for deletion with the smallest value in the right subtree
                replacement_node, pred = self._get_min_value_in_subtree(node.get_right(), node)
                
                node.set_value(replacement_node.get_value())
                self._check_succ_and_set(pred, replacement_node, None)
                replacement_node = None


    def _get_max_value_in_subtree(self, node, pred):
        # iterative approach
        current = node
        predecessor = pred
        while current.get_right():
            predecessor = current
            current = current.get_right()
        return current,predecessor

    def _get_min_value_in_subtree(self, node, pred):
        # iterative approach
        current = node
        predecessor = pred
        while current.get_left():
            predecessor = current
            current = current.get_left()
        return current,predecessor

    def _check_succ_and_set(self, pred, node, new_node):
        '''
        pred: predecessor Node
        node: successor node
        new_node: new successor of pred instead of old successor
        '''
        if pred.get_left() == node:
            pred.set_left(new_node)
        elif pred.get_right() == node:
            pred.set_right(new_node)
        else:
            raise Exception('Wrong predecessor')
        

    
    

        
    
        
    # Traversals
    # root - left - right
    def preorder(self, node):
        if node is None:
            return
        # print value
        print(node, end=" ")
        # recurse left
        self.preorder(node.get_left())
        # recurse right
        self.preorder(node.get_right())
        
    # left - root - right
    def inorder(self, node):
        if node is None:
            return
        # recurse left
        self.inorder(node.get_left())
        # print value
        print(node, end=" ")
        #recurse right
        self.inorder(node.get_right())
        
    # left - right - root
    def postorder(self, node):
        if node is None:
            return
        # recurse left
        self.postorder(node.get_left())
        # recurse right
        self.postorder(node.get_right())
        # print value
        print(node, end=" ")

    
# Testing
#import random
nodes = [Node(7), Node(20), Node(5), Node(15), Node(10), Node(4), Node(33), Node(2),\
         Node(25), Node(6)]
##for i in range(10):
##    nodes.append(Node(random.randint(1,100)))
##    #print(nodes[i])

bst = BinarySearchTree()
#nodes.pop(0)
for n in nodes:
    bst.insert_node(n)
    
##bst.preorder(bst.get_root())
##print()
##print(bst.search(4))
##print(bst.search(400))
###print(bst.search(None)) assertion error check
##print(bst.search(33))
##print()


##nodes2 = [Node(11), Node(1), Node(5), Node(15), Node(8), Node(14), Node(3), Node(12),\
##         Node(17), Node(6), Node(19), Node(13)]

##bst2 = BinarySearchTree()
##for n in nodes2:
##    bst2.insert_node(n)
#bst2.inorder(bst2.get_root())

##print()
##n = bst2.search(15)
##bst2.postorder(n)

##values = [25, 15, 10, 22, 50, 35, 70, 4, 12,18, 24, 31, 44, 66, 90]
##bst_nodes = []
##for value in values:
##    bst_nodes.append(Node(value))
##
##bs_tree = BinarySearchTree()
##for node in bst_nodes:
##    bs_tree.insert_node(node)
##root = bs_tree.get_root()
##print("Preorder traversal")
##bs_tree.preorder(root)
##print("Inorder traversal")
##bs_tree.inorder(root)
##print("Postorder traversal")
##bs_tree.postorder(root)

bst = BinarySearchTree()
bst.insert_node(Node(50))
bst.insert_node(Node(30)) 
bst.insert_node(Node(20)) 
bst.insert_node(Node(40)) 
bst.insert_node(Node(70)) 
bst.insert_node(Node(60)) 
bst.insert_node(Node(80))

print('\nInorder')
bst.inorder(bst.get_root())
print('\nDelete 20')
bst.remove(20)
bst.inorder(bst.get_root())
print('\nDelete 30')
bst.remove(30)
bst.inorder(bst.get_root())
print('\nDelete 50')
bst.remove(50)
bst.inorder(bst.get_root())
