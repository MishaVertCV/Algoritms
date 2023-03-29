l = list(map(str, input().split()))
p = list()
for i in  range(len(l)):
    if l[i] != '+' and l[i] != '-' and l[i] != '*':
        p.append(int(l[i]))
    if l[i] == '+':
        p.append(p[-1] + p[-2])
        p.pop(-2)
        p.pop(-2)
    if l[i] == '*':
        p.append(p[-1] * p[-2])
        p.pop(-2)
        p.pop(-2)
    if l[i] == '-':
        p.append(p[-2] - p[-1])
        p.pop(-2)
        p.pop(-2)
print(p[0])