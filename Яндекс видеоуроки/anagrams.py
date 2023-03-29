from collections import Counter
k = str(input())
l = str(input())
def Anagrams(a, b):
    ca = Counter(a)
    cb = Counter(b)
    diff = ca - cb
    if len(diff) == 0 and len(a) == len(b):
        print(1)
    else:
        print(0)
print(Anagrams(k, l))

