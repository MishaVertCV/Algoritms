N = int(input())
d = dict()
l1 = list()
l2 = list()
for i in range(N):
    s = str(input())
    if s[0:3] == 'add':
        index = s[4:].find(' ')
        k = s[5 + index:len(s)]
        l1.append(k)
        val = int(s[4:(4 + index)])
        l2.append(val)
        if k in d:
            d[k] += val
        else:
            d[k] = val
    if s[0:3] == 'get':
        if s[4:] in d:
            print(d[s[4:]])
        else:
            print(0)
    if s[0:6] == 'delete':
        c = int(s[7:])
        while c > 0:
            if c - l2[-1] < 0:
                d[l1[-1]] = d[l1[-1]] - c
                l2[-1] -= c
                c = 0
            else:
                d[l1[-1]] = d[l1[-1]] - l2[-1]
                c -= l2[-1]
                l1.pop()
                l2.pop()




