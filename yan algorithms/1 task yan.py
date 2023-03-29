l = list()
k = list()
d = dict()
with open('input1.txt') as f:
    s = f.read()
for i in range(len(s)):
    if s[i] not in l and s[i] != '\n' and s[i] != ' ':
        l.append(s[i])
        k.append(s.count(s[i]))
        d[s[i]] = k[-1]
d = sorted(d.items())
for i in range(len(k)):
        k[i] = d[i][1]
high_number = max(k)
line = str()
for i in range(max(k)):
    for j in range(len(k)):
        if k[j] >= high_number:
            line += '#'
        else:
            line += ' '
    print(line)
    line = str()
    high_number -= 1
for i in range(len(l)):
    line += str(d[i][0])
print(line)
