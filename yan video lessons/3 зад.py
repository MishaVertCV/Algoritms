from math import lcm
n = int(input())
res = None
for a in range(n):
    for b in range(n):
        if a+b == n:
            if not res:
                res = (a, b)
            else:
                if lcm(a, b)> lcm(*res):
                    res = a, b
print(*res)
