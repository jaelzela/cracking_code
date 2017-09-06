
class Vertex(object):
    def __init__(self, data=None):
        self.data = data


class Graph(object):

    def __init__(self, vertexes=[]):
        self.verts = vertexes
        self.m = []
        for i in range(len(self.verts)):
            self.m.append([0]*len(self.verts))

    def add_edges(self, edges):
        for u, v in edges:
            self.m[self.verts.index(u)][self.verts.index(v)] = 1

    def adjacent_list(self, vertex):
        return self.m[self.verts.index(vertex)]

    def vertexes(self):
        return self.verts


def is_sink(row, g, m):
    for col in range(len(g.vertexes())):
        if m[row][col] == 1:
            return False
    for col in range(len(g.vertexes())):
        if m[col][row] == 0 and row != col:
            return False
    return True


def celebrity(g, m):
    row = 1
    col = 1
    while row < len(g.vertexes()) and col < len(g.vertexes()):
        if m[row][col] == 1:
            row += 1
        else:
            col += 1
    if is_sink(row, g, m):
        return g.vertexes()[row].data
    else:
        return None


if __name__ == '__main__':
    a = Vertex(data='1')
    b = Vertex(data='2')
    c = Vertex(data='3')
    d = Vertex(data='4')
    e = Vertex(data='5')

    g = Graph(vertexes=[a, b, c, d, e])
    g.add_edges([(a, b), (a, d), (b, d), (b, e), (c, a), (c, d), (e, c), (e, d)])
    #print g.m
    print celebrity(g, g.m)