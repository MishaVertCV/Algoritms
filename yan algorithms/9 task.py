N, M, K = map(int, input().split())
A = [[int(it) for it in input().split()] for _ in range(N)]
def preprocess(mat):
    (M, N) = (len(mat), len(mat[0]))
 
    s = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
    s[0][0] = mat[0][0]
 
    for j in range(1, len(mat[0])):
        s[0][j] = mat[0][j] + s[0][j - 1]
 
    for i in range(1, len(mat)):
        s[i][0] = mat[i][0] + s[i - 1][0]
 
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            s[i][j] = mat[i][j] + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
 
    return s
 
def findSubmatrixSum(mat, p, q, r, s):
 
    if not mat or not len(mat):
        return 0
 
    mat = preprocess(mat)
    r -= 1
    s -= 1
    q -= 1
    p -= 1
 
    total = mat[r][s]
 
    if q - 1 >= 0:
        total -= mat[r][q - 1]
 
    if p - 1 >= 0:
        total -= mat[p - 1][s]
 
    if p - 1 >= 0 and q - 1 >= 0:
        total += mat[p - 1][q - 1]
 
    return total
for i in range(K):
    a, b, c, d = map(int, input().split())
    print(findSubmatrixSum(A, a, b, c, d))