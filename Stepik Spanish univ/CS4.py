l = list(map(int, input().split()))
n = l[0]
m = l[1]
cost = list(map(int, input().split(maxsplit=n)))
money = list(map(int, input().split(maxsplit=m)))
out = list()
k = 0
cost.sort()
for j in range(2):
    cost.insert(money[j])
    k = m - 1 - cost[::-1].index(money[j])
    out.append(k)
    print(cost)
    # del(cost[k])
print(' '.join(map(str, out)))

