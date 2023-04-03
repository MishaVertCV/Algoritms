m = input().split()
k = 0
best = 0
for i in range(len(m)):
    if int(m[i]) > 0:
        k += 1
        best = max(best, k)
    else:
        k = 0
print((best))
        
        
