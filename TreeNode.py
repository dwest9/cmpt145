# CMPT 145: Binary trees
# Defines the tree node ADT
#
# A treenode is a simple container with three pieces of information
#   data: the contained information
#   left:  a reference to another treenode or None
#   right: a reference to another treenode or None


# Implementation notes:
#   This implementation uses a Python class as a record.

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        """
        Create a new TreeNode for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the KVTreeNode
            left:   Another TreeNode (or None, by default)
            right:  Another TreeNode (or None, by default)
        """
        self.data = data
        self.left = left
        self.right = right

# that's it!