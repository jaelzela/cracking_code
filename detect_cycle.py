"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head is None:
        return 0

    d = []
    current = head
    while current.next != None:
        if current.data in d:
            return 1
        d.append(current.data)
        current = current.next

    return 0