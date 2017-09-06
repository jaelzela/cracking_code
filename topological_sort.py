class Vertex(object):

    def __init__(self, data=None):
        self.data = data
        self.status = None
        self.predecessor = None


class Graph(object):

    def __init__(self):
        self.elements = []
        self.adj = dict()

    def insert(self, vertex, adjacent_list=[]):
        self.elements.append(vertex)
        self.adj[vertex.data] = adjacent_list

    def adjacent_list(self, vertex):
        #print 'adj', vertex.data
        #print self.adj[vertex.data]
        return self.adj[vertex.data]

    def vertexes(self):
        return self.elements


def visit_vertex(graph, vertex, l):
    vertex.status = 1

    for v in graph.adjacent_list(vertex):
        if v.status == 0:
            v.predecessor = vertex
            visit_vertex(graph, v, l)

    vertex.status = 2
    l.insert(0, vertex)


def topological_sort(graph):
    for v in graph.vertexes():
        v.status = 0

    l = []
    for v in graph.vertexes():
        if v.status == 0:
            visit_vertex(graph, v, l)

    return l

#  ___________
# |  |        |
# w  z  u  v--y--x
#       |  |     |
#        --------

if __name__ == '__main__':

    u = Vertex(data='u')
    v = Vertex(data='v')
    w = Vertex(data='w')
    x = Vertex(data='x')
    y = Vertex(data='y')
    z = Vertex(data='z')

    g = Graph()
    g.insert(u, [v, x])
    g.insert(v, [y])
    g.insert(w, [y, z])
    g.insert(x, [y])
    g.insert(y, [x])
    g.insert(z, [z])

    print [e.data for e in topological_sort(g)]

    und = Vertex(data='undershorts')
    pan = Vertex(data='pants')
    bel = Vertex(data='belt')
    shi = Vertex(data='shirt')
    tie = Vertex(data='tie')
    jac = Vertex(data='jacket')
    soc = Vertex(data='socks')
    sho = Vertex(data='shoes')
    wat = Vertex(data='watch')

    r = Graph()
    r.insert(shi, [tie, bel])
    r.insert(wat, [])
    r.insert(und, [pan, sho])
    r.insert(pan, [bel, sho])
    r.insert(bel, [jac])
    r.insert(tie, [jac])
    r.insert(jac, [])
    r.insert(soc, [sho])
    r.insert(sho, [])


    print [e.data for e in topological_sort(r)]