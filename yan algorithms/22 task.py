N, k = map(int, input().split())
def kuz(n, k):
    l = [0] * (n)
    l[0] = 1
    for i in range(1, n):
        r = k
        if (i < r):
            r = i
        for j in range(1, r + 1):
            l[i] = l[i] + l[i - j]
    return l[n - 1]
    
print(kuz(N, k))
