l = [2, 4, 7]
N = int(input())
if N < 4:
    print(l[N - 1])
else:
    for i in range(3, N):
        a = l[i-1] + l[i-2] + l[i-3]
        l.append(a)
    print(l[-1])