N = int(input())
a = list(map(int, input().split()))
 
ans = [-1] * N
b = list()
for i in range(1, N):   
    while len(b) > 0 and a[i] < a[b[-1]]:
        ans[b.pop()] = i
    b.append(i)
 
print(*ans)
    


