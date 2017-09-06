class Stack(object):

    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        return self.elements.pop()

    def print_stack(self):
        print self.elements


if __name__ == '__main__':
    s = Stack()
    s.print_stack()
    s.push(1)
    s.print_stack()
    s.push(2)
    s.print_stack()
    s.push(3)
    s.print_stack()
    print s.pop()
    s.print_stack()
    s.push(4)
    s.print_stack()
    print s.pop()
    s.print_stack()