""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def deep_search_check(node, values):
    if node is None:
        return

    deep_search_check(node.left, values)
    values.append(node.data)
    deep_search_check(node.right, values)
    #if node.left is not None and node.data <= node.left.data:
    #    return False
    #if node.right is not None and node.data >= node.right.data:
    #    return False

    #return deep_search(node.left) and deep_search(node.right)


def checkBST(root):
    values = []
    deep_search_check(root, values)
    v = values[0]
    for i in range(1, len(values)):
        if v >= values[i]:
            return False
        v = values[i]

    return True


root = node(4)
l = node(2)
r = node (6)

ll = node(1)
lr = node(3)
l.left = ll
l.right = lr

rl = node(5)
rr = node(7)
r.left = rl
r.right = rr

root.left = l
root.right = r

print checkBST(root)