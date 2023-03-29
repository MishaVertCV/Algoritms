N = int(input())
l = list(map(int, input().split()))
p = list()
k = 0
while len(l) != 0 or len(p) != 0:
    if len(p) == 0 and len(l) != 0:
        p += l[0 : l.index(min(l)) + 1]
        del(l[0 : l.index(min(l)) + 1])
    if p[-1] == k + 1:
        k += 1
        p.pop()
    else:
        if len(l) != 0:
            p += l[0 : l.index(min(l)) + 1]
            del(l[0 : l.index(min(l)) + 1])
        else:
            print('NO')
            break
if len(l) == 0 and len(p) == 0:
    print('YES')



