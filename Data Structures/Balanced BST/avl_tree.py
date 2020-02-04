# Balanced Binary Search Tree - AVL

##class Node:
##    def __init__(self, value):
##        self._value = value
##        self._left = None
##        self._right = None
##        self._balanced_factor = 0
##        self._height = 0
##
##    def set_value(self, value):
##        self._value = value
##
##    def get_value(self):
##        return self._value
##
##    def set_left(self, node):
##        assert isinstance(node, Node) or node is None
##        self._left = node
##
##    def get_left(self):
##        return self._left
##
##    def set_right(self, node):
##        assert isinstance(node, Node) or node is None
##        self._right = node
##
##    def get_right(self):
##        return self._right
##
##    def set_balanced_factor(self, bf):
##        self._balanced_factor = bf
##
##    def get_balanced_factor(self):
##        return self._balanced_factor
##
##    def update_balanced_factor(self, value):
##        self.set_balanced_factor(self.get_balanced_factor() + value)
##
##    def set_height(self, height):
##        self._height = height
##
##    def get_height(self):
##        return self._height
##
##    def update_height(self, value):
##        self.set_height(self.get_height() + value)
##
##    def __str__(self):
##        return str(self.get_value())
##
##class AVLBST:
##    def __init__(self, root = None):
##        assert isinstance(root, Node) or root is None
##        self._root = root
##
##    def set_root(self, root):
##        assert isinstance(root, Node) or root is None
##        self._root = root
##
##    def get_root(self):
##        return self._root
##        
##
##    def insert(self, value):
##        '''
##        return True if node is inserted, False otherwise
##        '''
##        if value is None:
##            return False
##        # insert only unique values
##        if not self._contains(self.get_root(), value):
##            self.set_root(self._insert(self.get_root(), value))
##            return True
##        # duplicate
##        return False
##
##    def _insert(self, node, value):
##        assert isinstance(node, Node) or node is None
##        if node is None:
##            return Node(value)
##
##        if node.get_value() > value:
##            # go left
##            node.set_left(self._insert(node.get_left(), value))
##        else:
##            # go right
##            node.set_right(self._insert(node.get_right(), value))
##        # update balance factor
##        self._update(node)
##
##        # rebalance the tree
##        return self._balance(node)
##
##    def _update(self, node):
##        assert isinstance(node, Node) or node is None
##        # height of left and righ subtree
##        lh = rh = -1
##        if node.get_left() is not None: lh = node.get_left().get_height()
##        if node.get_right() is not None: rh = node.get_right().get_height()
##
##        # update node's height
##        node.set_height(max(lh,rh) + 1)
##        # update bf of current node
##        node.set_balanced_factor(rh-lh)
##
##    def _balance(self, node):
##        assert isinstance(node, Node) or node is None
##        # left heavy subtree
##        if node.get_balanced_factor() == -2:
##            left = node.get_left()
##            if left is not None and left.get_balanced_factor() <= 0:
##                return self._left_left_case(node)
##            else:
##                return self._left_right_case(node)
##        elif node.get_balanced_factor() == 2:
##            right = node.get_right()
##            if right is not None and right.get_balanced_factor() >= 0:
##                return self._right_right_case(node)
##            else:
##                return self._right_left_case(node)
##        # good balance
##        return node
##
##    # balancing cases
##    def _left_left_case(self, node):
##        return self._right_rotation(node)
##
##    def _left_right_case(self, node):
##        node.set_left(self._left_rotation(node.get_left()))
##        return self._left_left_case(node)
##    
##    def _right_right_case(self, node):
##        return self._left_rotation(node)
##
##    def _right_left_case(self, node):
##        node.set_right(self._right_rotation(node.get_right()))
##        return self._right_right_case(node)
##
##
##    def _right_rotation(self, node):
##        assert isinstance(node, Node) or node is None
##        left_child = node.get_left()
##        node.set_left(left_child.get_right())
##        left_child.set_right(node)
##        self._update(node)
##        self._update(left_child)
##        return left_child
##
##    def _left_rotation(self, node):
##        assert isinstance(node, Node) or node is None
##        right_child = node.get_right()
##        node.set_right(right_child.get_left())
##        right_child.set_left(node)
##        self._update(node)
##        self._update(right_child)
##        return right_child
##        
##                       
##    def _contains(self, root, value):
##        assert isinstance(root, Node) or root is None
##        if root is None:
##            return False
##        if root.get_value() == value:
##            return True
##
##        if root.get_value() > value:
##            return self._contains(root.get_left(), value)
##
##        else:
##            return self._contains(root.get_right(), value)
##
##   
##    def _get_min_value_in_subtree(self, node):
##        # iterative approach
##        current = node
##        while current.get_left():
##            current = current.get_left()
##        return current
##
##    def remove(self, value):
##        assert value is not None
##        if self.get_root() is None:
##            print('Tree is not formed')
##            return
##        else:
##            self._remove(self.get_root(), value)
##    def _remove(self, node, value, predecessor = None):
##        assert value is not None
##        if node is None:
##            print('Value cannot be found')
##            return
##
##        # value is in left subtree
##        if node.get_value() > value:
##            self._remove(node.get_left(), value, node)
##        # value is in right subtree
##        elif node.get_value() < value:
##            self._remove(node.get_right(), value, node)
##        else:
##            # case 1)/2) - left or right subtree
##            if node.get_left() is None:
##                tmp = node.get_right()
##                self._check_succ_and_set(predecessor, node, tmp)
##                node = tmp
##                return
##                
##            elif node.get_right() is None:
##                tmp = node.get_left()
##                self._check_succ_and_set(predecessor, node, tmp)
##                node = tmp
##                return
##            # case 3) - both subtrees   
##            else:
##                # option 1 - replace node for deletion with the greatest value in the left subtree
##                replacement_node, pred = self._get_max_value_in_subtree(node.get_left(), node)
##                # option 2 - replace node for deletion with the smallest value in the right subtree
##                replacement_node, pred = self._get_min_value_in_subtree(node.get_right(), node)
##                
##                node.set_value(replacement_node.get_value())
##                self._check_succ_and_set(pred, replacement_node, None)
##                replacement_node = None
##                # update bf of node
##                self._update(node)
##                # rebalance node
##                self._balance(node)
##                
##
##
##    def _get_max_value_in_subtree(self, node, pred):
##        # iterative approach
##        current = node
##        predecessor = pred
##        while current.get_right():
##            predecessor = current
##            current = current.get_right()
##        return current,predecessor
##
##    def _get_min_value_in_subtree(self, node, pred):
##        # iterative approach
##        current = node
##        predecessor = pred
##        while current.get_left():
##            predecessor = current
##            current = current.get_left()
##        return current,predecessor
##
##    def _check_succ_and_set(self, pred, node, new_node):
##        '''
##        pred: predecessor Node
##        node: successor node
##        new_node: new successor of pred instead of old successor
##        '''
##        if pred.get_left() == node:
##            pred.set_left(new_node)
##        elif pred.get_right() == node:
##            pred.set_right(new_node)
##        else:
##            raise Exception('Wrong predecessor')
##
##    # root - left - right
##    def preorder(self, node):
##        if node is None:
##            return
##        # print value
##        print(node, end=" ")
##        # recurse left
##        self.preorder(node.get_left())
##        # recurse right
##        self.preorder(node.get_right())

# rerooting concept
##avl = AVLBST()
##avl.insert(10)
##avl.insert(20)
##avl.insert(30)
##avl.insert(40)
##avl.insert(50)
##avl.insert(25)
##avl.insert(5)
##avl.insert(1)
##avl.preorder(avl.get_root())
##print()
##avl.remove(10)
##avl.preorder(avl.get_root())
##print()
##avl.remove(20)
##avl.preorder(avl.get_root())
##

# Python code to delete a node in AVL tree 
# Generic tree node class 
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
# AVL tree class which supports insertion, 
# deletion operations 
class AVL_Tree(object): 
  
    def insert(self, root, key): 
          
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                          self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    # Recursive function to delete a node with 
    # given key from subtree with given root. 
    # It returns root of the modified subtree. 
    def delete(self, root, key): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                #root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                #root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, 
                                      temp.val) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left),  
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left),  
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                          self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                          self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
  
  
myTree = AVL_Tree() 
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2] 
  
for num in nums: 
    root = myTree.insert(root, num) 
  
# Preorder Traversal 
print("Preorder Traversal after insertion -") 
myTree.preOrder(root) 
print() 
  
# Delete 
key = 10
root = myTree.delete(root, key) 
  
# Preorder Traversal 
print("Preorder Traversal after deletion -") 
myTree.preOrder(root) 
print() 

