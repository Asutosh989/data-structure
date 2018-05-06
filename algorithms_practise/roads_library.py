def find_regions(G, color):
    regions = []
    for u in G:
        if color[u] == 'white':
            region = set()
            region.add(u)
            DFS_visit(u, color, region)
            regions.append(region)
            # print(regions)
            # print(region)
    return regions

def DFS_visit(u, color, region):
    color[u] = 'gray'
    for v in G[u]:
        if color[v] == 'white':
            # parent[v] = u
            region.add(v)
            DFS_visit(v, color, region)
    color[u] = 'black'

n = int(input())

G = {}
color = {}
distance = {}
for _ in range(n):
    v, e, c_lib, c_road = map(int, input().split())
    for i in range(e):
        a,b = map(int, input().split())
        if a not in G:
            G[a] = []
        G[a].append(b)
        if b not in G:
            G[b] = []
        G[b].append(a)
       
    for j in G:
        color[j] = 'white'
        distance[j] = 0
        
    regions = find_regions(G, color)
    print(regions)
    
