from collections import defaultdict
graph = defaultdict(list)
N = int(input())
for i in range(N):
    row = input().split()
    if row[0] in graph.keys():
        graph[row[0]].append(row[1])
    else:
        graph[row[0]] = [row[1]]
    if row[1] in graph.keys():
        graph[row[1]].append(row[0])
    else:
        graph[row[1]] = [row[0]]
finish = input().split()
if finish[1] in graph[finish[0]]:
    print('YES')
else:
    print('NO')

