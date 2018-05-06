# https://www.hackerrank.com/challenges/journey-to-the-moon/problem
def DFS (G):
    t = []
    for u in G:
        if color[u] == 'white':
            t.append(DFS_visit(u))
    return t

def DFS_visit(u):
    color[u] = 'gray'
    temp = []
    temp.append(u)
    # time += 1
    # distance[u] = time
    for v in d[u]:
        if color[v] == 'white':
            # parent[v] = u
            temp.append(v)
            DFS_visit(v)
    color[u] = 'black'
    return temp
    # time += 1
    # final[u] = time


def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


if __name__ == '__main__':
    a, b = map(int, input().strip().split())
    d = {}
    color = {}
    # time = 0
    # distance = {}
    # parent = {}
    # final = {}

    for j in range(a):
        d[j] = []
        color[j] = 'white'
        # distance[j] = 0
        # parent[j] = 'NIL'

    for i in range(1,b+1):
        m,n = map(int, input().split())

        # print('\n\n')
        d[m].append(n)
        d[n].append(m)
    h = DFS(d)
    # print(h) 
    z = []
    for j in h:
        z.append(len(j))
    s = 0
    for w in range(len(z)):
        sum = 0
        for v in range(w+1):
            if (v == w):
                s += sum * z[v]
                break
            sum += z[v]
    print(s)
       


