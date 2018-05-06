def DFS (G):
    for u in G:
        if color[u] == 'white':
            DFS_visit(u)

def DFS_visit(u):
    global time
    color[u] = 'gray'
    time += 1
    distance[u] = time
    for v in graph[u]:
        if color[v] == 'white':
            parent[v] = u
            DFS_visit(v)
    color[u] = 'black'
    time += 1
    final[u] = time



graph = {
    'A' :['B','C'],
    'B' : ['A', 'D','E'],
    'C' : ['A','F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}
color = {}
distance = {}
parent = {}
final = {}
time = 0

for i in graph:
    color[i] = 'white'
    distance[i] = 0
    parent[i] = 'NIL'

print ("\nBefore DFS\n")
print(graph)
print(color)
print(distance)
print(final)

DFS(graph)

print ("\nAfter DFS\n")
print(graph)
print(color)
print(distance)
print(final)            




