n = int(input())
k = 0
l = list()
s = list()
for i in range(0, n):
    k = int(input())
    l.append(k)
l.sort()
for i in range(0, len(l)-1):
    if l[i] != l[i+1]:
        s.append(l[i])
if s[len(s)-1] != l[len(l)-1]:
    s.append(l[len(l)-1])
for i in range(len(s)):
    print(s[i])
    
    
    
