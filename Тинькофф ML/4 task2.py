from collections import Counter
l = list(map(int, input().split()))
d = dict(Counter(l))
print(d)