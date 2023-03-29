M = int(input())
N = int(input())
A = list()
B = list()
for k in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for i in range(len(A) - 1):
    for j in range(i, len(A)):
        if A[i] <= B[j] and A[j] <= B[i] and i != j:
            A[i] = A[j]
            B[i] = B[j]
print(len(set(A)))
    