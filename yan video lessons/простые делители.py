n = int(input())
i = 2
l = list()
while i * i <= n:
    while n % i == 0:
        l.append(i)
        n = n / i
    i = i + 1
if n > 1:
    l.append(n)
print(min(l))
         
    
