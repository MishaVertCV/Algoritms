import graphlib
from collections import defaultdict
N, M = map(int, input().split())
d = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
ts = graphlib.TopologicalSorter(d)
print(*tuple(ts.static_order()))