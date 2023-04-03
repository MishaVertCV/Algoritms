from collections import defaultdict
N, M = map(int, input().split())
d = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

visited = [False] * N
l = list()

def dfs(graph, visited, node):
    visited[node - 1] = True
    l.append(node)
    for neig in graph[node]:
        if not visited[neig - 1]:
            dfs(graph, visited, neig)
    l.sort()
    return str(len(l)) + '\n' + ' '.join(map(str, l))
print(dfs(d, visited, 1))