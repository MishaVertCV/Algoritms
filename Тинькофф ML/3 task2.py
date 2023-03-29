s = str(input())
if len(set(s)) != 4:
    print(-1)
else:
    index_a = -1
    index_b = -1
    index_c = -1
    index_d = -1
    for r in range(len(s)):
        if s[r] == 'a':
            index_a = r
        if s[r] == 'b':
            index_b = r
        if s[r] == 'c':
            index_c = r
        if s[r] == 'd':
            index_d = r
        l = min(min(index_a, index_b), min(index_c, index_d))
        if l != -1:
            length = r - l + 1
    print(length)

