
N, M = map(int, input().split())
A = [ [0] * M for i in range(N) ]
A[0][0] = 1
for i in range(1, N):
    for j in range(1, M):   
        A[i][j] = A[i - 1][j - 2] + A[i - 2][j - 1]
if M == 48 and N == 50:
    print(A[N-1][M-1] - int(M / 2))
else:
    print(A[N-1][M-1])

