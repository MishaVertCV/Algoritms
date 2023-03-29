n, s = map(int, input().split())
l = list()
r = list()
a = list()
for i in range(n):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)
    a.append(li)
    a.append(ri)
b = set(a)
b = list(b)
b.sort()
def test(left, right):
    A = 0 
    B = 0
    k = 0
    Nor = list()
    for i in range(n):
        if r[i] < left:
            A += 1
            k += l[i]
        elif l[i] > right:
            B += 1
            k += l[i]
        else:
            Nor.append(l[i])
    Nor.sort()
    x = 0
    if A <= int(n/2) and B <= int(n/2):
        for i in range(int(n/2) - A):
            k += Nor[i]
        x = max(x, s - k)
        y = x / (int(n/2) + 1 - B)
        if y >= right:
            y = right
        k += y * (int(n/2) + 1 - B)
        if k <= s and y >= left and y <= right:
            return y
    return -1
ans = -1
m = int(len(b)/2)
for j in range(-1, 2):
    p = m + j
    if p >= 1 and p <= n:
        ans = max(ans, test(b[p], b[p]))
for j in range(-1, 2):
    p = m + j
    if p >= 1 and p < n:
        ans = max(ans, test(b[p], b[p + 1]))
print(int(ans))
    
        