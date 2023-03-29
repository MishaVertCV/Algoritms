def union(j, s):
    k = 0
    for stone in s:
        if stone in j:
            k += 1
    return k
a = 'df'
f = 'dfdfdkdfgfdgkldgrokih'
print(union(a, f))
