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
        return self.adj[vertex.data]

    def vertexes(self):
        return self.elements


def visit_vertex(graph, vertex):
    vertex.status = 1

    for v in graph.adjacent_list(vertex):
        if v.status == 0:
            v.predecessor = vertex
            visit_vertex(graph, v)
    vertex.status = 2
    print vertex.data


def depth_first_search(graph):
    for v in graph.vertexes():
        v.status = 0

    for v in graph.vertexes():
        if v.status == 0:
            visit_vertex(graph, v)


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

    depth_first_search(g)