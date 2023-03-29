N = int(input())
l = list()
k = 0
for i in range(N):
    c = int(input())
    l.append(c)
for i in range(len(l) - 1):
    k += min(l[i], l[i+1])
print(k)

