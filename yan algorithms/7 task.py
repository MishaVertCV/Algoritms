from datetime import time
from math import ceil
A = str(input())
B = str(input())
C = str(input())
def seconds(S):
    h = int(S[0:2])
    m = int(S[3:5])
    s = int(S[6:8])
    m += 60 * h
    s += 60 * m
    return s
if seconds(C) < seconds(A):
    right_time = ceil((seconds(C) + 3600 * 24 - seconds(A)) / 2)
else:
    right_time = ceil((seconds(C) - seconds(A)) / 2)
right_time += seconds(B)
if right_time >= 3600 * 24:
    right_time -= 3600 * 24
H = right_time // 3600
M = (right_time - H * 3600) // 60
Sec = right_time - H * 3600 - M * 60
right_time = time(H, M, Sec)
print(right_time)
