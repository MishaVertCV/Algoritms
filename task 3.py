import random as rn
from math import sqrt
l = list(map(int, input().split()))
n = l[0]
k = l[1]
win = 0
mult = 1
for i in range(10000):
    for j in range(n):
        result = rn.randint(1, k)
        mult *= result
    a = int(sqrt(mult))
    b = int(mult/a)
    if a != b:
        win += 1 
    mult = 1 
p = int(win/10000 * 1000000007)     
print(p)

        

# p = win/1
# print(int(p * 1000000007))
