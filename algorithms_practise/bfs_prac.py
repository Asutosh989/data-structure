class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbours = list()
        self.distance = 9999
        self.color = 'black'
    
    def add_neighbours(self,v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        # to check if a vertex given is actually a valid vertex and if the vertex name exist in the vertices list
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbours(v)
                if key == v:
                    value.add_neighbours(u)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print (key + str(self.vertices[key].neighbours) + " " + str(self.vertices[key].distance))

    def bfs(self, name):
        vert = self.vertices[name]
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbours:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)
        
        while (len(q) > 0):
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbours:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if (node_v.distance > node_u.distance + 1):
                        node_v.distance = node_u.distance + 1

h=Graph()
n = int(input())
for i in range(n-1):
    m,l = input().split()
    h.add_vertex(Vertex(m))
    h.add_vertex(Vertex(l))
    h.add_edge(m,l)

s = input()
# h.add_vertex(s)
h.bfs(s)
h.print_graph()


# for key in sorted(list(h.vertices.keys())):
#     print(h.vertices[key].distance)

# g = Graph()
# a = Vertex('A')
# g.add_vertex(a)
# g.add_vertex(Vertex('B'))
# for i in range(ord('A'), ord('K')):
#     g.add_vertex(Vertex(chr(i)))

# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

# for edge in edges:
#     g.add_edge(edge[:1], edge[1:])

# g.bfs(a)
# g.print_graph()
        
