n = input()
s = input()
b = input()
h = list(b)
d = s.split()
r = list()
k = 0
for i in range(len(d)):
    t = list(d[i])
    r.append(len(t))
for i in range(len(r)-1):
    r[i+1] += r[i]
for i in range(len(b)):
    if h[i-1] == h[i] and i-1 not in r:
        k += 1   
print(k)
