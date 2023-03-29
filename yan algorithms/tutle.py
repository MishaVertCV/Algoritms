N, M = map(int, input().split())
matrix = [[0] * (M + 1)]
for i in range(1, N + 1):
    matrix += [[0] + list(map(int, input().split()))]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])
l = list()
print(matrix[N][M])
while N != 1 or M != 1:
    if matrix[N - 1][M] >= matrix[N][M - 1]:
        l.append('D')
        N -= 1
    else: 
        l.append('R')
        M -= 1
    if N == 1:
        l += ['R'] * (M - 1)
        break
    if M == 1:
        l += ['D'] * (N - 1)
        break
print(' '.join(l[::-1]))

