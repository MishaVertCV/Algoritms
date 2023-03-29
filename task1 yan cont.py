import numpy as np
n = int(input())
p = list()
meetings = list()
p_index = 0
index = 0
k = 0
z = 0
result = np.zeros(n)
l = list(map(int, input().split(maxsplit=n)))
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(1, len(a)):
        p.append(a[j])
        if p.index(a[j]) != index + j:
            while p.index(a[j]) > p_index:
                p_index += meetings[k]
                k += 1
            if l[i] == 1 or l[k+1] == 1:
                result[i] = 1
                result[k+1] = 1
    meetings.append(a[0])
    index += len(a) - 1
for z in range(n):
    if l[z] == 1:
        result[z] = 1
print(result)


    



