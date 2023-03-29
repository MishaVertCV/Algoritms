N = int(input())
n = list(map(int, input().split(maxsplit=N)))
K = int(input())
p = list(map(int, input().split(maxsplit=K)))
n.sort()
n = set(n)
n = list(n)
def binary_search(a, x): 
    mid = int(len(a) // 2)
    low = 0
    high = len(a) - 1
    while a[mid] != x and low <= high:
        if x > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return low
    else:
        return mid
for i in range(len(p)):
    print(binary_search(n, p[i]))


