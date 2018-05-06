def dequeue(q):
    s = q[0]
    del q[0]
    return s

def bfs(g,color, distance, s):
    color[s] = 'gray'
    distance[s] = 0
    q = []
    q.append(s)
    while (len(q) != 0):
        v = dequeue(q)
        for n in g[v]:
            if (color[n] == 'white'):
                color[n] = 'gray'
                distance[n] = distance[v] + 1
                q.append(n)
        color[v] = 'black'
    return color, distance


d = {}
color = {}
distance = {}

n = int(input())

for i in range(n-1):
    a,b = input().split()
    if (a not in d.keys()):
        d[a]=[]
    elif (a in d.keys()):
        d[a].append(b)
    if (b not in d.keys()):
        d[b] = []
        d[b].append(a)
    elif (b in d.keys()):
        d[b].append(a)
        
for i in d:
    color[i] = 'white'
    distance[i] = 9999

s = int(input())

color,distance = bfs(d, color, distance, '1')

counter = 0
for i in d:
    print(f'Node {i} is colored {color[i]} at level {distance[i]}')
    if (distance[i] == s-1):
        counter += 1
print(counter)