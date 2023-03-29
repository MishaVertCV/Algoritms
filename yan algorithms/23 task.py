N = int(input())
def f(n):
    l = list()
    cache = [0] * (n)
    for i in range(2, n):
        v = cache[i - 1]
        if i % 2 == 0:
            v = min(v, cache[i // 2])
        if i % 3 == 0:
            v = min(v, cache[i // 3])
        cache[i] = v + 1
    k = n
    while k > 1:
        if cache[i] == cache[i-1] + 1:
            l.append(1)
            i -= 1
        if k % 2 == 0 and cache[i] == cache[i/2] + 1:
            l.append(2)
            k = k / 2
        if k % 3 == 0 and cache[i] == cache[i/3] + 1:
            l.append(3)
            k = k / 3
    print(l)
    return cache[-1]
print(f(N))

