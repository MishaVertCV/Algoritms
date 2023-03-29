p1 = input().split()
p2 = input().split()
n = 0 
while p1 and p2:
    n += 1
    a, b = p1.pop(0), p2.pop(0)
    if a > b and (b, a) != ('0', '9') or (a, b) == ('0', '9'):
         p1 += [a, b]
    else:
         p2 += [a, b]
    if n == 1000000:
         print('botva')
         break
else:
    print('first' if p1 else 'second', n)



