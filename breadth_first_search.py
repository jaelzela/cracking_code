class Vertex(object):

    def __init__(self, data=None):
        self.data = data
        self.status = None
        self.predecessor = None


class Graph(object):

    def __init__(self):
        self.vertexes = []
        self.adj = dict()

    def insert(self, vertex, adjacent_list=[]):
        self.vertexes.append(vertex)
        self.adj[vertex.data] = adjacent_list

    def adjacent_list(self, vertex):
        return self.adj[vertex.data]

    def all_vertexs(self):
        return self.vertexes


def breadth_first_search(g, v):
    for vertex in g.all_vertexs():
        vertex.status = 0

    v.status = 1
    v.predecessor = None

    q = []
    q.insert(0, v)
    while len(q) > 0:
        u = q.pop()

        for vertex in g.adjacent_list(u):
            if vertex.status == 0:
                vertex.status = 1
                vertex.predecessor = u
                q.insert(0, vertex)
        u.status = 2
        print u.data


if __name__ == '__main__':
    r = Vertex(data='r')
    s = Vertex(data='s')
    t = Vertex(data='t')
    u = Vertex(data='u')
    v = Vertex(data='v')
    w = Vertex(data='w')
    x = Vertex(data='x')
    y = Vertex(data='y')

    g = Graph()
    g.insert(r, [v, s])
    g.insert(s, [w, r])
    g.insert(t, [u, w, x])
    g.insert(u, [t, x, y])
    g.insert(v, [r])
    g.insert(w, [t, x, s])
    g.insert(x, [y, u, t, w])
    g.insert(y, [u, x])

    breadth_first_search(g, s)