n = int(input())
l = list(map(int, input().split(maxsplit=n)))
s = list()
a1 = l[0]
s.append(a1)
k = 0     
while k < 10 + len(l): 
    if l[a1] == -1:
        break
    s.append(l[a1])
    a1 = l[a1]
    k += 1
if k > len(l) + 1:
    print('No')
else:
    print('Yes')   