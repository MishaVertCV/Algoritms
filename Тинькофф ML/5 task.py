n = int(input())
a = list(map(int, input().split()))
sum_a = [a[0]]
sum_ai = a[0]
for i in range(1, n):
    sum_ai += a[i]
    sum_a.append(sum_ai)
d = dict()
d[0] = 0
index_i = 0
ans = 0
for j in range(n):
    if sum_a[j] not in d:
        d[sum_a[j]] = j
    else:
        i = d[sum_a[j]]
        ans += (i - index_i + 1) * (n - j)
        d[sum_a[j]] = j
        index_i = i
print(ans)
