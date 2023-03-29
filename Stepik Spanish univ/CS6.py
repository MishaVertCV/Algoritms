l = list(map(int, input().split()))
number = l[0]
roads = l[1]
k = list(map(int, input().split()))
x = 2
y = 1
result = 0
for i in range(roads-1):
    s = list(map(int, input().split()))
    if (s[0] in k and s[1] not in k) or (s[0] not in k and s[1] in k):
        x += 1
        y += 1
    if s[0] and s[1] in k:
        y += 1
    if s[0] not in k and s[1] not in k:
        result += (x*(x-1)/2) - y
        x = 2
        y = 1
    k.append(s[0])
    k.append(s[1])
if x != 2 and y != 1:
    result += (x*(x-1)/2) - y
print(int(result))

