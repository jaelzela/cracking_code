class Node(object):
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree(object):

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(data=value)
            return

        current = self.root
        while current:
            if value > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(data=value, parent=current)
                    return
            elif value < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(data=value, parent=current)
                    return

    def pre_order(self, node):
        if node is not None:
            print node.data
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print node.data
            self.in_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print node.data

    def search(self, value):
        current = self.root

        while current:
            if current.data == value:
                return current
            elif current.data < value:
                current = current.right
            else:
                current = current.left

        return None

    def minimum(self):
        if self.root is None:
            return None

        current = self.root
        while current.left:
            current = current.left

        return current

    def maximum(self):
        if self.root is None:
            return None

        current = self.root
        while current.right:
            current = current.right

        return current

    def sucessor(self, node):
        if node.right is not None:
            current = node.right
            while current.left:
                current = current.left
            return current
        else:
            p = node.parent
            current = node
            while p is not None and current == p.right:
                current = p
                p = p.parent
            return p

    def predecessor(self, node):
        if node.left is not None:
            current = node.left
            while current.right:
                current = current.right
            return current
        else:
            p = node.parent
            current = node
            while p is not None and current == p.left:
                current = p
                p = p.parent
            return p

    def swap(self, node1, node2):
        if node1 == node1.parent.right:
            node1.parent.right = node2
        else:
            node1.parent.left = node2

        if node2.parent and node2.parent != node1:
            if node2 == node2.parent.right:
                node2.parent.right = None
            else:
                node2.parent.left = None

        node2.parent = node1.parent

    def delete(self, node):
        if node.parent is None:
            self.root = None
            return

        if node.left is None and node.right is None and node.parent:
            if node == node.parent.right:
                node.parent.right = None
            else:
                node.parent.left = None
        elif node.left is None and node.right and node.parent:
            self.swap(node, node.right)
        elif node.left and node.right is None and node.parent:
            self.swap(node, node.left)
        else:
            sucessor = self.sucessor(node)
            self.swap(node, sucessor)
            if sucessor != node.left:
                sucessor.left = node.left
            if sucessor != node.right:
                sucessor.right = node.right




if __name__ == '__main__':
    t = BinaryTree()
    t.insert(15)
    t.insert(6)
    t.insert(18)
    t.insert(3)
    t.insert(7)
    t.insert(17)
    t.insert(20)
    t.insert(2)
    t.insert(4)
    t.insert(13)
    t.insert(9)
    t.in_order(t.root)
    n = t.search(6)
    #print n.data
    #print n.parent.data
    #if n.left:
    #    print n.left.data
    #if n.right:
    #    print n.right.data
    print '-'
    t.delete(n)
    t.in_order(t.root)