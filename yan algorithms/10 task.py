s = str(input())
d = dict()
for letter in set(s):
    k = 0
    for i in range(len(s)):
        if letter == s[i]:
            k += (i + 1) * (len(s) - i)
    d[letter + ':'] = k
d = dict(sorted(d.items()))
for key in d:
    print(key, d[key])

