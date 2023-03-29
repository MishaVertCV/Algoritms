import random as ran
import numpy as np
from math import hypot
result = 0
result1_true = 0
result2_true = 0
type1 = ()
type2 = ()
t = 0
def generate1():  
    a = ran.uniform(0, 1)  
    b = ran.uniform(0, 1)  
    return (a * np.cos(2 * np.pi * b), a * np.sin(2 * np.pi * b))
def generate2():  
    while True:  
        x = ran.uniform(-1, 1)  
        y = ran.uniform(-1, 1)  
        if x ** 2 + y ** 2 > 1:  
            continue  
        return (x, y)
s = list()
l = list()
out = list()
for p1 in range(10000):
    type1 = generate1()
    result1_true += type1[0] ** 2 + type1[1] ** 2
result1_true = result1_true / 10000
print(result1_true)
for p2 in range(10000):
    type2 = generate2()
    result2_true += type2[0] ** 2 + type2[1] ** 2
result2_true = result2_true / 10000 
print(result2_true)  
for i in range(100):
    result = 0
    l.append(ran.randint(1, 2))
    for j in range(1000):
        if l[i] == 1:
            type1 = generate1()
            s.append(type1[0])
            s.append(type1[1])
        else:
            type2 = generate2()
            s.append(type2[0])
            s.append(type2[1])
    for k in range(len(s)):
        result += s[k] ** 2
    result = result / 1000
    print(result)
    if abs(result1_true - result) < abs(result2_true - result):
        out.append(1)
    else:
        out.append(2)
    s = list()
print(l)
print(out)
number = 0
for q in range(len(l)):
    if l[q] == out[q]:
        number += 1
print(number)



