from array import *
def reverse(l):
    i = 0
    for i in range(int(len(l)/2)):
        l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]
    return l
    
h = [1, 3, 5, 6]
print(reverse(h))

