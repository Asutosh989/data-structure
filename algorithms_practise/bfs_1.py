def bfs(g, color,distance, s):
    color[s] = 'gray'
    distance[s] = 0
    q = []
    q.append(s)
    while (len(q) != 0):
        v = q.pop(0)
        try:
            for n in g[v]:
                if (color[n] == 'white'):
                    color[n] = 'gray'
                    distance[n] = distance[v] + 1
                    q.append(n)
            color[v] = 'black'
        except:
            print(g[v])
    return color, distance



n = int(input())
for i in range(n):
    d = {}
    color = {}
    distance = {}
    x, y  = map(int, input().split())
    for r in range(1,x+1):
        d[r] = []
        color[r] = 'white'
        distance[r] = 9999
    for j in range(y):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    index = int(input())
    c, dist = bfs(d, color, distance, index)
    string = []
    for h in dist:
        dist[h] = dist[h] * 6
        if (dist[h]> 0 and dist[h]<10000):
            string.append(str(dist[h]))
        if (dist[h] > 10000):
            string.append('-1')
    print(' '.join(string))
            