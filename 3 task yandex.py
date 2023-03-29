file = open("input.txt", "r")
data = list()
for line in file:
    data.append(int(line))
N = int(data[0])
result = 0
for i in range(1, len(data)):
    result += data[i]
Cmse = result/N
print(Cmse)
del(data[0])
data.sort()
print(data[0])
