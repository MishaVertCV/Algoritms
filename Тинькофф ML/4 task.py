n = int(input())
l = list(map(int, input().split()))
d = dict()
for i in range(len(l)):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1
    p = list(d.values())
    if len(p) == 1:
        length = p[0]
    else:
        p.sort()
        if (min(p) == max(p) - 1 and p[-1] != p[-2]) or (p[0] != p[1] and p[1] == max(p) and p[0] == 1) or (p[0] == max(p) and p[0] == 1):
            length = i + 1
print(length)   