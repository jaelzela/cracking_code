class Queue(object):

    def __init__(self):
        self.elements = []

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        element = self.elements[0]
        del self.elements[0]
        return element

    def print_queue(self):
        print self.elements

if __name__ == '__main__':
    q = Queue()
    q.print_queue()
    q.enqueue(1)
    q.print_queue()
    q.enqueue(2)
    q.print_queue()
    q.enqueue(3)
    q.print_queue()
    print q.dequeue()
    q.print_queue()
    q.enqueue(4)
    q.print_queue()
    print q.dequeue()
    q.print_queue()