a = float(input())

count = 0

while a != 1:

    if (a % 2 == 0 or a % 3 == 0):
        if (((a - 1) % 9 == 0) and a % 16 != 0):
            a = (a - 1)/9
            count += 3
        else:
            if ((a - 1) % 32 == 0):
                a = (a - 1)/32
                count += 6
            if (a % 16 == 0):
                a = a/16
                count += 4
            if (a % 16 != 0 and a % 2 == 0):
                a = a/2
                count += 1
            if (a % 9 == 0 or a % 3 == 0):
                a = a/3
                count += 1
    else:
        if a != 1:
            a = a - 1
            count += 1
        if a == 1:
            break
print(count)