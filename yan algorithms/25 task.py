n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
d = [0] * n
d[1] = lst[1] - lst[0]
if n > 2:
    d[2] = lst[2] - lst[0]
    for i in range(3, n):
        d[i] = min(d[i - 2], d[i - 1]) + lst[i] - lst[i - 1]
print(d[n - 1])