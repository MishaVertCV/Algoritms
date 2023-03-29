import numpy as np
n = int(input())
k = 0
t = 0
result = 0
for i in range(0, n):
    k = int(input())
    if k == 1:
        t += 1
        result = max(result, t)
    else:
        t = 0    
print(result)
