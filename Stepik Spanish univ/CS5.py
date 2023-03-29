import numpy as np
l = list(map(int, input().split()))
s = str(input())
k = list(map(str, input().split()))
result = list(map(int,(np.zeros(len(s)))))
x = 0
n = 0
for i in range(len(s)):
    if s[i] in k:
        result[i] = 1
for y in range(len(result)):
    if result[y] == 1:
        x += 1
    else:
        n += x*(x+1)/2
        x = 0
if x != 0:
    n += x*(x+1)/2
print(int(n))