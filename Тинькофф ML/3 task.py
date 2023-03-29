n = int(input())
s = str(input())
if len(set(s)) != 4:
    print(-1)
else:
    length = 2 * 10 ** 5
    for l in range(len(s) - 3):
        lis = ['a', 'b', 'c', 'd']
        r = l
        while lis != list() and r < len(s):
            if s[r] in lis:
                del(lis[lis.index(s[r])])
            r += 1
        if lis == list():
            length = min(length, r - l)
            if length == 4:
                break
    print(length)
        