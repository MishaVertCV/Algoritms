from collections import Counter

def stringnum(s):
    t = Counter()
    for symbol in s:
        t[symbol] += 1
    return t
k = str(input())
print(stringnum(k))
