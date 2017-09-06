class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(data=value)
        else:
            self.head = Node(data=value)

    def insert_after(self, node, value):
        next_node = node.next_node
        node.next_node = Node(data=value, next_node=next_node)

    def push(self, value):
        next_node = self.head
        self.head = Node(data=value, next_node=next_node)

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next_node
        return None

    def delete(self, value):
        if self.head and self.head.data == value:
            self.head = self.head.next_node
            return

        current = self.head
        while current.next_node and current.next_node.data != value:
            current = current.next_node

        if current.next_node.data == value:
            current.next_node = current.next_node.next_node

    def print_list(self):
        elements = []
        if self.head:
            current = self.head
            while current:
                elements.append(current.data)
                current = current.next_node
        print elements

    def detect_remove_loop(self):
        slow = self.head
        fast = self.head.next_node

        while fast and fast.next_node:
            if slow == fast:
                break
            slow = slow.next_node
            fast = fast.next_node.next_node

        if slow == fast:
            slow = self.head
            while slow != fast.next_node:
                slow = slow.next_node
                fast = fast.next_node

            fast.next_node = None


def merge_lists(a, b):
    """
    head = None

    if a is None:
        return b
    elif b is None:
        return a

    if a.data < b.data:
        head = a
        head.next_node = merge_lists(a.next_node, b)
    else:
        head = b
        head.next_node = merge_lists(a, b.next_node)

    return head

    """
    current = Node()
    head = current
    while True:
        if a is None:
            current.next_node = b
            break

        if b is None:
            current.next_node = a
            break

        if a.data >= b.data:
            current.next_node = b
            current = b
            b = b.next_node
        else:
            current.next_node = a
            current = a
            a = a.next_node

    return head.next_node



if __name__ == "__main__":
    l = LinkedList()
    #l.insert(4)
    #l.insert(6)
    #l.insert(9)
    l.print_list()

    s = LinkedList()
    #s.insert(1)
    #s.insert(3)
    #s.insert(8)
    s.print_list()

    h = merge_lists(l.head, s.head)

    p = LinkedList()
    p.head = h
    p.print_list()