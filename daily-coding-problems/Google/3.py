#This problem was asked by Google.

#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
#and deserialize(s), which deserializes the string back into the tree.

#For example, given the following Node class

class Node:
    def__init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

def serialize(Node root) {
    if root is None:     #if root is None: checks if the root is null
        return "#"
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

} 

def deserialize(s) {
    def helper():
} 