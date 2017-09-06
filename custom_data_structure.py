
class DStruct(object):
    def __init__(self):
        self.elements = []
        self.mins = []

    def get_last(self):
        return self.elements[-1]

    def remove_last(self):
        elem = self.elements.pop()
        if elem == self.mins[-1]:
            self.mins.pop()

    def add(self, elem):
        if len(self.mins) == 0:
            self.mins.append(elem)
        elif self.mins[-1] >= elem:
            self.mins.append(elem)
        self.elements.append(elem)

    def minimum(self):
        return self.mins[-1]


if __name__ == '__main__':
    d = DStruct()
    d.add(5)
    d.add(3)
    d.add(8)
    d.add(7)
    d.add(2)
    d.add(6)
    d.add(9)
    print d.minimum()
    d.remove_last()
    print d.minimum()
    d.remove_last()
    print d.minimum()
    d.remove_last()
    print d.minimum()
