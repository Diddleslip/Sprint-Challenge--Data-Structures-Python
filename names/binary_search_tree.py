"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # #1. Check if there is no root,
        #     # we can check this by checking if self is None
        # if self is None:
        #     # if there isn't create the node and park it
        #     self = BSTNode(value)
        # #2. Other wise, there is a root
        # else:
        # Compare the value to the root's value to determine 
        # which direction we're gonna go in
        # if the value < root's value
        if value < self.value:
            # go left
            # how do we go left?
            # we have to check if there is another node on the left side
            if self.left:
                # then self.left is a Node
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else the value >= root's vale
        else:
            # go right
            # how do we go right?
            # we have to check if there is another node on the right side
            if self.right:
                # then self.right is a Node
                self.right.insert(value)
            else:
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        # If not the same as the main root and .left and .right don't exist, return False
        if not self.left and not self.right:
            return False
        # Check if target is smaller than root value
        if target < self.value:
            # Go left
            # check if self.left is a node
            if self.left:
                # make self.left the new root and check that
                return self.left.contains(target)
            else: 
                #if self.left doesn't exist up to this point return False
                return False
                # Check if target is bigger than root value
        else:
            # Go right
            if self.right:
                # make self.right the new root and check that
                return self.right.contains(target)
            else:
                #if it doesn't exist then return False
                return False

        # return duplicate

    # Return the maximum value found in the tree
    def get_max(self):
        # Start of with max_value as the root's value
        max_value = self.value
        # print(max_value)

        # self.right is biggest value in our case
        # we want to go to the right branches only
        # check if there is a self.right
        if self.right:
            # compare max_value with the next self.right in line
            if max_value < self.right.value:
                # if greater, assign new value and go to next self.right
                max_value = self.right.value
                return self.right.get_max()
            # if the value isn't bigger just go to next branch
            else: 
               return self.right.get_max()

        # else we traveled through all self.right's and got the highest
        else:
            return max_value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # print("THIS IS SELF.VALUE", self.value)
        fn(self.value)
        # if self.left and self.right:
        #     # fn(self.left.value)
        #     # fn(self.right.value)
        #     return self.left.for_each(fn), self.right.for_each(fn)
        
        if self.left:
            # fn(self.left.value)
            self.left.for_each(fn)

        if self.right:
            # fn(self.right.value)
            self.right.for_each(fn)
                    
        # else:
        #     return

    def iter_depth_first_for_each(self, fn): 
        # with depth-first traversal, there's a certain to when we visit nodes
        # what's that order?
        # init a stack to keep track of the order of nodes we visited
        stack = []
        # add the first node to our stack
        stack.append(self)
        # continue traversing until our stack is empty
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            # add its children to the stack
            # add the right child first and left child second
            # to ensure that left is popped of the stack first
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            # call the fn function on self.value
            fn(self.value)

    def iter_breadth_first_search(self, fn):
        # breadth first traversal follows FIFO ordering of its nodes
        # init a deque
        q = deque()
        # add the first node to our q
        q.append(self)        
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            fn(self.value)


    # Part 2 -----------------------
# depth first traversal is the leaf traversal
# breadth first traversal is the onion traversal

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node = None):

        # if self.left:
        #     self.left.in_order_print(self)
        # print(self.value)
        # if self.right:
        #     self.right.in_order_print(self)

        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque()

        q.append(self)

        while len(q) > 0:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # with depth-first traversal, there's a certain to when we visit nodes
        # what's the order?
        # ini a stack to keep track of the order of nodes we visited
        stack = []
        # add the first node to our stack
        stack.append(self)

        while len(stack) > 0:
            # pop off the stack
            node = stack.pop()
            # add its children to the stack
            # add the right child
            # to ensure that left is popped of the stack first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            # call the print statement on the node.value
            print(node.value)



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            # First print the data of node
            print(node.value)
            # then recurse on the left child
            self.pre_order_dft(node.left) 
            # then recurse on the right child
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:

            # first recurse on left child
            self.post_order_dft(node.left)
            # then recurse on the right child
            self.post_order_dft(node.right)
            # now print the root node.value
            print(node.value)

