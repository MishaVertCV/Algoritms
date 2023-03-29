t = int(input())
o = input()
def beatiful(s, k):
    n = k
    right = 0
    a = 0
    for letter in set(s):
        for left in range(len(s)):
            while k > 0 or s[right + left] == letter:
                if letter != s[right + left]:
                    k -= 1
                right += 1
                if right + left == len(s):
                    break
            if left > right and k <= 0:
                break
            k = n
            a = max(a, right)
            right = 0
    return(a)
print(beatiful(o, t))




