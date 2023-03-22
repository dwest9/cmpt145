# CMPT 145: Node-based Queues
# Defines the Node ADT
#
# A node is a simple container with two pieces of information
#   data: the contained information
#   next: a reference to another node
# We can create node-chains of any size.

# Implementation notes:
#   This implementation uses a Python dictionary as a record.


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
